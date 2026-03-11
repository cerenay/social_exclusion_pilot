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
    # Each choice is either 'A' or 'B'
    painting_choice_1 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #1")
    painting_choice_2 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #2")
    painting_choice_3 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #3")
    painting_choice_4 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #4")
    painting_choice_5 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #5")
    explanation = models.StringField(choices=['I liked the colours', 'I liked the shapes', 'The paintings calmed me down', 'I identify myself with the paintings', 'It was a random choice', 'Other - please specify'],  widget=widgets.RadioSelect, label="Before you continue to Part 2, can you briefly describe the reason behind your choice of the paintings?")
    consent = models.StringField(choices=[['Yes', 'Do not proceed'], ['No', 'Accept and proceed']],label='By selecting the “Accept and proceed” option, you indicate that you are 18 years of age or older, that you understand the above information and that you voluntarily agree to participate in this study.',widget=widgets.RadioSelect)

    def count_klee_choices(self):
        return sum([
            self.painting_choice_1 == 'A',
            self.painting_choice_2 == 'A',
            self.painting_choice_3 == 'A',
            self.painting_choice_4 == 'A',
            self.painting_choice_5 == 'A',
        ])

    def count_kandinsky_choices(self):
        return 5 - self.count_klee_choices()


class Welcome(Page):
    form_model = 'player'
    form_fields = ['consent']

class Intro(Page):
    pass

class PaintingChoice(Page):
    form_model = 'player'
    form_fields = [
        'painting_choice_1',
        'painting_choice_2',
        'painting_choice_3',
        'painting_choice_4',
        'painting_choice_5',
    ]

    def vars_for_template(player):
        # Optional: Define who is A or B for each pair if needed
        # For example, randomly assign Klee/Kandinsky to A/B
        return {}

class Transition(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        num_klee = player.count_klee_choices()
        if num_klee >= 3:
            player.participant.vars['painting_group'] = 'Klee'
        else:
            player.participant.vars['painting_group'] = 'Kandinsky'

class Explanation(Page):
    form_model = 'player'
    form_fields = ['explanation']


page_sequence = [Welcome, Intro, PaintingChoice, Transition, Explanation]