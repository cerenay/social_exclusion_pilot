from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'painting_choice'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_PAIRS = 5
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


def creating_session(subsession):
    # For each participant, independently randomize — for every pair — which
    # letter (A or B) corresponds to the Klee painting. Stored as a 5-character
    # string like "ABBAB".  This way, answering "A" for every pair does not
    # automatically place the participant into the Klee (or Kandinsky) group.
    for p in subsession.get_players():
        p.klee_letter_map = ''.join(random.choice('AB') for _ in range(C.NUM_PAIRS))


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    painting_choice_1 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #1")
    painting_choice_2 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #2")
    painting_choice_3 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #3")
    painting_choice_4 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #4")
    painting_choice_5 = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, label="Pair #5")
    # 5-character string, one letter per pair, identifying which radio button
    # (A or B) is the Klee painting for this participant on that pair.
    # Populated in creating_session().
    klee_letter_map = models.StringField()
    # Stores semicolon-separated list of selected reasons (multi-select, rendered manually in template)
    explanation = models.StringField(blank=True, label="Before you continue to Part 2, can you briefly describe the reason behind your choice of the paintings?")
    explanation_other_text = models.StringField(blank=True, label="Please specify")
    consent = models.StringField(
        choices=[['accept', 'Accept and proceed'], ['decline', 'Do not proceed']],
        label='By selecting the "Accept and proceed" option, you indicate that you are 18 years of age or older, that you understand the above information and that you voluntarily agree to participate in this study.',
        widget=widgets.RadioSelect
    )

    def count_klee_choices(self):
        # For each pair, the Klee painting corresponds to the letter stored at
        # that position in klee_letter_map (per-participant randomization).
        mapping = self.klee_letter_map or ''
        choices = [
            self.painting_choice_1,
            self.painting_choice_2,
            self.painting_choice_3,
            self.painting_choice_4,
            self.painting_choice_5,
        ]
        return sum(
            choice == mapping[i]
            for i, choice in enumerate(choices)
            if i < len(mapping)
        )

    def count_kandinsky_choices(self):
        return C.NUM_PAIRS - self.count_klee_choices()


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
        # Build a list of (pair_index, klee_letter) pairs so the template can
        # display the Klee painting on either the A or B side, based on this
        # participant's randomly-assigned mapping.
        mapping = player.klee_letter_map or 'A' * C.NUM_PAIRS
        pairs = [(i + 1, mapping[i]) for i in range(C.NUM_PAIRS)]
        return dict(pairs=pairs)

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
