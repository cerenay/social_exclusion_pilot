from random import choices

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
    question_1 = models.StringField(
        choices=['Klee', 'Kandisky'],
        widget=widgets.RadioSelect,
        label="Which painting group were you assigned to in Part 1 of the study?")
    question_2a = models.StringField(
        choices=['Very unfamiliar', 'Unfamiliar', 'Neither unfamiliar nor familiar', 'Familiar', 'Very familiar'],
        widget=widgets.RadioSelect,
        label="How familiar were you with paintings made by Klee before this study?")
    question_2b = models.StringField(
        choices=['Very unfamiliar', 'Unfamiliar', 'Neither unfamiliar nor familiar', 'Familiar', 'Very familiar'],
        widget=widgets.RadioSelect,
        label="How familiar were you with paintings made by Kandisky before this study?")
    question_3 = models.StringField(
        choices=['Strongly disagree', 'Disagree', 'Neither disagree nor agree', 'Agree', 'Strongly agree'],
        widget=widgets.RadioSelectHorizontal,
        label="I felt like I belonged to my group throughout the study")
    question_4 = models.StringField(
        choices=['Strongly disagree', 'Disagree', 'Neither disagree nor agree', 'Agree', 'Strongly agree'],
        widget=widgets.RadioSelectHorizontal,
        label="I felt left out because of my group")
    question_5 = models.StringField(
        choices=['Strongly disagree', 'Disagree', 'Neither disagree nor agree', 'Agree', 'Strongly agree'],
        widget=widgets.RadioSelectHorizontal,
        label="The task I was assigned to was easy")
    question_6 = models.StringField(
        choices=['Strongly disagree', 'Disagree', 'Neither disagree nor agree', 'Agree', 'Strongly agree'],
        widget=widgets.RadioSelectHorizontal,
        label="The decision about the version of my task was unfair")
    question_7 = models.StringField(
        choices=['Strongly disagree', 'Disagree', 'Neither disagree nor agree', 'Agree', 'Strongly agree'],
        widget=widgets.RadioSelectHorizontal,
        label="I felt valued by the person who assigned the version of my task")
    question_8 = models.StringField(
        choices=['Strongly disagree', 'Disagree', 'Neither disagree nor agree', 'Agree', 'Strongly agree'],
        widget=widgets.RadioSelectHorizontal,
        label="The person who assigned the version of my task favored their own group")
    question_9 = models.StringField(
        choices=['Try to allocate money equally between us','Try to allocate more money to myself', 'Try to allocate more money to the other participant', 'Randomly', 'Other - Please specify:'],
        widget=widgets.RadioSelect,
        label="In Part 3 when you were asked to allocate money between yourself and another participant, how would you describe the strategy you used?")
    question_10a = models.StringField(
        choices=['Try to allocate money equally between us', 'Try to allocate more money to myself',
                 'Try to allocate more money to the other participant', 'Randomly', 'Other - Please specify:'],
        widget=widgets.RadioSelect,
        label="In Part 3 when you were asked to allocate money between yourself and a participant from your own group, how would you describe the strategy you used?")
    question_10b = models.StringField(
        choices=['Try to allocate money equally between us', 'Try to allocate more money to myself',
                 'Try to allocate more money to the other participant', 'Randomly', 'Other - Please specify:'],
        widget=widgets.RadioSelect,
        label="In Part 3 when you were asked to allocate money between yourself and a participant from the other group, how would you describe the strategy you used?")
    question_11a = models.StringField(
        choices=['Try to allocate money equally between us', 'Try to allocate more money to myself',
                 'Try to allocate more money to the other participant', 'Randomly', 'Other - Please specify:'],
        widget=widgets.RadioSelect,
        label="In Part 3 when you were asked to allocate money between yourself and a participant who performed the easy task, how would you describe the strategy you used?")
    question_11b = models.StringField(
        choices=['Try to allocate money equally between us', 'Try to allocate more money to myself',
                 'Try to allocate more money to the other participant', 'Randomly', 'Other - Please specify:'],
        widget=widgets.RadioSelect,
        label="In Part 3 when you were asked to allocate money between yourself and a participant who performed the difficult task, how would you describe the strategy you used?")

    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    education = models.StringField(
        choices=[['Completed some high school', 'Completed some high school'], ['High school graduate', 'High school graduate']],
        label='What is the highest level of education you have completed?',
        widget=widgets.RadioSelect,
    )
    donation = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No']],
        label='In the past twelve months, have you donated money to or done volunteer work for charities or other nonprofit organizations?',
        widget=widgets.RadioSelect,
    )

class Postexp_surv1(Page):
        form_model = 'player'
        form_fields = ['question_1', 'question_2a', 'question_2b']


class Postexp_surv2(Page):
    form_model = 'player'
    form_fields = ['question_3', 'question_4', 'question_5', 'question_6',
                   'question_7', 'question_8']

class Postexp_surv3(Page):
    form_model = 'player'
    form_fields = ['question_9', 'question_10a', 'question_10b', 'question_11a',
                   'question_11b']

class Demo(Page):
        form_model = 'player'
        form_fields = ['age', 'gender', 'education', 'donation']

class EndSurvey(Page):
    pass

page_sequence = [Postexp_surv1, Postexp_surv2, Postexp_surv3, Demo, EndSurvey]