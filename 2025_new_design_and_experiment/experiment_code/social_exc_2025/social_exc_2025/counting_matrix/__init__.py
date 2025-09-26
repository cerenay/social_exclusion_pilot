from otree.api import *


doc = """
Your app description
"""



class C(BaseConstants):
    NAME_IN_URL = 'counting_matrix'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


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
    matrix_answer = models.IntegerField(label="How many 0s did you count?")
    correct_zeros = models.IntegerField(blank=True)
    slider1 = models.IntegerField(min=0, max=100, label="Slider 1")
    slider2 = models.IntegerField(min=0, max=100, label="Slider 2")
    slider3 = models.IntegerField(min=0, max=100, label="Slider 3")
    slider4 = models.IntegerField(min=0, max=100, label="Slider 4")
    slider5 = models.IntegerField(min=0, max=100, label="Slider 5")
    task_difficulty=models.StringField()


# PAGES
class Instructions(Page):
    pass

import random

class MatrixTask(Page):
    form_model = 'player'
    form_fields = ['slider1', 'slider2', 'slider3', 'slider4', 'slider5']

    @staticmethod
    def vars_for_template(player: Player):
        difficulty = player.task_difficulty
        min_val, max_val = (40, 60) if difficulty == 'easy' else (50, 55)
        return dict(min_val=min_val, max_val=max_val, difficulty=difficulty)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Set correct interval based on difficulty
        if player.task_difficulty == 'easy':
            lower, upper = 40, 60
        else:
            lower, upper = 50, 55

        sliders = [player.slider1, player.slider2, player.slider3, player.slider4, player.slider5]
        correct = sum(lower <= val <= upper for val in sliders)
        player.correct_zeros = correct

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Instructions, MatrixTask]
