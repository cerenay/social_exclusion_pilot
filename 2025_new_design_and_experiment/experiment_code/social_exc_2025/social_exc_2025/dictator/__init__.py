from otree.api import *


doc = """
Dictator Game - Strategy Method Version
Participants make allocation decisions in 5 rounds with varying context.
All decisions are made up front using the strategy method.
One round is randomly selected for payment.
"""


class C(BaseConstants):
    NAME_IN_URL = 'dictator_strategy'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = cu(20)
    ROUNDS = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    selected_round = models.IntegerField()
    treatment = models.StringField()  # for potential use later

    def set_payoffs(self):
        allocator = self.get_player_by_role("allocator")
        recipient = self.get_player_by_role("recipient")

        # Select random round
        import random
        self.selected_round = random.randint(1, C.ROUNDS)

        # Get allocator's choice for that round
        selected_amount = getattr(allocator, f'choice_round_{self.selected_round}')

        allocator.payoff = C.ENDOWMENT - selected_amount
        recipient.payoff = selected_amount


class Player(BasePlayer):
    # One field per round
    choice_round_1 = models.CurrencyField(min=0, max=C.ENDOWMENT, label="How much do you want to send?")
    choice_round_2 = models.CurrencyField(min=0, max=C.ENDOWMENT, label="If the recipient is from your group / other group")
    choice_round_3 = models.CurrencyField(min=0, max=C.ENDOWMENT, label="If the recipient did easy / hard task")
    #choice_round_4 = models.CurrencyField(min=0, max=C.ENDOWMENT, label="If the recipient is from your group and did easy / hard task")
    #choice_round_5 = models.CurrencyField(min=0, max=C.ENDOWMENT, label="If the recipient is from the other group and did easy / hard task")

    def role(self):
        return "allocator" if self.id_in_group == 1 else "recipient"


# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Offer(Page):
    form_model = 'player'
    form_fields = [
        'choice_round_1',
        'choice_round_2',
        'choice_round_3'
    ]

    @staticmethod
    def is_displayed(player):
        return player.role() == "allocator"


class WaitForAll(WaitPage):
    after_all_players_arrive = Group.set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player):
        group = player.group
        allocator = group.get_player_by_role("allocator")
        selected = group.selected_round
        sent = getattr(allocator, f'choice_round_{selected}')
        kept = C.ENDOWMENT - sent

        return dict(
            selected_round=selected,
            sent=sent,
            kept=kept,
            role=player.role(),
            my_payoff=player.payoff
        )

page_sequence = [
    Introduction,
    Offer,
    WaitForAll,
    Results
]

