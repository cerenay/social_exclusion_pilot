from otree.api import *

from survey import Demographics

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'quest'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_1 = models.StringField(choices=['Strongly disagree', 'Disagree', 'Neither disagree nor agree', 'Agree', 'Strongly agree'], widget=widgets.RadioSelectHorizontal, label="The task I was assigned was easy")
    question_2 = models.StringField(choices=['Strongly disagree', 'Disagree', 'Neither disagree nor agree', 'Agree', 'Strongly agree'], widget=widgets.RadioSelectHorizontal, label="I felt like I belonged to my group")
    question_3 = models.StringField(choices=['Strongly disagree', 'Disagree', 'Neither disagree nor agree', 'Agree', 'Strongly agree'], widget=widgets.RadioSelectHorizontal, label="I felt valued by the person that assigned the version of the task")
    question_4 = models.StringField(choices=['Strongly disagree', 'Disagree', 'Neither disagree nor agree', 'Agree', 'Strongly agree'], widget=widgets.RadioSelectHorizontal, label="I felt left out because of my group")
    question_5 = models.StringField(choices=['Strongly disagree', 'Disagree', 'Neither disagree nor agree', 'Agree', 'Strongly agree'], widget=widgets.RadioSelectHorizontal, label="The decision about my task was unfair")
    question_6 = models.StringField(choices=['Strongly disagree', 'Disagree', 'Neither disagree nor agree', 'Agree', 'Strongly agree'], widget=widgets.RadioSelectHorizontal, label="The person who assigned the version of the task favored their own group")
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )

    class Postexp_surv(Page):
        form_model = 'player'
        form_fields = ['question_1', 'question_2', 'question_3', 'question_4', 'question_5', 'question_6']

    class Demo(Page):
        form_model = 'player'
        form_fields = ['age', 'gender']

page_sequence = [Postexp_surv, Demo]