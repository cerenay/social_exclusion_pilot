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
    FAMILIAR_CHOICES = ['Very unfamiliar', 'Unfamiliar', 'Neither unfamiliar nor familiar', 'Familiar', 'Very familiar']
    AGREE_CHOICES = ['Strongly disagree', 'Disagree', 'Neither disagree nor agree', 'Agree', 'Strongly agree']
    EMOTION_CHOICES = ['Not at all', 'To some extent', 'Moderately', 'Very much', 'Extremely']

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
        choices=C.FAMILIAR_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label="Klee")
    question_2b = models.StringField(
        choices=C.FAMILIAR_CHOICES,
        widget=widgets.RadioSelect,
        label="Kandisky")

    question_3 = models.StringField(choices=C.AGREE_CHOICES, widget=widgets.RadioSelectHorizontal,
                                    label="I felt attached to my own group throughout the study.")
    question_4 = models.StringField(choices=C.AGREE_CHOICES, widget=widgets.RadioSelectHorizontal,
                                    label="I felt left out because of my group.")
    question_5 = models.StringField(choices=C.AGREE_CHOICES, widget=widgets.RadioSelectHorizontal,
                                    label="I felt my group was devalued in this interaction.")
    question_6 = models.StringField(choices=C.AGREE_CHOICES, widget=widgets.RadioSelectHorizontal,
                                    label="I felt valued by the independent participant/system that assigned the task.")
    question_7 = models.StringField(choices=C.AGREE_CHOICES, widget=widgets.RadioSelectHorizontal,
                                    label="The independent participant assigning the task favoured their own group.")
    question_8 = models.StringField(choices=C.AGREE_CHOICES, widget=widgets.RadioSelectHorizontal,
                                    label="I was given this task because of my group.")
    question_9 = models.StringField(choices=C.AGREE_CHOICES, widget=widgets.RadioSelectHorizontal,
                                    label="The decision about my task was unfair.")
    question_10 = models.StringField(choices=C.AGREE_CHOICES, widget=widgets.RadioSelectHorizontal,
                                     label="The task I was assigned to was easy.")


    question_11_upset = models.StringField(choices=C.EMOTION_CHOICES, label="Upset", widget=widgets.RadioSelectHorizontal)
    question_11_angry = models.StringField(choices=C.EMOTION_CHOICES, label="Angry", widget=widgets.RadioSelectHorizontal)
    question_11_sad = models.StringField(choices=C.EMOTION_CHOICES, label="Sad", widget=widgets.RadioSelectHorizontal)
    question_11_anxious = models.StringField(choices=C.EMOTION_CHOICES, label="Anxious", widget=widgets.RadioSelectHorizontal)
    question_11_frustrated = models.StringField(choices=C.EMOTION_CHOICES, label="Frustrated", widget=widgets.RadioSelectHorizontal)
    question_11_discouraged = models.StringField(choices=C.EMOTION_CHOICES, label="Discouraged", widget=widgets.RadioSelectHorizontal)

    question_12 = models.StringField(
        choices=['Try to allocate money equally between us','Try to allocate more money to myself', 'Try to allocate more money to the other participant', 'Randomly', 'Other - Please specify:'],
        widget=widgets.RadioSelect,
        label="In Part 3 when you were asked to allocate money between yourself and another participant, how would you describe the strategy you used?")
    question_13 = models.StringField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect,
        label="In Part 3, when you were asked to allocate money between yourself and another participant, did it affect your decision in any way which group the other participant came from?")
    question_14a = models.StringField(
        choices=['Try to allocate money equally between us', 'Try to allocate more money to myself',
                 'Try to allocate more money to the other participant', 'Randomly', 'Other - Please specify:'],
        widget=widgets.RadioSelect,
        label="In Part 3 when you were asked to allocate money between yourself and a participant from your own group, how would you describe the strategy you used?")
    question_14b = models.StringField(
        choices=['Try to allocate money equally between us', 'Try to allocate more money to myself',
                 'Try to allocate more money to the other participant', 'Randomly', 'Other - Please specify:'],
        widget=widgets.RadioSelect,
        label="In Part 3 when you were asked to allocate money between yourself and a participant from the other group, how would you describe the strategy you used?")
    question_15 = models.StringField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect,
        label="In Part 3, when you were asked to allocate money between yourself and another participant, did it affect your decision in any way which task the other participant performed?")
    question_16a = models.StringField(
        choices=['Try to allocate money equally between us', 'Try to allocate more money to myself',
                 'Try to allocate more money to the other participant', 'Randomly', 'Other - Please specify:'],
        widget=widgets.RadioSelect,
        label="In Part 3 when you were asked to allocate money between yourself and a participant who performed the easy task, how would you describe the strategy you used?")
    question_16b = models.StringField(
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
    sibling = models.StringField(
        choices=[['0', '0 siblings'], ['1-2', '1-2 siblings'],
                 ['3', '3 or more siblings']],
        label='How many siblings do you have?',
        widget=widgets.RadioSelect,
    )
    economics = models.StringField(
        choices=[['Yes', 'Yes - please specify'], ['No', 'No']],
        label='Have you ever participated in any economics or psychology experimental studies before?',
        widget=widgets.RadioSelect,
    )
    background = models.StringField(
        choices=[['White', 'White'], ['Black', 'Black'], ['Hispanic', 'Hispanic'], ['Asian', 'Asian'], ['Other', 'Other - please specify']],
        label='What do you consider your racial or ethnic background to be?',
        widget=widgets.RadioSelect,
    )
    donation = models.StringField(
        choices=[['Yes', 'Yes - please specify'], ['Amount', 'Amount donated'], ['Hours', 'Number of hours volunteered'], ['No', 'No']],
        label='In the past twelve months, have you donated money to or done volunteer work for charities or other nonprofit organizations?',
        widget=widgets.RadioSelect,
    )

class Postexp_surv1(Page):
    form_model = 'player'
    form_fields = ['question_1', 'question_2a', 'question_2b']

    @staticmethod
    def vars_for_template(player):
        return dict(
            familiar_fields=[
                ('question_2a', 'Klee'),
                ('question_2b', 'Kandinsky'),
            ],
            familiar_choices=C.FAMILIAR_CHOICES,
        )

class Postexp_surv2(Page):
    form_model = 'player'
    form_fields = ['question_3', 'question_4', 'question_5', 'question_6',
                   'question_7', 'question_8', 'question_9', 'question_10']

    @staticmethod
    def vars_for_template(player):
        return dict(
            agree_fields=[
                ('question_3', 'I felt attached to my own group throughout the study.'),
                ('question_4', 'I felt left out because of my group.'),
                ('question_5', 'I felt my group was devalued in this interaction.'),
                ('question_6', 'I felt valued by the independent participant/system that assigned the task.'),
                ('question_7', 'The independent participant assigning the task favoured their own group.'),
                ('question_8', 'I was given this task because of my group.'),
                ('question_9', 'The decision about my task was unfair.'),
                ('question_10', 'The task I was assigned to was easy.'),
            ],
            agree_choices=C.AGREE_CHOICES,
        )

class Postexp_surv2b(Page):
    form_model = 'player'
    form_fields = ['question_11_upset', 'question_11_angry', 'question_11_sad',
                    'question_11_anxious', 'question_11_frustrated', 'question_11_discouraged']

    @staticmethod
    def vars_for_template(player):
        return dict(
            emotion_fields=[
                ('question_11_upset', 'Upset'),
                ('question_11_angry', 'Angry'),
                ('question_11_sad', 'Sad'),
                ('question_11_anxious', 'Anxious'),
                ('question_11_frustrated', 'Frustrated'),
                ('question_11_discouraged', 'Discouraged'),
            ],
            choices=C.EMOTION_CHOICES,
        )

class Postexp_surv3(Page):
    form_model = 'player'
    form_fields = ['question_12', 'question_13', 'question_14a', 'question_14b',
                   'question_15', 'question_16a', 'question_16b']

class Demo(Page):
        form_model = 'player'
        form_fields = ['age', 'gender', 'education', 'sibling', 'economics', 'background', 'donation']

class EndSurvey(Page):
    pass

page_sequence = [Postexp_surv1, Postexp_surv2, Postexp_surv2b, Postexp_surv3, Demo, EndSurvey]