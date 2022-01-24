import itertools
import json
import random

from otree.api import *


author = 'ceren ay'
doc = """
In this app players play in groups of 4 to split a total amount of 40
"""


class Constants(BaseConstants):
    name_in_url = 'stage_2'
    players_per_group = 4
    num_rounds = 1
    group_endowment = 40


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass
    ##1st round
    P1_1 = models.IntegerField()
    P2_1 = models.IntegerField()
    P3_1 = models.IntegerField()
    P4_1 = models.IntegerField()
    benef_2 = models.IntegerField()
    ##2nd round
    P1_2 = models.IntegerField()
    P2_2 = models.IntegerField()
    P3_2 = models.IntegerField()
    P4_2 = models.IntegerField()
    benef_3 = models.IntegerField()
    ##3rd Round
    P1_3 = models.IntegerField()
    P2_3 = models.IntegerField()
    P3_3 = models.IntegerField()
    P4_3 = models.IntegerField()
    benef_4 = models.IntegerField()
    ##4th round
    P1_4 = models.IntegerField()
    P2_4 = models.IntegerField()
    P3_4 = models.IntegerField()
    P4_4 = models.IntegerField()
    benef_5 = models.IntegerField()
    ##5th round
    P1_5 = models.IntegerField()
    P2_5 = models.IntegerField()
    P3_5 = models.IntegerField()
    P4_5 = models.IntegerField()
    benef_6 = models.IntegerField()
    ##6th round
    P1_6 = models.IntegerField()
    P2_6 = models.IntegerField()
    P3_6 = models.IntegerField()
    P4_6 = models.IntegerField()
    benef_7 = models.IntegerField()
    ##7th round
    P1_7 = models.IntegerField()
    P2_7 = models.IntegerField()
    P3_7 = models.IntegerField()
    P4_7 = models.IntegerField()
    benef_8 = models.IntegerField()
    ##8th round
    P1_8 = models.IntegerField()
    P2_8 = models.IntegerField()
    P3_8 = models.IntegerField()
    P4_8 = models.IntegerField()
    benef_9 = models.IntegerField()
    ##9th round
    P1_9 = models.IntegerField()
    P2_9 = models.IntegerField()
    P3_9 = models.IntegerField()
    P4_9 = models.IntegerField()
    benef_10 = models.IntegerField()
    ##10th round
    P1_10 = models.IntegerField()
    P2_10 = models.IntegerField()
    P3_10 = models.IntegerField()
    P4_10 = models.IntegerField()
    benef_11 = models.IntegerField()
    ##11th round
    P1_11 = models.IntegerField()
    P2_11 = models.IntegerField()
    P3_11 = models.IntegerField()
    P4_11 = models.IntegerField()
    benef_12 = models.IntegerField()
    ##12th round
    P1_12 = models.IntegerField()
    P2_12 = models.IntegerField()
    P3_12 = models.IntegerField()
    P4_12 = models.IntegerField()
    benef_13 = models.IntegerField()
    ##13th round
    P1_13 = models.IntegerField()
    P2_13 = models.IntegerField()
    P3_13 = models.IntegerField()
    P4_13 = models.IntegerField()
    benef_14 = models.IntegerField()
    ##14th round
    P1_14 = models.IntegerField()
    P2_14 = models.IntegerField()
    P3_14 = models.IntegerField()
    P4_14 = models.IntegerField()
    benef_15 = models.IntegerField()
    ##15th round
    P1_15 = models.IntegerField()
    P2_15 = models.IntegerField()
    P3_15 = models.IntegerField()
    P4_15 = models.IntegerField()
    benef_16 = models.IntegerField()
    ##16th round
    P1_16 = models.IntegerField()
    P2_16 = models.IntegerField()
    P3_16 = models.IntegerField()
    P4_16 = models.IntegerField()
    benef_17 = models.IntegerField()
    ##17th round
    P1_17 = models.IntegerField()
    P2_17 = models.IntegerField()
    P3_17 = models.IntegerField()
    P4_17 = models.IntegerField()
    benef_18 = models.IntegerField()
    ##18th round
    P1_18 = models.IntegerField()
    P2_18 = models.IntegerField()
    P3_18 = models.IntegerField()
    P4_18 = models.IntegerField()
    benef_19 = models.IntegerField()
    ##19th round
    P1_19 = models.IntegerField()
    P2_19 = models.IntegerField()
    P3_19 = models.IntegerField()
    P4_19 = models.IntegerField()
    benef_20 = models.IntegerField()


##20th round
class Player(BasePlayer):
    points = models.FloatField()
    payoff2 = models.IntegerField()
    first_benef = models.IntegerField()
    P1_initial = models.IntegerField()
    P2_initial = models.IntegerField()
    P3_initial = models.IntegerField()
    P4_initial = models.IntegerField()
    P1_luck = models.IntegerField()
    P2_luck = models.IntegerField()
    P3_luck = models.IntegerField()
    P4_luck = models.IntegerField()
    first_income = models.FloatField()
    ##Questionnairre after Stage 2
    exclusion = models.IntegerField(
        blank=False,
        choices=[
            [1, 'Strongly disagree'],
            [2, 'Disagree'],
            [3, 'Neither disagree nor agree'],
            [4, 'Agree'],
            [5, 'Strongly agree'],
        ],
    )
    inclusion = models.IntegerField(
        blank=False,
        choices=[
            [1, 'Strongly disagree'],
            [2, 'Disagree'],
            [3, 'Neither disagree nor agree'],
            [4, 'Agree'],
            [5, 'Strongly agree'],
        ],
    )
    own_team = models.IntegerField(
        blank=False,
        choices=[
            [1, 'Strongly disagree'],
            [2, 'Disagree'],
            [3, 'Neither disagree nor agree'],
            [4, 'Agree'],
            [5, 'Strongly agree'],
        ],
    )
    other_team = models.IntegerField(
        blank=False,
        choices=[
            [1, 'Strongly disagree'],
            [2, 'Disagree'],
            [3, 'Neither disagree nor agree'],
            [4, 'Agree'],
            [5, 'Strongly agree'],
        ],
    )
    fair = models.IntegerField(
        blank=False,
        choices=[
            [1, 'Strongly disagree'],
            [2, 'Disagree'],
            [3, 'Neither disagree nor agree'],
            [4, 'Agree'],
            [5, 'Strongly agree'],
        ],
    )
    fair_benef = models.IntegerField(
        blank=False,
        choices=[
            [1, 'Very unfair'],
            [2, 'Unfair'],
            [3, 'Neither unfair nor fair'],
            [4, 'Fair'],
            [5, 'Very fair'],
        ],
    )
    fair_benef_own = models.IntegerField(
        blank=False,
        choices=[
            [1, 'Very unfair'],
            [2, 'Unfair'],
            [3, 'Neither unfair nor fair'],
            [4, 'Fair'],
            [5, 'Very fair'],
        ],
    )
    fair_benef_other = models.IntegerField(
        blank=False,
        choices=[
            [1, 'Very unfair'],
            [2, 'Unfair'],
            [3, 'Neither unfair nor fair'],
            [4, 'Fair'],
            [5, 'Very fair'],
        ],
    )
    rejected = models.IntegerField(
        blank=False,
        choices=[
            [1, 'Always'],
            [2, 'Often'],
            [3, 'About half the time'],
            [4, 'Seldom'],
            [5, 'Never'],
        ],
    )
    happy = models.IntegerField(
        blank=False,
        choices=[
            [0, '0-Not happy  at all'],
            [1, '1-'],
            [2, '2-'],
            [3, '3-'],
            [4, '4-'],
            [5, '5-'],
            [6, '6-'],
            [7, '7-'],
            [8, '8-'],
            [9, '9-'],
            [10, '10-Extremely happy'],
        ],
    )
    well_being = models.IntegerField(
        blank=False,
        choices=[
            [0, '-5- Much lower than before'],
            [1, '-4'],
            [2, '-3'],
            [3, '-2'],
            [4, '-1'],
            [5, '0- No change'],
            [6, '1'],
            [7, '2'],
            [8, '3'],
            [9, '4'],
            [10, '+5- Much higher than before'],
        ],
    )
    ## Post-experiment questionnairre
    ####1st round
    # condition = models.StringField()
    colour = models.StringField()
    position = models.StringField()
    luck = models.IntegerField()
    initial = models.IntegerField()
    first_role = models.IntegerField()



####2nd round
# FUNCTIONS


def set_points(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p3 = group.get_player_by_id(3)
    p4 = group.get_player_by_id(4)
    p1.points = (
        (
            group.P1_1
            + group.P1_2
            + group.P1_3
            + group.P1_4
            + group.P1_5
            + group.P1_6
            + group.P1_7
            + group.P1_8
            + group.P1_9
            + group.P1_10
            + group.P1_11
            + group.P1_12
            + group.P1_13
            + group.P1_14
            + group.P1_15
            + group.P1_16
            + group.P1_17
            + group.P1_18
            + group.P1_19
        )
        / 20
    ) * 40
    p2.points = (
        (
            group.P2_1
            + group.P2_2
            + group.P2_3
            + group.P2_4
            + group.P2_5
            + group.P2_6
            + group.P2_7
            + group.P2_8
            + group.P2_9
            + group.P2_10
            + group.P2_11
            + group.P2_12
            + group.P2_13
            + group.P2_14
            + group.P2_15
            + group.P2_16
            + group.P2_17
            + group.P2_18
            + group.P2_19
        )
        / 20
    ) * 40
    p3.points = (
        (
            group.P3_1
            + group.P3_2
            + group.P3_3
            + group.P3_4
            + group.P3_5
            + group.P3_6
            + group.P3_7
            + group.P3_8
            + group.P3_9
            + group.P3_10
            + group.P3_11
            + group.P3_12
            + group.P3_13
            + group.P3_14
            + group.P3_15
            + group.P3_16
            + group.P3_17
            + group.P3_18
            + group.P3_19
        )
        / 20
    ) * 40
    p4.points = (
        (
            group.P4_1
            + group.P4_2
            + group.P4_3
            + group.P4_4
            + group.P4_5
            + group.P4_6
            + group.P4_7
            + group.P4_8
            + group.P4_9
            + group.P4_10
            + group.P4_11
            + group.P4_12
            + group.P4_13
            + group.P4_14
            + group.P4_15
            + group.P4_16
            + group.P4_17
            + group.P4_18
            + group.P4_19
        )
        / 20
    ) * 40


def set_payoff2(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p3 = group.get_player_by_id(3)
    p4 = group.get_player_by_id(4)
    p1.payoff2 = (
        (
            p1.P1_initial
            + group.P1_1
            + group.P1_2
            + group.P1_3
            + group.P1_4
            + group.P1_5
            + group.P1_6
            + group.P1_7
            + group.P1_8
            + group.P1_9
            + group.P1_10
            + group.P1_11
            + group.P1_12
            + group.P1_13
            + group.P1_14
            + group.P1_15
            + group.P1_16
            + group.P1_17
            + group.P1_18
            + group.P1_19
        )
        / 20
    ) * 4
    p2.payoff2 = (
        (
            p2.P2_initial
            + group.P2_1
            + group.P2_2
            + group.P2_3
            + group.P2_4
            + group.P2_5
            + group.P2_6
            + group.P2_7
            + group.P2_8
            + group.P2_9
            + group.P2_10
            + group.P2_11
            + group.P2_12
            + group.P2_13
            + group.P2_14
            + group.P2_15
            + group.P2_16
            + group.P2_17
            + group.P2_18
            + group.P2_19
        )
        / 20
    ) * 4
    p3.payoff2 = (
        (
            p3.P3_initial
            + group.P3_1
            + group.P3_2
            + group.P3_3
            + group.P3_4
            + group.P3_5
            + group.P3_6
            + group.P3_7
            + group.P3_8
            + group.P3_9
            + group.P3_10
            + group.P3_11
            + group.P3_12
            + group.P3_13
            + group.P3_14
            + group.P3_15
            + group.P3_16
            + group.P3_17
            + group.P3_18
            + group.P3_19
        )
        / 20
    ) * 4
    p4.payoff2 = (
        (
            p4.P4_initial
            + group.P4_1
            + group.P4_2
            + group.P4_3
            + group.P4_4
            + group.P4_5
            + group.P4_6
            + group.P4_7
            + group.P4_8
            + group.P4_9
            + group.P4_10
            + group.P4_11
            + group.P4_12
            + group.P4_13
            + group.P4_14
            + group.P4_15
            + group.P4_16
            + group.P4_17
            + group.P4_18
            + group.P4_19
        )
        / 20
    ) * 4


def get_partner(player: Player):
    return player.get_others_in_group()


# PAGES
class Wait_start(WaitPage):
    template_name = 'exclusion/Wait_start.html'
    group_by_arrival_time = True


class Wait_start_2(WaitPage):
    template_name = 'exclusion/Wait_start_2.html'

    def after_all_players_arrive(group):
        colours = itertools.cycle(['Green', 'Purple', 'Green', 'Purple'])
        players = group.get_players()
        for p in players:
            p.position = "Non-beneficiary"
            p.first_income = 0
            p.colour = next(colours)
        rich_player = random.choice(players)
        rich_player.position = "Beneficiary"
        rich_player.first_income = 1
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)
        p3 = group.get_player_by_id(3)
        p4 = group.get_player_by_id(4)
        if p1.position == 'Beneficiary':
                p1.first_benef = 1
                p2.first_benef = 1
                p3.first_benef = 1
                p4.first_benef = 1
                p1.P1_initial = 2
                p2.P1_initial = 2
                p3.P1_initial = 2
                p4.P1_initial = 2
                p1.P2_initial = 0
                p2.P2_initial = 0
                p3.P2_initial = 0
                p4.P2_initial = 0
                p1.P3_initial = 0
                p2.P3_initial = 0
                p3.P3_initial = 0
                p4.P3_initial = 0
                p1.P4_initial = 0
                p2.P4_initial = 0
                p3.P4_initial = 0
                p4.P4_initial = 0
        else:
            if p2.position == 'Beneficiary':
                    p1.first_benef = 2
                    p2.first_benef = 2
                    p3.first_benef = 2
                    p4.first_benef = 2
                    p1.P2_initial = 2
                    p2.P2_initial = 2
                    p3.P2_initial = 2
                    p4.P2_initial = 2
                    p1.P1_initial = 0
                    p2.P1_initial = 0
                    p3.P1_initial = 0
                    p4.P1_initial = 0
                    p1.P3_initial = 0
                    p2.P3_initial = 0
                    p3.P3_initial = 0
                    p4.P3_initial = 0
                    p1.P4_initial = 0
                    p2.P4_initial = 0
                    p3.P4_initial = 0
                    p4.P4_initial = 0
            else:
                if p3.position == 'Beneficiary':
                        p1.first_benef = 3
                        p2.first_benef = 3
                        p3.first_benef = 3
                        p4.first_benef = 3
                        p1.P3_initial = 2
                        p2.P3_initial = 2
                        p3.P3_initial = 2
                        p4.P3_initial = 2
                        p1.P1_initial = 0
                        p2.P1_initial = 0
                        p3.P1_initial = 0
                        p4.P1_initial = 0
                        p1.P4_initial = 0
                        p2.P4_initial = 0
                        p3.P4_initial = 0
                        p4.P4_initial = 0
                        p1.P2_initial = 0
                        p2.P2_initial = 0
                        p3.P2_initial = 0
                        p4.P2_initial = 0
                else:
                    if p4.position == 'Beneficiary':
                            p1.first_benef = 4
                            p2.first_benef = 4
                            p3.first_benef = 4
                            p4.first_benef = 4
                            p1.P4_initial = 2
                            p2.P4_initial = 2
                            p3.P4_initial = 2
                            p4.P4_initial = 2
                            p1.P2_initial = 0
                            p2.P2_initial = 0
                            p3.P2_initial = 0
                            p4.P2_initial = 0
                            p1.P1_initial = 0
                            p2.P1_initial = 0
                            p3.P1_initial = 0
                            p4.P1_initial = 0
                            p1.P3_initial = 0
                            p2.P3_initial = 0
                            p3.P3_initial = 0
                            p4.P3_initial = 0


class Introduction(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {'color': player.colour}


class history_0(Page):
    @staticmethod
    def vars_for_template(player: Player):
        my_partners = player.get_others_in_group()
        return dict(my_partners=my_partners, position=player.position)


class benef_start(Page):
    @staticmethod
    def vars_for_template(player: Player):
        my_partners = player.get_others_in_group()
        return {'id': player.id_in_group, 'my_partners': my_partners}

    @staticmethod
    def is_displayed(player: Player):
        return player.position == 'Beneficiary'

    form_model = 'group'
    form_fields = ['P1_1', 'P2_1', 'P3_1', 'P4_1', 'benef_2']


class wait_for_benef_1(WaitPage):
    template_name = 'exclusion/wait_for_benef_1.html'

    @staticmethod
    def vars_for_template(player: Player):
        my_partners = player.get_others_in_group()
        return {'my_partners': my_partners, 'benef_start': player.first_benef}


class Waiting(WaitPage):
    pass


class history_1(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'P1': player.group.P1_1 + (player.P1_initial / 2),
            'P2': player.group.P2_1 + (player.P2_initial / 2),
            'P3': player.group.P3_1 + (player.P3_initial / 2),
            'P4': player.group.P4_1 + (player.P4_initial / 2),
            'P1_p': player.P1_initial + ((player.group.P1_1 / 20) * 40),
            'P2_p': player.P2_initial + ((player.group.P2_1 / 20) * 40),
            'P3_p': player.P3_initial + ((player.group.P3_1 / 20) * 40),
            'P4_p': player.P4_initial + ((player.group.P4_1 / 20) * 40),
        }


class benef_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_2

    form_model = 'group'
    form_fields = ['P1_2', 'P2_2', 'P3_2', 'P4_2', 'benef_3']

    @staticmethod
    def vars_for_template(player: Player):
        my_partners = player.get_others_in_group()
        return dict(
            my_partners=my_partners, position=player.position, first_benef=player.first_benef
        )


class wait_for_benef_2(WaitPage):
    template_name = 'exclusion/wait_for_benef_2.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_2': player.group.benef_2,
            'P1': player.group.P1_1 + (player.P1_initial / 2),
            'P2': player.group.P2_1 + (player.P2_initial / 2),
            'P3': player.group.P3_1 + (player.P3_initial / 2),
            'P4': player.group.P4_1 + (player.P4_initial / 2),
            'P1_p': player.P1_initial + ((player.group.P1_1 / 20) * 40),
            'P2_p': player.P2_initial + ((player.group.P2_1 / 20) * 40),
            'P3_p': player.P3_initial + ((player.group.P3_1 / 20) * 40),
            'P4_p': player.P4_initial + ((player.group.P4_1 / 20) * 40),
        }


class history_2(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'P1': player.group.P1_1 + player.group.P1_2 + (player.P1_initial / 2),
            'P2': player.group.P2_1 + player.group.P2_2 + (player.P2_initial / 2),
            'P3': player.group.P3_1 + player.group.P3_2 + (player.P3_initial / 2),
            'P4': player.group.P4_1 + player.group.P4_2 + (player.P4_initial / 2),
            'P1_p': player.P1_initial + ((player.group.P1_1 + player.group.P1_2) / 20) * 40,
            'P2_p': player.P2_initial + ((player.group.P2_1 + player.group.P2_2) / 20) * 40,
            'P3_p': player.P3_initial + ((player.group.P3_1 + player.group.P3_2) / 20) * 40,
            'P4_p': player.P4_initial + ((player.group.P4_1 + player.group.P4_2) / 20) * 40,
        }


class benef_3(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_3

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_2,
            'P1': player.group.P1_1 + player.group.P1_2 + (player.P1_initial / 2),
            'P2': player.group.P2_1 + player.group.P2_2 + (player.P2_initial / 2),
            'P3': player.group.P3_1 + player.group.P3_2 + (player.P3_initial / 2),
            'P4': player.group.P4_1 + player.group.P4_2 + (player.P4_initial / 2),
            'P1_p': player.P1_initial + ((player.group.P1_1 + player.group.P1_2) / 20) * 40,
            'P2_p': player.P2_initial + ((player.group.P2_1 + player.group.P2_2) / 20) * 40,
            'P3_p': player.P3_initial + ((player.group.P3_1 + player.group.P3_2) / 20) * 40,
            'P4_p': player.P4_initial + ((player.group.P4_1 + player.group.P4_2) / 20) * 40,
        }

    form_model = 'group'
    form_fields = ['P1_3', 'P2_3', 'P3_3', 'P4_3', 'benef_4']


class wait_for_benef_3(WaitPage):
    template_name = 'exclusion/wait_for_benef_3.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_3': player.group.benef_3,
            'P1': player.group.P1_1 + player.group.P1_2 + (player.P1_initial / 2),
            'P2': player.group.P2_1 + player.group.P2_2 + (player.P2_initial / 2),
            'P3': player.group.P3_1 + player.group.P3_2 + (player.P3_initial / 2),
            'P4': player.group.P4_1 + player.group.P4_2 + (player.P4_initial / 2),
            'P1_p': player.P1_initial + ((player.group.P1_1 + player.group.P1_2) / 20) * 40,
            'P2_p': player.P2_initial + ((player.group.P2_1 + player.group.P2_2) / 20) * 40,
            'P3_p': player.P3_initial + ((player.group.P3_1 + player.group.P3_2) / 20) * 40,
            'P4_p': player.P4_initial + ((player.group.P4_1 + player.group.P4_2) / 20) * 40,
        }


class history_3(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'P1': player.group.P1_1 + player.group.P1_2 + player.group.P1_3,
            'P2': player.group.P2_1 + player.group.P2_2 + player.group.P2_3,
            'P3': player.group.P3_1 + player.group.P3_2 + player.group.P3_3,
            'P4': player.group.P4_1 + player.group.P4_2 + player.group.P4_3,
            'P1_p': ((player.group.P1_1 + player.group.P1_2 + player.group.P1_3) / 20) * 40,
            'P2_p': ((player.group.P2_1 + player.group.P2_2 + player.group.P2_3) / 20) * 40,
            'P3_p': ((player.group.P3_1 + player.group.P3_2 + player.group.P3_3) / 20) * 40,
            'P4_p': ((player.group.P4_1 + player.group.P4_2 + player.group.P4_3) / 20) * 40,
        }


class benef_4(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_4

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_3,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + ((player.group.P1_1 + player.group.P1_2 + player.group.P1_3) / 20) * 40,
            'P2_p': player.P2_initial
            + ((player.group.P2_1 + player.group.P2_2 + player.group.P2_3) / 20) * 40,
            'P3_p': player.P3_initial
            + ((player.group.P3_1 + player.group.P3_2 + player.group.P3_3) / 20) * 40,
            'P4_p': player.P4_initial
            + ((player.group.P4_1 + player.group.P4_2 + player.group.P4_3) / 20) * 40,
        }

    form_model = 'group'
    form_fields = ['P1_4', 'P2_4', 'P3_4', 'P4_4', 'benef_5']


class wait_for_benef_4(WaitPage):
    template_name = 'exclusion/wait_for_benef_4.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_4': player.group.benef_4,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + ((player.group.P1_1 + player.group.P1_2 + player.group.P1_3) / 20) * 40,
            'P2_p': player.P2_initial
            + ((player.group.P2_1 + player.group.P2_2 + player.group.P2_3) / 20) * 40,
            'P3_p': player.P3_initial
            + ((player.group.P3_1 + player.group.P3_2 + player.group.P3_3) / 20) * 40,
            'P4_p': player.P4_initial
            + ((player.group.P4_1 + player.group.P4_2 + player.group.P4_3) / 20) * 40,
        }


class benef_5(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_5

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_4,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + ((player.group.P1_1 + player.group.P1_2 + player.group.P1_3 + player.group.P1_4) / 20)
            * 40,
            'P2_p': player.P2_initial
            + ((player.group.P2_1 + player.group.P2_2 + player.group.P2_3 + player.group.P2_4) / 20)
            * 40,
            'P3_p': player.P3_initial
            + ((player.group.P3_1 + player.group.P3_2 + player.group.P3_3 + player.group.P3_4) / 20)
            * 40,
            'P4_p': player.P4_initial
            + ((player.group.P4_1 + player.group.P4_2 + player.group.P4_3 + player.group.P4_4) / 20)
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_5', 'P2_5', 'P3_5', 'P4_5', 'benef_6']


class wait_for_benef_5(WaitPage):
    template_name = 'exclusion/wait_for_benef_5.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_5': player.group.benef_5,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + ((player.group.P1_1 + player.group.P1_2 + player.group.P1_3 + player.group.P1_4) / 20)
            * 40,
            'P2_p': player.P2_initial
            + ((player.group.P2_1 + player.group.P2_2 + player.group.P2_3 + player.group.P2_4) / 20)
            * 40,
            'P3_p': player.P3_initial
            + ((player.group.P3_1 + player.group.P3_2 + player.group.P3_3 + player.group.P3_4) / 20)
            * 40,
            'P4_p': player.P4_initial
            + ((player.group.P4_1 + player.group.P4_2 + player.group.P4_3 + player.group.P4_4) / 20)
            * 40,
        }


class benef_6(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_6

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_5,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                )
                / 20
            )
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_6', 'P2_6', 'P3_6', 'P4_6', 'benef_7']


class wait_for_benef_6(WaitPage):
    template_name = 'exclusion/wait_for_benef_6.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_6': player.group.benef_6,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                )
                / 20
            )
            * 40,
        }


class benef_7(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_7

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_6,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                )
                / 20
            )
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_7', 'P2_7', 'P3_7', 'P4_7', 'benef_8']


class wait_for_benef_7(WaitPage):
    template_name = 'exclusion/wait_for_benef_7.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_7': player.group.benef_7,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                )
                / 20
            )
            * 40,
        }


class benef_8(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_8

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_7,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                )
                / 20
            )
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_8', 'P2_8', 'P3_8', 'P4_8', 'benef_9']


class wait_for_benef_8(WaitPage):
    template_name = 'exclusion/wait_for_benef_8.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_8': player.group.benef_8,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                )
                / 20
            )
            * 40,
        }


class benef_9(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_9

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_8,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                )
                / 20
            )
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_9', 'P2_9', 'P3_9', 'P4_9', 'benef_10']


class wait_for_benef_9(WaitPage):
    template_name = 'exclusion/wait_for_benef_9.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_9': player.group.benef_9,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                )
                / 20
            )
            * 40,
        }


class benef_10(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_10

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_9,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                )
                / 20
            )
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_10', 'P2_10', 'P3_10', 'P4_10', 'benef_11']


class wait_for_benef_10(WaitPage):
    template_name = 'exclusion/wait_for_benef_10.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_10': player.group.benef_10,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                )
                / 20
            )
            * 40,
        }


class benef_11(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_11

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_10,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                )
                / 20
            )
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_11', 'P2_11', 'P3_11', 'P4_11', 'benef_12']


class wait_for_benef_11(WaitPage):
    template_name = 'exclusion/wait_for_benef_11.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_11': player.group.benef_11,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                )
                / 20
            )
            * 40,
        }


class benef_12(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_12

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_11,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                )
                / 20
            )
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_12', 'P2_12', 'P3_12', 'P4_12', 'benef_13']


class wait_for_benef_12(WaitPage):
    template_name = 'exclusion/wait_for_benef_12.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_12': player.group.benef_12,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                )
                / 20
            )
            * 40,
        }


class benef_13(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_13

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_12,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                )
                / 20
            )
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_13', 'P2_13', 'P3_13', 'P4_13', 'benef_14']


class wait_for_benef_13(WaitPage):
    template_name = 'exclusion/wait_for_benef_13.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_13': player.group.benef_13,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                )
                / 20
            )
            * 40,
        }


class benef_14(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_14

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_13,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + player.group.P1_13
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + player.group.P2_13
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + player.group.P3_13
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + player.group.P4_13
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                )
                / 20
            )
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_14', 'P2_14', 'P3_14', 'P4_14', 'benef_15']


class wait_for_benef_14(WaitPage):
    template_name = 'exclusion/wait_for_benef_14.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_14': player.group.benef_14,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + player.group.P1_13
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + player.group.P2_13
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + player.group.P3_13
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + player.group.P4_13
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                )
                / 20
            )
            * 40,
        }


class benef_15(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_15

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_14,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + player.group.P1_13
            + player.group.P1_14
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + player.group.P2_13
            + player.group.P2_14
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + player.group.P3_13
            + player.group.P3_14
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + player.group.P4_13
            + player.group.P4_14
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                    + player.group.P1_14
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                    + player.group.P2_14
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                    + player.group.P3_14
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                    + player.group.P4_14
                )
                / 20
            )
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_15', 'P2_15', 'P3_15', 'P4_15', 'benef_16']


class wait_for_benef_15(WaitPage):
    template_name = 'exclusion/wait_for_benef_15.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_15': player.group.benef_15,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + player.group.P1_13
            + player.group.P1_14
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + player.group.P2_13
            + player.group.P2_14
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + player.group.P3_13
            + player.group.P3_14
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + player.group.P4_13
            + player.group.P4_14
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                    + player.group.P1_14
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                    + player.group.P2_14
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                    + player.group.P3_14
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                    + player.group.P4_14
                )
                / 20
            )
            * 40,
        }


class benef_16(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_16

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_15,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + player.group.P1_13
            + player.group.P1_14
            + player.group.P1_15
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + player.group.P2_13
            + player.group.P2_14
            + player.group.P2_15
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + player.group.P3_13
            + player.group.P3_14
            + player.group.P3_15
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + player.group.P4_13
            + player.group.P4_14
            + player.group.P4_15
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                    + player.group.P1_14
                    + player.group.P1_15
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                    + player.group.P2_14
                    + player.group.P2_15
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                    + player.group.P3_14
                    + player.group.P3_15
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                    + player.group.P4_14
                    + player.group.P4_15
                )
                / 20
            )
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_16', 'P2_16', 'P3_16', 'P4_16', 'benef_17']


class wait_for_benef_16(WaitPage):
    template_name = 'exclusion/wait_for_benef_16.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_16': player.group.benef_16,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + player.group.P1_13
            + player.group.P1_14
            + player.group.P1_15
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + player.group.P2_13
            + player.group.P2_14
            + player.group.P2_15
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + player.group.P3_13
            + player.group.P3_14
            + player.group.P3_15
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + player.group.P4_13
            + player.group.P4_14
            + player.group.P4_15
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                    + player.group.P1_14
                    + player.group.P1_15
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                    + player.group.P2_14
                    + player.group.P2_15
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                    + player.group.P3_14
                    + player.group.P3_15
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                    + player.group.P4_14
                    + player.group.P4_15
                )
                / 20
            )
            * 40,
        }


class benef_17(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_17

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_16,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + player.group.P1_13
            + player.group.P1_14
            + player.group.P1_15
            + player.group.P1_16
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + player.group.P2_13
            + player.group.P2_14
            + player.group.P2_15
            + player.group.P2_16
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + player.group.P3_13
            + player.group.P3_14
            + player.group.P3_15
            + player.group.P3_16
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + player.group.P4_13
            + player.group.P4_14
            + player.group.P4_15
            + player.group.P4_16
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                    + player.group.P1_14
                    + player.group.P1_15
                    + player.group.P1_16
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                    + player.group.P2_14
                    + player.group.P2_15
                    + player.group.P2_16
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                    + player.group.P3_14
                    + player.group.P3_15
                    + player.group.P3_16
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                    + player.group.P4_14
                    + player.group.P4_15
                    + player.group.P4_16
                )
                / 20
            )
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_17', 'P2_17', 'P3_17', 'P4_17', 'benef_18']


class wait_for_benef_17(WaitPage):
    template_name = 'exclusion/wait_for_benef_17.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_17': player.group.benef_17,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + player.group.P1_13
            + player.group.P1_14
            + player.group.P1_15
            + player.group.P1_16
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + player.group.P2_13
            + player.group.P2_14
            + player.group.P2_15
            + player.group.P2_16
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + player.group.P3_13
            + player.group.P3_14
            + player.group.P3_15
            + player.group.P3_16
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + player.group.P4_13
            + player.group.P4_14
            + player.group.P4_15
            + player.group.P4_16
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                    + player.group.P1_14
                    + player.group.P1_15
                    + player.group.P1_16
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                    + player.group.P2_14
                    + player.group.P2_15
                    + player.group.P2_16
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                    + player.group.P3_14
                    + player.group.P3_15
                    + player.group.P3_16
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                    + player.group.P4_14
                    + player.group.P4_15
                    + player.group.P4_16
                )
                / 20
            )
            * 40,
        }


class benef_18(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_18

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_17,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + player.group.P1_13
            + player.group.P1_14
            + player.group.P1_15
            + player.group.P1_16
            + player.group.P1_17
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + player.group.P2_13
            + player.group.P2_14
            + player.group.P2_15
            + player.group.P2_16
            + player.group.P2_17
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + player.group.P3_13
            + player.group.P3_14
            + player.group.P3_15
            + player.group.P3_16
            + player.group.P3_17
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + player.group.P4_13
            + player.group.P4_14
            + player.group.P4_15
            + player.group.P4_16
            + player.group.P4_17
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                    + player.group.P1_14
                    + player.group.P1_15
                    + player.group.P1_16
                    + player.group.P1_17
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                    + player.group.P2_14
                    + player.group.P2_15
                    + player.group.P2_16
                    + player.group.P2_17
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                    + player.group.P3_14
                    + player.group.P3_15
                    + player.group.P3_16
                    + player.group.P3_17
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                    + player.group.P4_14
                    + player.group.P4_15
                    + player.group.P4_16
                    + player.group.P4_17
                )
                / 20
            )
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_18', 'P2_18', 'P3_18', 'P4_18', 'benef_19']


class wait_for_benef_18(WaitPage):
    template_name = 'exclusion/wait_for_benef_18.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_18': player.group.benef_18,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + player.group.P1_13
            + player.group.P1_14
            + player.group.P1_15
            + player.group.P1_16
            + player.group.P1_17
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + player.group.P2_13
            + player.group.P2_14
            + player.group.P2_15
            + player.group.P2_16
            + player.group.P2_17
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + player.group.P3_13
            + player.group.P3_14
            + player.group.P3_15
            + player.group.P3_16
            + player.group.P3_17
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + player.group.P4_13
            + player.group.P4_14
            + player.group.P4_15
            + player.group.P4_16
            + player.group.P4_17
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                    + player.group.P1_14
                    + player.group.P1_15
                    + player.group.P1_16
                    + player.group.P1_17
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                    + player.group.P2_14
                    + player.group.P2_15
                    + player.group.P2_16
                    + player.group.P2_17
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                    + player.group.P3_14
                    + player.group.P3_15
                    + player.group.P3_16
                    + player.group.P3_17
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                    + player.group.P4_14
                    + player.group.P4_15
                    + player.group.P4_16
                    + player.group.P4_17
                )
                / 20
            )
            * 40,
        }


class benef_19(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_19

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_18,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + player.group.P1_13
            + player.group.P1_14
            + player.group.P1_15
            + player.group.P1_16
            + player.group.P1_17
            + player.group.P1_18
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + player.group.P2_13
            + player.group.P2_14
            + player.group.P2_15
            + player.group.P2_16
            + player.group.P2_17
            + player.group.P2_18
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + player.group.P3_13
            + player.group.P3_14
            + player.group.P3_15
            + player.group.P3_16
            + player.group.P3_17
            + player.group.P3_18
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + player.group.P4_13
            + player.group.P4_14
            + player.group.P4_15
            + player.group.P4_16
            + player.group.P4_17
            + player.group.P4_18
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                    + player.group.P1_14
                    + player.group.P1_15
                    + player.group.P1_16
                    + player.group.P1_17
                    + player.group.P1_18
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                    + player.group.P2_14
                    + player.group.P2_15
                    + player.group.P2_16
                    + player.group.P2_17
                    + player.group.P2_18
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                    + player.group.P3_14
                    + player.group.P3_15
                    + player.group.P3_16
                    + player.group.P3_17
                    + player.group.P3_18
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                    + player.group.P4_14
                    + player.group.P4_15
                    + player.group.P4_16
                    + player.group.P4_17
                    + player.group.P4_18
                )
                / 20
            )
            * 40,
        }

    form_model = 'group'
    form_fields = ['P1_19', 'P2_19', 'P3_19', 'P4_19', 'benef_20']


class wait_for_benef_19(WaitPage):
    template_name = 'exclusion/wait_for_benef_19.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_19': player.group.benef_19,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + player.group.P1_13
            + player.group.P1_14
            + player.group.P1_15
            + player.group.P1_16
            + player.group.P1_17
            + player.group.P1_18
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + player.group.P2_13
            + player.group.P2_14
            + player.group.P2_15
            + player.group.P2_16
            + player.group.P2_17
            + player.group.P2_18
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + player.group.P3_13
            + player.group.P3_14
            + player.group.P3_15
            + player.group.P3_16
            + player.group.P3_17
            + player.group.P3_18
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + player.group.P4_13
            + player.group.P4_14
            + player.group.P4_15
            + player.group.P4_16
            + player.group.P4_17
            + player.group.P4_18
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                    + player.group.P1_14
                    + player.group.P1_15
                    + player.group.P1_16
                    + player.group.P1_17
                    + player.group.P1_18
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                    + player.group.P2_14
                    + player.group.P2_15
                    + player.group.P2_16
                    + player.group.P2_17
                    + player.group.P2_18
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                    + player.group.P3_14
                    + player.group.P3_15
                    + player.group.P3_16
                    + player.group.P3_17
                    + player.group.P3_18
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                    + player.group.P4_14
                    + player.group.P4_15
                    + player.group.P4_16
                    + player.group.P4_17
                    + player.group.P4_18
                )
                / 20
            )
            * 40,
        }


class benef_20(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == player.group.benef_20

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.group.benef_19,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + player.group.P1_13
            + player.group.P1_14
            + player.group.P1_15
            + player.group.P1_16
            + player.group.P1_17
            + player.group.P1_18
            + player.group.P1_19
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + player.group.P2_13
            + player.group.P2_14
            + player.group.P2_15
            + player.group.P2_16
            + player.group.P2_17
            + player.group.P2_18
            + player.group.P2_19
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + player.group.P3_13
            + player.group.P3_14
            + player.group.P3_15
            + player.group.P3_16
            + player.group.P3_17
            + player.group.P3_18
            + player.group.P3_19
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + player.group.P4_13
            + player.group.P4_14
            + player.group.P4_15
            + player.group.P4_16
            + player.group.P4_17
            + player.group.P4_18
            + player.group.P4_19
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                    + player.group.P1_14
                    + player.group.P1_15
                    + player.group.P1_16
                    + player.group.P1_17
                    + player.group.P1_18
                    + player.group.P1_19
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                    + player.group.P2_14
                    + player.group.P2_15
                    + player.group.P2_16
                    + player.group.P2_17
                    + player.group.P2_18
                    + player.group.P2_19
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                    + player.group.P3_14
                    + player.group.P3_15
                    + player.group.P3_16
                    + player.group.P3_17
                    + player.group.P3_18
                    + player.group.P3_19
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                    + player.group.P4_14
                    + player.group.P4_15
                    + player.group.P4_16
                    + player.group.P4_17
                    + player.group.P4_18
                    + player.group.P4_19
                )
                / 20
            )
            * 40,
        }


class wait_for_benef_20(WaitPage):
    template_name = 'exclusion/wait_for_benef_20.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_20': player.group.benef_20,
            'P1': player.group.P1_1
            + player.group.P1_2
            + player.group.P1_3
            + player.group.P1_4
            + player.group.P1_5
            + player.group.P1_6
            + player.group.P1_7
            + player.group.P1_8
            + player.group.P1_9
            + player.group.P1_10
            + player.group.P1_11
            + player.group.P1_12
            + player.group.P1_13
            + player.group.P1_14
            + player.group.P1_15
            + player.group.P1_16
            + player.group.P1_17
            + player.group.P1_18
            + player.group.P1_19
            + (player.P1_initial / 2),
            'P2': player.group.P2_1
            + player.group.P2_2
            + player.group.P2_3
            + player.group.P2_4
            + player.group.P2_5
            + player.group.P2_6
            + player.group.P2_7
            + player.group.P2_8
            + player.group.P2_9
            + player.group.P2_10
            + player.group.P2_11
            + player.group.P2_12
            + player.group.P2_13
            + player.group.P2_14
            + player.group.P2_15
            + player.group.P2_16
            + player.group.P2_17
            + player.group.P2_18
            + player.group.P2_19
            + (player.P2_initial / 2),
            'P3': player.group.P3_1
            + player.group.P3_2
            + player.group.P3_3
            + player.group.P3_4
            + player.group.P3_5
            + player.group.P3_6
            + player.group.P3_7
            + player.group.P3_8
            + player.group.P3_9
            + player.group.P3_10
            + player.group.P3_11
            + player.group.P3_12
            + player.group.P3_13
            + player.group.P3_14
            + player.group.P3_15
            + player.group.P3_16
            + player.group.P3_17
            + player.group.P3_18
            + player.group.P3_19
            + (player.P3_initial / 2),
            'P4': player.group.P4_1
            + player.group.P4_2
            + player.group.P4_3
            + player.group.P4_4
            + player.group.P4_5
            + player.group.P4_6
            + player.group.P4_7
            + player.group.P4_8
            + player.group.P4_9
            + player.group.P4_10
            + player.group.P4_11
            + player.group.P4_12
            + player.group.P4_13
            + player.group.P4_14
            + player.group.P4_15
            + player.group.P4_16
            + player.group.P4_17
            + player.group.P4_18
            + player.group.P4_19
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                    + player.group.P1_14
                    + player.group.P1_15
                    + player.group.P1_16
                    + player.group.P1_17
                    + player.group.P1_18
                    + player.group.P1_19
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                    + player.group.P2_14
                    + player.group.P2_15
                    + player.group.P2_16
                    + player.group.P2_17
                    + player.group.P2_18
                    + player.group.P2_19
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                    + player.group.P3_14
                    + player.group.P3_15
                    + player.group.P3_16
                    + player.group.P3_17
                    + player.group.P3_18
                    + player.group.P3_19
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                    + player.group.P4_14
                    + player.group.P4_15
                    + player.group.P4_16
                    + player.group.P4_17
                    + player.group.P4_18
                    + player.group.P4_19
                )
                / 20
            )
            * 40,
        }


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoff2'
    after_all_players_arrive = 'set_points'


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        first = player.first_income
        return {
            'points': cu(player.points + first),
            'payoff': player.points+first,
            'P1_p': player.P1_initial
            + (
                (
                    player.group.P1_1
                    + player.group.P1_2
                    + player.group.P1_3
                    + player.group.P1_4
                    + player.group.P1_5
                    + player.group.P1_6
                    + player.group.P1_7
                    + player.group.P1_8
                    + player.group.P1_9
                    + player.group.P1_10
                    + player.group.P1_11
                    + player.group.P1_12
                    + player.group.P1_13
                    + player.group.P1_14
                    + player.group.P1_15
                    + player.group.P1_16
                    + player.group.P1_17
                    + player.group.P1_18
                    + player.group.P1_19
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.group.P2_1
                    + player.group.P2_2
                    + player.group.P2_3
                    + player.group.P2_4
                    + player.group.P2_5
                    + player.group.P2_6
                    + player.group.P2_7
                    + player.group.P2_8
                    + player.group.P2_9
                    + player.group.P2_10
                    + player.group.P2_11
                    + player.group.P2_12
                    + player.group.P2_13
                    + player.group.P2_14
                    + player.group.P2_15
                    + player.group.P2_16
                    + player.group.P2_17
                    + player.group.P2_18
                    + player.group.P2_19
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.group.P3_1
                    + player.group.P3_2
                    + player.group.P3_3
                    + player.group.P3_4
                    + player.group.P3_5
                    + player.group.P3_6
                    + player.group.P3_7
                    + player.group.P3_8
                    + player.group.P3_9
                    + player.group.P3_10
                    + player.group.P3_11
                    + player.group.P3_12
                    + player.group.P3_13
                    + player.group.P3_14
                    + player.group.P3_15
                    + player.group.P3_16
                    + player.group.P3_17
                    + player.group.P3_18
                    + player.group.P3_19
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.group.P4_1
                    + player.group.P4_2
                    + player.group.P4_3
                    + player.group.P4_4
                    + player.group.P4_5
                    + player.group.P4_6
                    + player.group.P4_7
                    + player.group.P4_8
                    + player.group.P4_9
                    + player.group.P4_10
                    + player.group.P4_11
                    + player.group.P4_12
                    + player.group.P4_13
                    + player.group.P4_14
                    + player.group.P4_15
                    + player.group.P4_16
                    + player.group.P4_17
                    + player.group.P4_18
                    + player.group.P4_19
                )
                / 20
            )
            * 40,
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.points = player.points
        participant.first_income = player.first_income


class survey(Page):
    form_model = 'player'
    form_fields = [
        'exclusion',
        'inclusion',
        'fair',
        'fair_benef',
        'fair_benef_other',
        'fair_benef_own',
        'rejected',
        'happy',
        'well_being',
    ]


    # def app_after_this_page(self, upcoming_apps):
    #   return "dictator"


page_sequence = [
    Wait_start,
    Wait_start_2,
    Introduction,
    benef_start,
    wait_for_benef_1,
    benef_2,
    wait_for_benef_2,
    benef_3,
    wait_for_benef_3,
    benef_4,
    wait_for_benef_4,
    benef_5,
    wait_for_benef_5,
    benef_6,
    wait_for_benef_6,
    benef_7,
    wait_for_benef_7,
    benef_8,
    wait_for_benef_8,
    benef_9,
    wait_for_benef_9,
    benef_10,
    wait_for_benef_10,
    benef_11,
    wait_for_benef_11,
    benef_12,
    wait_for_benef_12,
    benef_13,
    wait_for_benef_13,
    benef_14,
    wait_for_benef_14,
    benef_15,
    wait_for_benef_15,
    benef_16,
    wait_for_benef_16,
    benef_17,
    wait_for_benef_17,
    benef_18,
    wait_for_benef_18,
    benef_19,
    wait_for_benef_19,
    benef_20,
    wait_for_benef_20,
    ResultsWaitPage,
    Results,
    survey,
]
