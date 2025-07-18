from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'painting_choice'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    PAINTING_CHOICES = [
        ('klee', 'Paul Klee'),
        ('kandinsky', 'Wassily Kandinsky'),
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    painting_choice = models.StringField(
        choices=[
            ['klee', 'Paul Klee'],
            ['kandinsky', 'Wassily Kandinsky'],
        ],
        label="Which painting do you prefer?",
        widget=widgets.RadioSelectHorizontal,
    )

    explanation= models.StringField( label=" ")


class Welcome(Page):
    pass

class PaintingChoice(Page):
    form_model = 'player'
    form_fields = ['painting_choice']


class Explanation(Page):
    form_model = 'player'
    form_fields = ['explanation']

class Transition(Page):
    pass

page_sequence = [Welcome, PaintingChoice, Explanation, Transition]