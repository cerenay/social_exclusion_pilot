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
    task_difficulty=models.StringField()


# PAGES
class Instructions(Page):
    pass

import random

class MatrixTask(Page):
    form_model = 'player'
    form_fields = ['matrix_answer']

    def vars_for_template(player):
        if not player.task_difficulty:
            player.task_difficulty = random.choice(['easy', 'hard'])

        size = 5 if player.task_difficulty == 'easy' else 10
        matrix = [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]
        # Count 0s
        zero_count = sum(row.count(0) for row in matrix)
        player.correct_zeros = zero_count
        player.participant.vars['matrix'] = matrix
        return dict(
            matrix=matrix,
            size=size,
            difficulty=player.task_difficulty
        )
class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Instructions, MatrixTask]
