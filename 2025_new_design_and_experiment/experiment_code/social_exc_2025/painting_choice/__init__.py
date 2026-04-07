from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'painting_choice'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    PAINTING_CHOICES = [
        ('klee', 'Paul Klee'),
        ('kandinsky', 'Wassily Kandinsky'),
    ]
    EXPLANATION_OPTIONS = [
        'I liked the colours',
        'I liked the shapes',
        'The paintings calmed me down',
        'I identify myself with the paintings',
        'It was a random choice',
        'Other',
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    painting_choice_1 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #1")
    painting_choice_2 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #2")
    painting_choice_3 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #3")
    painting_choice_4 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #4")
    painting_choice_5 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #5")
    # Stores semicolon-separated list of selected reasons (multi-select, rendered manually in template)
    explanation = models.StringField(blank=True, label="Before you continue to Part 2, can you briefly describe the reason behind your choice of the paintings?")
    explanation_other_text = models.StringField(blank=True, label="Please specify")
    consent = models.StringField(
        choices=[['accept', 'Accept and proceed'], ['decline', 'Do not proceed']],
        label='By selecting the "Accept and proceed" option, you indicate that you are 18 years of age or older, that you understand the above information and that you voluntarily agree to participate in this study.',
        widget=widgets.RadioSelect
    )

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

    @staticmethod
    def vars_for_template(player):
        return {}

    @staticmethod
    def before_next_page(player, timeout_happened):
        # Assign painting group based on majority preference, before Transition page is shown
        num_klee = player.count_klee_choices()
        if num_klee >= 3:
            player.participant.vars['painting_group'] = 'Klee'
        else:
            player.participant.vars['painting_group'] = 'Kandinsky'

class Transition(Page):
    @staticmethod
    def vars_for_template(player):
        # Group is already set in PaintingChoice.before_next_page
        return dict(painting_group=player.participant.vars.get('painting_group', ''))

class Explanation(Page):
    form_model = 'player'
    form_fields = ['explanation', 'explanation_other_text']

    @staticmethod
    def vars_for_template(player):
        # Randomize all options except 'Other', which always appears last
        options = [o for o in C.EXPLANATION_OPTIONS if o != 'Other']
        random.shuffle(options)
        options.append('Other')
        return dict(options=options)


page_sequence = [Welcome, Intro, PaintingChoice, Transition, Explanation]
