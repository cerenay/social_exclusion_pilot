from otree.api import *
import random


doc = """
Dictator Game - Strategy Method Version
Participants make allocation decisions across 3 rounds. Rounds 2 and 3 each
have two scenarios. All decisions are made up-front using the strategy method.
One round (and for rounds 2 & 3 one scenario) is randomly selected for payment.
"""


class C(BaseConstants):
    NAME_IN_URL = 'dictator_strategy'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = cu(20)
    ROUNDS = 3  # we have Round 1, Round 2 (x2 scenarios), Round 3 (x2 scenarios)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    selected_round = models.IntegerField()
    # Only meaningful for selected_round == 2 or 3; otherwise defaulted to 1.
    selected_scenario = models.IntegerField()
    treatment = models.StringField()  # for potential use later

    def set_payoffs(self):
        allocator = self.get_player_by_role("allocator")
        recipient = self.get_player_by_role("recipient")

        # Randomly pick which round (1, 2, or 3) determines payoffs.
        self.selected_round = random.randint(1, C.ROUNDS)

        # Rounds 2 and 3 have two scenarios each; round 1 has a single decision.
        if self.selected_round == 1:
            self.selected_scenario = 1
            kept = allocator.choice_round_1a
            sent = allocator.choice_round_1b
        else:
            self.selected_scenario = random.randint(1, 2)
            kept = getattr(
                allocator,
                f'choice_round_{self.selected_round}_{self.selected_scenario}a',
            )
            sent = getattr(
                allocator,
                f'choice_round_{self.selected_round}_{self.selected_scenario}b',
            )

        allocator.payoff = kept
        recipient.payoff = sent


class Player(BasePlayer):
    # One field per round
    choice_round_1a = models.CurrencyField(min=0, max=C.ENDOWMENT, label="You")
    choice_round_1b = models.CurrencyField(min=0, max=C.ENDOWMENT, label="Other participant")
    choice_round_2_1a = models.CurrencyField(min=0, max=C.ENDOWMENT, label="You")
    choice_round_2_1b = models.CurrencyField(min=0, max=C.ENDOWMENT, label="Other participant")
    choice_round_2_2a = models.CurrencyField(min=0, max=C.ENDOWMENT, label="You")
    choice_round_2_2b = models.CurrencyField(min=0, max=C.ENDOWMENT, label="Other participant")
    choice_round_3_1a = models.CurrencyField(min=0, max=C.ENDOWMENT, label="You")
    choice_round_3_1b = models.CurrencyField(min=0, max=C.ENDOWMENT, label="Other participant")
    choice_round_3_2a = models.CurrencyField(min=0, max=C.ENDOWMENT, label="You")
    choice_round_3_2b = models.CurrencyField(min=0, max=C.ENDOWMENT, label="Other participant")
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
    pass




def _allocation_error(values, scenarios):
    """Return an error string if any scenario's (kept + sent) != ENDOWMENT.

    `scenarios` is a list of (label, kept_field, sent_field) tuples.
    """
    endowment = int(C.ENDOWMENT)
    bad = []
    for label, a_field, b_field in scenarios:
        a = values.get(a_field) or 0
        b = values.get(b_field) or 0
        if int(a) + int(b) != endowment:
            bad.append(f"{label} (you {int(a)} + other {int(b)} = {int(a) + int(b)})")
    if bad:
        return (
            f"Your allocation must total exactly {endowment} EMU in each scenario. "
            f"Please fix: {'; '.join(bad)}."
        )
    return None


class offer_1(Page):
    form_model = 'player'
    form_fields = ['choice_round_1a', 'choice_round_1b']

    @staticmethod
    def is_displayed(player):
        return player.role() == "allocator"

    @staticmethod
    def vars_for_template(player):
        return dict(endowment=int(C.ENDOWMENT))

    @staticmethod
    def error_message(player, values):
        return _allocation_error(
            values,
            [("Round 1", 'choice_round_1a', 'choice_round_1b')],
        )


class offer_2(Page):
    form_model = 'player'
    form_fields = ['choice_round_2_1a', 'choice_round_2_1b',
                   'choice_round_2_2a', 'choice_round_2_2b']

    @staticmethod
    def is_displayed(player):
        return player.role() == "allocator"

    @staticmethod
    def vars_for_template(player):
        own_group   = player.participant.vars.get('painting_group', '')
        other_group = 'Kandinsky' if own_group == 'Klee' else 'Klee'
        own_color   = 'green' if own_group == 'Klee' else 'red'
        other_color = 'green' if other_group == 'Klee' else 'red'
        return dict(
            endowment   = int(C.ENDOWMENT),
            own_group   = own_group,
            other_group = other_group,
            own_color   = own_color,
            other_color = other_color,
        )

    @staticmethod
    def error_message(player, values):
        return _allocation_error(
            values,
            [
                ("Scenario 1 (in-group)",  'choice_round_2_1a', 'choice_round_2_1b'),
                ("Scenario 2 (out-group)", 'choice_round_2_2a', 'choice_round_2_2b'),
            ],
        )


class offer_3(Page):
    form_model = 'player'
    form_fields = ['choice_round_3_1a', 'choice_round_3_1b',
                   'choice_round_3_2a', 'choice_round_3_2b']

    @staticmethod
    def is_displayed(player):
        return player.role() == "allocator"

    @staticmethod
    def vars_for_template(player):
        return dict(endowment=int(C.ENDOWMENT))

    @staticmethod
    def error_message(player, values):
        return _allocation_error(
            values,
            [
                ("Scenario 1 (easy task)", 'choice_round_3_1a', 'choice_round_3_1b'),
                ("Scenario 2 (hard task)", 'choice_round_3_2a', 'choice_round_3_2b'),
            ],
        )



class WaitForAll(WaitPage):
    after_all_players_arrive = Group.set_payoffs


# Human-readable scenario descriptions used on the Results page so the
# participant understands which scenario was selected.
SCENARIO_TEXT = {
    2: {
        1: "the other participant is from your painting group",
        2: "the other participant is from the other painting group",
    },
    3: {
        1: "the other participant previously completed the easy slider task",
        2: "the other participant previously completed the hard slider task",
    },
}


def _get_choice(allocator, selected_round, selected_scenario):
    """Return (kept, sent) for the selected round/scenario."""
    if selected_round == 1:
        return allocator.choice_round_1a, allocator.choice_round_1b
    kept = getattr(allocator, f'choice_round_{selected_round}_{selected_scenario}a')
    sent = getattr(allocator, f'choice_round_{selected_round}_{selected_scenario}b')
    return kept, sent


class Results(Page):
    @staticmethod
    def vars_for_template(player):
        group = player.group
        allocator = group.get_player_by_role("allocator")
        selected_round = group.selected_round
        selected_scenario = group.selected_scenario

        kept, sent = _get_choice(allocator, selected_round, selected_scenario)

        scenario_desc = None
        if selected_round in SCENARIO_TEXT:
            scenario_desc = SCENARIO_TEXT[selected_round].get(selected_scenario)

        return dict(
            selected_round=selected_round,
            selected_scenario=selected_scenario,
            scenario_desc=scenario_desc,
            sent=sent,
            kept=kept,
            role=player.role(),
            my_payoff=player.payoff,
        )


class totPayoffs(Page):
    @staticmethod
    def vars_for_template(player):
        # Part 1 (painting choice) is identity formation only => no payoff.
        # Part 2 (effort task) pays a fixed amount regardless of difficulty.
        # Part 3 (dictator) payoff comes from the selected-round allocation.
        part1_payoff = 0
        part2_payoff = 10  # EMU — adjust as needed
        part3_payoff = int(player.payoff)
        total_payoff = part1_payoff + part2_payoff + part3_payoff

        exchange_rate = 10  # 10 EMU = £1
        earnings_gbp = total_payoff / exchange_rate

        payoff_rows = [
            ("Part 1 (painting choice)", part1_payoff),
            ("Part 2 (slider task)", part2_payoff),
            ("Part 3 (allocation decision)", part3_payoff),
        ]

        return dict(
            payoff_rows=payoff_rows,
            total_payoff=total_payoff,
            exchange_rate=exchange_rate,
            earnings_gbp=f"{earnings_gbp:.2f}",
        )


page_sequence = [
    Introduction,
    Offer,
    offer_1,
    offer_2,
    offer_3,
    WaitForAll,
    Results,
    totPayoffs,
]

