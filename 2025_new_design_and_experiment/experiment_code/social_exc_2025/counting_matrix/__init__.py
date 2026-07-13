from otree.api import *
import random
import json
import time


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'counting_matrix'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Per-slider ranges for each difficulty level
    EASY_RANGES  = [[0, 20], [20, 40], [40, 60], [60, 80], [80, 100]]
    HARD_RANGES  = [[15, 20], [25, 30], [45, 50], [50, 55], [65, 70]]


class Subsession(BaseSubsession):
    pass

def creating_session(subsession):
    import itertools
    pressures = itertools.cycle(['easy', 'hard'])
    for player in subsession.get_players():
        player.task_difficulty = next(pressures)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    matrix_answer   = models.IntegerField(label="How many 0s did you count?")
    correct_zeros   = models.IntegerField(blank=True)
    slider1         = models.IntegerField(min=0, max=100, label="Slider 1")
    slider2         = models.IntegerField(min=0, max=100, label="Slider 2")
    slider3         = models.IntegerField(min=0, max=100, label="Slider 3")
    slider4         = models.IntegerField(min=0, max=100, label="Slider 4")
    slider5         = models.IntegerField(min=0, max=100, label="Slider 5")
    task_difficulty = models.StringField()
    slider_exp1     = models.IntegerField(min=0, max=100, label="Slider practice")
    # Stores the randomised per-slider ranges as JSON so they are available
    # in before_next_page and Results without regenerating them
    slider_ranges   = models.StringField(blank=True)
    # Seconds the participant spent on the MatrixTask page
    task_duration   = models.FloatField(blank=True)


# PAGES
class Instructions(Page):
    pass

class SliderExample(Page):
    form_model  = 'player'
    form_fields = ['slider_exp1']


class MatrixTask(Page):
    form_model  = 'player'
    form_fields = ['slider1', 'slider2', 'slider3', 'slider4', 'slider5']

    @staticmethod
    def vars_for_template(player: Player):
        difficulty = player.task_difficulty
        base_ranges = list(C.EASY_RANGES if difficulty == 'easy' else C.HARD_RANGES)
        random.shuffle(base_ranges)

        # Persist the shuffled ranges so before_next_page and Results can use them
        player.slider_ranges = json.dumps(base_ranges)

        # Record page-load time for duration tracking
        player.participant.vars['task_start'] = time.time()

        # Build a list of dicts for easy template access
        slider_ranges = [
            {'num': i + 1, 'min_val': r[0], 'max_val': r[1]}
            for i, r in enumerate(base_ranges)
        ]
        return dict(slider_ranges=slider_ranges, difficulty=difficulty)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        ranges = json.loads(player.slider_ranges)
        sliders = [player.slider1, player.slider2, player.slider3,
                   player.slider4, player.slider5]
        player.correct_zeros = sum(
            r[0] <= val <= r[1] for val, r in zip(sliders, ranges)
        )
        start = player.participant.vars.get('task_start', time.time())
        player.task_duration = round(time.time() - start, 2)
        # Persist task difficulty to participant.vars so the badge rendered in
        # the global page header surfaces it on every subsequent page (from the
        # slider Results page onwards).
        player.participant.vars['task_difficulty'] = player.task_difficulty


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        ranges = json.loads(player.slider_ranges)
        values = [player.slider1, player.slider2, player.slider3,
                  player.slider4, player.slider5]
        slider_results = [
            dict(
                num     = i + 1,
                value   = val,
                min_val = r[0],
                max_val = r[1],
                correct = r[0] <= val <= r[1],
            )
            for i, (val, r) in enumerate(zip(values, ranges))
        ]
        return dict(
            slider_results = slider_results,
            correct_count  = player.correct_zeros,
            difficulty     = player.task_difficulty,
            task_duration  = player.task_duration,
        )


page_sequence = [Instructions, SliderExample, MatrixTask, Results]
