import itertools
import json
import random

from otree.api import *


author = 'ceren ay'
doc = """
In this app players play in groups of 4 to split a total amount of 40
"""


class Constants(BaseConstants):
    name_in_url = 'STAGE_2'
    players_per_group = None
    num_rounds = 1
    group_endowment = 40


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


##20th round
class Player(BasePlayer):
##from csv
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

    points = models.IntegerField()
    payoff2 = models.IntegerField()
    first_benef = models.IntegerField()
    P1_initial = models.IntegerField()
    P2_initial = models.IntegerField()
    P3_initial = models.IntegerField()
    P4_initial = models.IntegerField()
    first_income = models.IntegerField()
    position = models.StringField()
    number = models.IntegerField()
    id_group = models.IntegerField()






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
    initial = models.IntegerField()
    first_role = models.IntegerField()



####2nd round
# FUNCTIONS

def creating_session(subsession: Subsession):
    import csv
    f = open('exclusion_control/control_variables.csv', encoding='utf-8-sig')
    rows = list(csv.DictReader(f))
    players = subsession.get_players()
    for i in range(len(players)):
        row = rows[i]
        player = players[i]
        # CSV contains all data in string form, so we need to convert
        # to the correct data type, e.g. '1' -> 1 -> True.
        player.number = int(row['number'])
        player.points = int(row['points'])
        player.first_benef = int(row['first_benef'])
        player.position = row['position']
        player.colour = row ['colour']
        player.P1_initial = int(row['P1_initial'])
        player.P2_initial = int(row['P2_initial'])
        player.P3_initial = int(row['P3_initial'])
        player.P4_initial = int(row['P4_initial'])
        player.first_income = int(row['first_income'])
        player.id_group = int(row['id_group'])
        player.P1_1 = int(row['P1_1'])
        player.P2_1 = int(row['P2_1'])
        player.P3_1 = int(row['P3_1'])
        player.P4_1 = int(row['P4_1'])
        player.benef_2 = int(row['benef_2'])
        player.P1_2 = int(row['P1_2'])
        player.P2_2 = int(row['P2_2'])
        player.P3_2 = int(row['P3_2'])
        player.P4_2 = int(row['P4_2'])
        player.benef_3 = int(row['benef_3'])
        player.P1_3 = int(row['P1_3'])
        player.P2_3 = int(row['P2_3'])
        player.P3_3 = int(row['P3_3'])
        player.P4_3 = int(row['P4_3'])
        player.benef_4 = int(row['benef_4'])
        player.P1_4 = int(row['P1_4'])
        player.P2_4 = int(row['P2_4'])
        player.P3_4 = int(row['P3_4'])
        player.P4_4 = int(row['P4_4'])
        player.benef_5 = int(row['benef_5'])
        player.P1_5 = int(row['P1_5'])
        player.P2_5 = int(row['P2_5'])
        player.P3_5 = int(row['P3_5'])
        player.P4_5 = int(row['P4_5'])
        player.benef_6 = int(row['benef_6'])
        player.P1_6 = int(row['P1_6'])
        player.P2_6 = int(row['P2_6'])
        player.P3_6 = int(row['P3_6'])
        player.P4_6 = int(row['P4_6'])
        player.benef_7 = int(row['benef_7'])
        player.P1_7 = int(row['P1_7'])
        player.P2_7 = int(row['P2_7'])
        player.P3_7 = int(row['P3_7'])
        player.P4_7 = int(row['P4_7'])
        player.benef_8 = int(row['benef_8'])
        player.P1_8 = int(row['P1_8'])
        player.P2_8 = int(row['P2_8'])
        player.P3_8 = int(row['P3_8'])
        player.P4_8 = int(row['P4_8'])
        player.benef_9 = int(row['benef_9'])
        player.P1_9 = int(row['P1_9'])
        player.P2_9 = int(row['P2_9'])
        player.P3_9 = int(row['P3_9'])
        player.P4_9 = int(row['P4_9'])
        player.benef_10 = int(row['benef_10'])
        player.P1_10 = int(row['P1_10'])
        player.P2_10 = int(row['P2_10'])
        player.P3_10 = int(row['P3_10'])
        player.P4_10 = int(row['P4_10'])
        player.benef_11 = int(row['benef_11'])
        player.P1_11 = int(row['P1_11'])
        player.P2_11 = int(row['P2_11'])
        player.P3_11 = int(row['P3_11'])
        player.P4_11 = int(row['P4_11'])
        player.benef_12 = int(row['benef_12'])
        player.P1_12 = int(row['P1_12'])
        player.P2_12 = int(row['P2_12'])
        player.P3_12 = int(row['P3_12'])
        player.P4_12 = int(row['P4_12'])
        player.benef_13 = int(row['benef_13'])
        player.P1_13 = int(row['P1_13'])
        player.P2_13 = int(row['P2_13'])
        player.P3_13 = int(row['P3_13'])
        player.P4_13 = int(row['P4_13'])
        player.benef_14 = int(row['benef_14'])
        player.P1_14 = int(row['P1_14'])
        player.P2_14 = int(row['P2_14'])
        player.P3_14 = int(row['P3_14'])
        player.P4_14 = int(row['P4_14'])
        player.benef_15 = int(row['benef_15'])
        player.P1_15 = int(row['P1_15'])
        player.P2_15 = int(row['P2_15'])
        player.P3_15 = int(row['P3_15'])
        player.P4_15 = int(row['P4_15'])
        player.benef_16 = int(row['benef_16'])
        player.P1_16 = int(row['P1_16'])
        player.P2_16 = int(row['P2_16'])
        player.P3_16 = int(row['P3_16'])
        player.P4_16 = int(row['P4_16'])
        player.benef_17 = int(row['benef_17'])
        player.P1_17 = int(row['P1_17'])
        player.P2_17 = int(row['P2_17'])
        player.P3_17 = int(row['P3_17'])
        player.P4_17 = int(row['P4_17'])
        player.benef_18 = int(row['benef_18'])
        player.P1_18 = int(row['P1_18'])
        player.P2_18 = int(row['P2_18'])
        player.P3_18 = int(row['P3_18'])
        player.P4_18 = int(row['P4_18'])
        player.benef_19 = int(row['benef_19'])
        player.P1_19 = int(row['P1_19'])
        player.P2_19 = int(row['P2_19'])
        player.P3_19 = int(row['P3_19'])
        player.P4_19 = int(row['P4_19'])
        player.benef_20 = int(row['benef_20'])




def get_partner(player: Player):
    return player.get_others_in_group()


# PAGES
class Wait_start(Page):
    template_name = 'exclusion_control/Wait_start.html'
    group_by_arrival_time = True


class Wait_start_2(Page):
    template_name = 'exclusion_control/Wait_start_2.html'


class Introduction(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {'color': player.colour}



class benef_start(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'P1': player.P1_initial / 2,
            'P2': player.P2_initial / 2,
            'P3': player.P3_initial / 2,
            'P4': player.P4_initial / 2,
            'P1_p': (player.P1_initial / 40) * 40,
            'P2_p': (player.P2_initial / 40) * 40,
            'P3_p': (player.P3_initial / 40) * 40,
            'P4_p': (player.P4_initial / 40) * 40,
        }
    @staticmethod
    def is_displayed(player: Player):
        return player.position == 'Beneficiary'


class wait_for_benef_1(Page):
    template_name = 'exclusion_control/wait_for_benef_1.html'


    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_start': player.first_benef,
            'P1': player.P1_initial / 2,
            'P2': player.P2_initial / 2,
            'P3': player.P3_initial / 2,
            'P4': player.P4_initial / 2,
            'P1_p': (player.P1_initial /40) * 40,
            'P2_p': (player.P2_initial / 40) * 40,
            'P3_p': (player.P3_initial  / 40) * 40,
            'P4_p': (player.P4_initial / 40) * 40,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.position != 'Beneficiary'


class benef_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_2

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_2': player.benef_2,
            'P1': player.P1_1 + (player.P1_initial / 2),
            'P2': player.P2_1 + (player.P2_initial / 2),
            'P3': player.P3_1 + (player.P3_initial / 2),
            'P4': player.P4_1 + (player.P4_initial / 2),
            'P1_p': player.P1_initial + ((player.P1_1 / 20) * 40),
            'P2_p': player.P2_initial + ((player.P2_1 / 20) * 40),
            'P3_p': player.P3_initial + ((player.P3_1 / 20) * 40),
            'P4_p': player.P4_initial + ((player.P4_1 / 20) * 40),
        }


class wait_for_benef_3_2(Page):
    template_name = 'exclusion_control/wait_for_benef_3_2.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_2': player.benef_2,
            'P1': player.P1_1 + (player.P1_initial / 2),
            'P2': player.P2_1 + (player.P2_initial / 2),
            'P3': player.P3_1 + (player.P3_initial / 2),
            'P4': player.P4_1 + (player.P4_initial / 2),
            'P1_p': player.P1_initial + ((player.P1_1 / 20) * 40),
            'P2_p': player.P2_initial + ((player.P2_1 / 20) * 40),
            'P3_p': player.P3_initial + ((player.P3_1 / 20) * 40),
            'P4_p': player.P4_initial + ((player.P4_1 / 20) * 40),
        }
    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_2




class benef_3(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_3

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_2,
            'P1': player.P1_1 + player.P1_2 + (player.P1_initial / 2),
            'P2': player.P2_1 + player.P2_2 + (player.P2_initial / 2),
            'P3': player.P3_1 + player.P3_2 + (player.P3_initial / 2),
            'P4': player.P4_1 + player.P4_2 + (player.P4_initial / 2),
            'P1_p': player.P1_initial + ((player.P1_1 + player.P1_2) / 20) * 40,
            'P2_p': player.P2_initial + ((player.P2_1 + player.P2_2) / 20) * 40,
            'P3_p': player.P3_initial + ((player.P3_1 + player.P3_2) / 20) * 40,
            'P4_p': player.P4_initial + ((player.P4_1 + player.P4_2) / 20) * 40,
        }


class wait_for_benef_3(Page):
    template_name = 'exclusion_control/wait_for_benef_3.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_3': player.benef_3,
            'P1': player.P1_1 + player.P1_2 + (player.P1_initial / 2),
            'P2': player.P2_1 + player.P2_2 + (player.P2_initial / 2),
            'P3': player.P3_1 + player.P3_2 + (player.P3_initial / 2),
            'P4': player.P4_1 + player.P4_2 + (player.P4_initial / 2),
            'P1_p': player.P1_initial + ((player.P1_1 + player.P1_2) / 20) * 40,
            'P2_p': player.P2_initial + ((player.P2_1 + player.P2_2) / 20) * 40,
            'P3_p': player.P3_initial + ((player.P3_1 + player.P3_2) / 20) * 40,
            'P4_p': player.P4_initial + ((player.P4_1 + player.P4_2) / 20) * 40,
        }
    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_3


class benef_4(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_4

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_3,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + ((player.P1_1 + player.P1_2 + player.P1_3) / 20) * 40,
            'P2_p': player.P2_initial
            + ((player.P2_1 + player.P2_2 + player.P2_3) / 20) * 40,
            'P3_p': player.P3_initial
            + ((player.P3_1 + player.P3_2 + player.P3_3) / 20) * 40,
            'P4_p': player.P4_initial
            + ((player.P4_1 + player.P4_2 + player.P4_3) / 20) * 40,
        }



class wait_for_benef_4(Page):
    template_name = 'exclusion_control/wait_for_benef_4.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_4': player.benef_4,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + ((player.P1_1 + player.P1_2 + player.P1_3) / 20) * 40,
            'P2_p': player.P2_initial
            + ((player.P2_1 + player.P2_2 + player.P2_3) / 20) * 40,
            'P3_p': player.P3_initial
            + ((player.P3_1 + player.P3_2 + player.P3_3) / 20) * 40,
            'P4_p': player.P4_initial
            + ((player.P4_1 + player.P4_2 + player.P4_3) / 20) * 40,
        }
    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_4


class benef_5(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_5

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_4,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + ((player.P1_1 + player.P1_2 + player.P1_3 + player.P1_4) / 20)
            * 40,
            'P2_p': player.P2_initial
            + ((player.P2_1 + player.P2_2 + player.P2_3 + player.P2_4) / 20)
            * 40,
            'P3_p': player.P3_initial
            + ((player.P3_1 + player.P3_2 + player.P3_3 + player.P3_4) / 20)
            * 40,
            'P4_p': player.P4_initial
            + ((player.P4_1 + player.P4_2 + player.P4_3 + player.P4_4) / 20)
            * 40,
        }


class wait_for_benef_5(Page):
    template_name = 'exclusion_control/wait_for_benef_5.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_5': player.benef_5,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + ((player.P1_1 + player.P1_2 + player.P1_3 + player.P1_4) / 20)
            * 40,
            'P2_p': player.P2_initial
            + ((player.P2_1 + player.P2_2 + player.P2_3 + player.P2_4) / 20)
            * 40,
            'P3_p': player.P3_initial
            + ((player.P3_1 + player.P3_2 + player.P3_3 + player.P3_4) / 20)
            * 40,
            'P4_p': player.P4_initial
            + ((player.P4_1 + player.P4_2 + player.P4_3 + player.P4_4) / 20)
            * 40,
        }
    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_5


class benef_6(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_6

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_5,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                )
                / 20
            )
            * 40,
        }



class wait_for_benef_6(Page):
    template_name = 'exclusion_control/wait_for_benef_6.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_6': player.benef_6,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                )
                / 20
            )
            * 40,
        }
    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_6


class benef_7(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_7

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_6,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                )
                / 20
            )
            * 40,
        }


class wait_for_benef_7(Page):
    template_name = 'exclusion_control/wait_for_benef_7.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_7': player.benef_7,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                )
                / 20
            )
            * 40,
        }
    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_7


class benef_8(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_8

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_7,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                )
                / 20
            )
            * 40,
        }



class wait_for_benef_8(Page):
    template_name = 'exclusion_control/wait_for_benef_8.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_8': player.benef_8,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                )
                / 20
            )
            * 40,
        }
    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_8

class benef_9(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_9

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_8,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                )
                / 20
            )
            * 40,
        }



class wait_for_benef_9(Page):
    template_name = 'exclusion_control/wait_for_benef_9.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_9': player.benef_9,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                )
                / 20
            )
            * 40,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_9


class benef_10(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_10

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_9,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                )
                / 20
            )
            * 40,
        }


class wait_for_benef_10(Page):
    template_name = 'exclusion_control/wait_for_benef_10.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_10': player.benef_10,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                )
                / 20
            )
            * 40,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_10


class benef_11(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_11

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_10,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                )
                / 20
            )
            * 40,
        }


class wait_for_benef_11(Page):
    template_name = 'exclusion_control/wait_for_benef_11.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_11': player.benef_11,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                )
                / 20
            )
            * 40,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_11


class benef_12(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_12

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_11,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                )
                / 20
            )
            * 40,
        }

class wait_for_benef_12(Page):
    template_name = 'exclusion_control/wait_for_benef_12.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_12': player.benef_12,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                )
                / 20
            )
            * 40,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_12


class benef_13(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_13

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_12,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                )
                / 20
            )
            * 40,
        }


class wait_for_benef_13(Page):
    template_name = 'exclusion_control/wait_for_benef_13.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_13': player.benef_13,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                )
                / 20
            )
            * 40,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_13


class benef_14(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_14

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_13,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + player.P1_13
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + player.P2_13
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + player.P3_13
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + player.P4_13
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                )
                / 20
            )
            * 40,
        }


class wait_for_benef_14(Page):
    template_name = 'exclusion_control/wait_for_benef_14.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_14': player.benef_14,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + player.P1_13
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + player.P2_13
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + player.P3_13
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + player.P4_13
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                )
                / 20
            )
            * 40,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_14

class benef_15(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_15

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_14,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + player.P1_13
            + player.P1_14
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + player.P2_13
            + player.P2_14
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + player.P3_13
            + player.P3_14
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + player.P4_13
            + player.P4_14
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                    + player.P1_14
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                    + player.P2_14
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                    + player.P3_14
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                    + player.P4_14
                )
                / 20
            )
            * 40,
        }


class wait_for_benef_15(Page):
    template_name = 'exclusion_control/wait_for_benef_15.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_15': player.benef_15,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + player.P1_13
            + player.P1_14
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + player.P2_13
            + player.P2_14
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + player.P3_13
            + player.P3_14
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + player.P4_13
            + player.P4_14
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                    + player.P1_14
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                    + player.P2_14
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                    + player.P3_14
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                    + player.P4_14
                )
                / 20
            )
            * 40,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_15


class benef_16(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_16

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_15,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + player.P1_13
            + player.P1_14
            + player.P1_15
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + player.P2_13
            + player.P2_14
            + player.P2_15
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + player.P3_13
            + player.P3_14
            + player.P3_15
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + player.P4_13
            + player.P4_14
            + player.P4_15
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                    + player.P1_14
                    + player.P1_15
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                    + player.P2_14
                    + player.P2_15
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                    + player.P3_14
                    + player.P3_15
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                    + player.P4_14
                    + player.P4_15
                )
                / 20
            )
            * 40,
        }


class wait_for_benef_16(Page):
    template_name = 'exclusion_control/wait_for_benef_16.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_16': player.benef_16,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + player.P1_13
            + player.P1_14
            + player.P1_15
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + player.P2_13
            + player.P2_14
            + player.P2_15
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + player.P3_13
            + player.P3_14
            + player.P3_15
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + player.P4_13
            + player.P4_14
            + player.P4_15
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                    + player.P1_14
                    + player.P1_15
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                    + player.P2_14
                    + player.P2_15
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                    + player.P3_14
                    + player.P3_15
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                    + player.P4_14
                    + player.P4_15
                )
                / 20
            )
            * 40,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_16

class benef_17(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_17

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_16,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + player.P1_13
            + player.P1_14
            + player.P1_15
            + player.P1_16
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + player.P2_13
            + player.P2_14
            + player.P2_15
            + player.P2_16
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + player.P3_13
            + player.P3_14
            + player.P3_15
            + player.P3_16
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + player.P4_13
            + player.P4_14
            + player.P4_15
            + player.P4_16
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                    + player.P1_14
                    + player.P1_15
                    + player.P1_16
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                    + player.P2_14
                    + player.P2_15
                    + player.P2_16
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                    + player.P3_14
                    + player.P3_15
                    + player.P3_16
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                    + player.P4_14
                    + player.P4_15
                    + player.P4_16
                )
                / 20
            )
            * 40,
        }


class wait_for_benef_17(Page):
    template_name = 'exclusion_control/wait_for_benef_17.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_17': player.benef_17,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + player.P1_13
            + player.P1_14
            + player.P1_15
            + player.P1_16
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + player.P2_13
            + player.P2_14
            + player.P2_15
            + player.P2_16
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + player.P3_13
            + player.P3_14
            + player.P3_15
            + player.P3_16
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + player.P4_13
            + player.P4_14
            + player.P4_15
            + player.P4_16
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                    + player.P1_14
                    + player.P1_15
                    + player.P1_16
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                    + player.P2_14
                    + player.P2_15
                    + player.P2_16
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                    + player.P3_14
                    + player.P3_15
                    + player.P3_16
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                    + player.P4_14
                    + player.P4_15
                    + player.P4_16
                )
                / 20
            )
            * 40,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_17


class benef_18(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_18

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_17,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + player.P1_13
            + player.P1_14
            + player.P1_15
            + player.P1_16
            + player.P1_17
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + player.P2_13
            + player.P2_14
            + player.P2_15
            + player.P2_16
            + player.P2_17
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + player.P3_13
            + player.P3_14
            + player.P3_15
            + player.P3_16
            + player.P3_17
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + player.P4_13
            + player.P4_14
            + player.P4_15
            + player.P4_16
            + player.P4_17
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                    + player.P1_14
                    + player.P1_15
                    + player.P1_16
                    + player.P1_17
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                    + player.P2_14
                    + player.P2_15
                    + player.P2_16
                    + player.P2_17
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                    + player.P3_14
                    + player.P3_15
                    + player.P3_16
                    + player.P3_17
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                    + player.P4_14
                    + player.P4_15
                    + player.P4_16
                    + player.P4_17
                )
                / 20
            )
            * 40,
        }



class wait_for_benef_18(Page):
    template_name = 'exclusion_control/wait_for_benef_18.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_18': player.benef_18,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + player.P1_13
            + player.P1_14
            + player.P1_15
            + player.P1_16
            + player.P1_17
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + player.P2_13
            + player.P2_14
            + player.P2_15
            + player.P2_16
            + player.P2_17
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + player.P3_13
            + player.P3_14
            + player.P3_15
            + player.P3_16
            + player.P3_17
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + player.P4_13
            + player.P4_14
            + player.P4_15
            + player.P4_16
            + player.P4_17
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                    + player.P1_14
                    + player.P1_15
                    + player.P1_16
                    + player.P1_17
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                    + player.P2_14
                    + player.P2_15
                    + player.P2_16
                    + player.P2_17
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                    + player.P3_14
                    + player.P3_15
                    + player.P3_16
                    + player.P3_17
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                    + player.P4_14
                    + player.P4_15
                    + player.P4_16
                    + player.P4_17
                )
                / 20
            )
            * 40,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_18


class benef_19(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_19

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_18,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + player.P1_13
            + player.P1_14
            + player.P1_15
            + player.P1_16
            + player.P1_17
            + player.P1_18
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + player.P2_13
            + player.P2_14
            + player.P2_15
            + player.P2_16
            + player.P2_17
            + player.P2_18
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + player.P3_13
            + player.P3_14
            + player.P3_15
            + player.P3_16
            + player.P3_17
            + player.P3_18
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + player.P4_13
            + player.P4_14
            + player.P4_15
            + player.P4_16
            + player.P4_17
            + player.P4_18
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                    + player.P1_14
                    + player.P1_15
                    + player.P1_16
                    + player.P1_17
                    + player.P1_18
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                    + player.P2_14
                    + player.P2_15
                    + player.P2_16
                    + player.P2_17
                    + player.P2_18
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                    + player.P3_14
                    + player.P3_15
                    + player.P3_16
                    + player.P3_17
                    + player.P3_18
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                    + player.P4_14
                    + player.P4_15
                    + player.P4_16
                    + player.P4_17
                    + player.P4_18
                )
                / 20
            )
            * 40,
        }



class wait_for_benef_19(Page):
    template_name = 'exclusion_control/wait_for_benef_19.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_19': player.benef_19,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + player.P1_13
            + player.P1_14
            + player.P1_15
            + player.P1_16
            + player.P1_17
            + player.P1_18
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + player.P2_13
            + player.P2_14
            + player.P2_15
            + player.P2_16
            + player.P2_17
            + player.P2_18
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + player.P3_13
            + player.P3_14
            + player.P3_15
            + player.P3_16
            + player.P3_17
            + player.P3_18
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + player.P4_13
            + player.P4_14
            + player.P4_15
            + player.P4_16
            + player.P4_17
            + player.P4_18
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                    + player.P1_14
                    + player.P1_15
                    + player.P1_16
                    + player.P1_17
                    + player.P1_18
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                    + player.P2_14
                    + player.P2_15
                    + player.P2_16
                    + player.P2_17
                    + player.P2_18
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                    + player.P3_14
                    + player.P3_15
                    + player.P3_16
                    + player.P3_17
                    + player.P3_18
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                    + player.P4_14
                    + player.P4_15
                    + player.P4_16
                    + player.P4_17
                    + player.P4_18
                )
                / 20
            )
            * 40,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_19

class benef_20(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.number == player.benef_20

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prev': player.benef_19,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + player.P1_13
            + player.P1_14
            + player.P1_15
            + player.P1_16
            + player.P1_17
            + player.P1_18
            + player.P1_19
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + player.P2_13
            + player.P2_14
            + player.P2_15
            + player.P2_16
            + player.P2_17
            + player.P2_18
            + player.P2_19
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + player.P3_13
            + player.P3_14
            + player.P3_15
            + player.P3_16
            + player.P3_17
            + player.P3_18
            + player.P3_19
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + player.P4_13
            + player.P4_14
            + player.P4_15
            + player.P4_16
            + player.P4_17
            + player.P4_18
            + player.P4_19
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                    + player.P1_14
                    + player.P1_15
                    + player.P1_16
                    + player.P1_17
                    + player.P1_18
                    + player.P1_19
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                    + player.P2_14
                    + player.P2_15
                    + player.P2_16
                    + player.P2_17
                    + player.P2_18
                    + player.P2_19
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                    + player.P3_14
                    + player.P3_15
                    + player.P3_16
                    + player.P3_17
                    + player.P3_18
                    + player.P3_19
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                    + player.P4_14
                    + player.P4_15
                    + player.P4_16
                    + player.P4_17
                    + player.P4_18
                    + player.P4_19
                )
                / 20
            )
            * 40,
        }


class wait_for_benef_20(Page):
    template_name = 'exclusion_control/wait_for_benef_20.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'benef_20': player.benef_20,
            'P1': player.P1_1
            + player.P1_2
            + player.P1_3
            + player.P1_4
            + player.P1_5
            + player.P1_6
            + player.P1_7
            + player.P1_8
            + player.P1_9
            + player.P1_10
            + player.P1_11
            + player.P1_12
            + player.P1_13
            + player.P1_14
            + player.P1_15
            + player.P1_16
            + player.P1_17
            + player.P1_18
            + player.P1_19
            + (player.P1_initial / 2),
            'P2': player.P2_1
            + player.P2_2
            + player.P2_3
            + player.P2_4
            + player.P2_5
            + player.P2_6
            + player.P2_7
            + player.P2_8
            + player.P2_9
            + player.P2_10
            + player.P2_11
            + player.P2_12
            + player.P2_13
            + player.P2_14
            + player.P2_15
            + player.P2_16
            + player.P2_17
            + player.P2_18
            + player.P2_19
            + (player.P2_initial / 2),
            'P3': player.P3_1
            + player.P3_2
            + player.P3_3
            + player.P3_4
            + player.P3_5
            + player.P3_6
            + player.P3_7
            + player.P3_8
            + player.P3_9
            + player.P3_10
            + player.P3_11
            + player.P3_12
            + player.P3_13
            + player.P3_14
            + player.P3_15
            + player.P3_16
            + player.P3_17
            + player.P3_18
            + player.P3_19
            + (player.P3_initial / 2),
            'P4': player.P4_1
            + player.P4_2
            + player.P4_3
            + player.P4_4
            + player.P4_5
            + player.P4_6
            + player.P4_7
            + player.P4_8
            + player.P4_9
            + player.P4_10
            + player.P4_11
            + player.P4_12
            + player.P4_13
            + player.P4_14
            + player.P4_15
            + player.P4_16
            + player.P4_17
            + player.P4_18
            + player.P4_19
            + (player.P4_initial / 2),
            'P1_p': player.P1_initial
            + (
                (
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                    + player.P1_14
                    + player.P1_15
                    + player.P1_16
                    + player.P1_17
                    + player.P1_18
                    + player.P1_19
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                    + player.P2_14
                    + player.P2_15
                    + player.P2_16
                    + player.P2_17
                    + player.P2_18
                    + player.P2_19
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                    + player.P3_14
                    + player.P3_15
                    + player.P3_16
                    + player.P3_17
                    + player.P3_18
                    + player.P3_19
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                    + player.P4_14
                    + player.P4_15
                    + player.P4_16
                    + player.P4_17
                    + player.P4_18
                    + player.P4_19
                )
                / 20
            )
            * 40,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.number != player.benef_20


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass

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
                    player.P1_1
                    + player.P1_2
                    + player.P1_3
                    + player.P1_4
                    + player.P1_5
                    + player.P1_6
                    + player.P1_7
                    + player.P1_8
                    + player.P1_9
                    + player.P1_10
                    + player.P1_11
                    + player.P1_12
                    + player.P1_13
                    + player.P1_14
                    + player.P1_15
                    + player.P1_16
                    + player.P1_17
                    + player.P1_18
                    + player.P1_19
                )
                / 20
            )
            * 40,
            'P2_p': player.P2_initial
            + (
                (
                    player.P2_1
                    + player.P2_2
                    + player.P2_3
                    + player.P2_4
                    + player.P2_5
                    + player.P2_6
                    + player.P2_7
                    + player.P2_8
                    + player.P2_9
                    + player.P2_10
                    + player.P2_11
                    + player.P2_12
                    + player.P2_13
                    + player.P2_14
                    + player.P2_15
                    + player.P2_16
                    + player.P2_17
                    + player.P2_18
                    + player.P2_19
                )
                / 20
            )
            * 40,
            'P3_p': player.P3_initial
            + (
                (
                    player.P3_1
                    + player.P3_2
                    + player.P3_3
                    + player.P3_4
                    + player.P3_5
                    + player.P3_6
                    + player.P3_7
                    + player.P3_8
                    + player.P3_9
                    + player.P3_10
                    + player.P3_11
                    + player.P3_12
                    + player.P3_13
                    + player.P3_14
                    + player.P3_15
                    + player.P3_16
                    + player.P3_17
                    + player.P3_18
                    + player.P3_19
                )
                / 20
            )
            * 40,
            'P4_p': player.P4_initial
            + (
                (
                    player.P4_1
                    + player.P4_2
                    + player.P4_3
                    + player.P4_4
                    + player.P4_5
                    + player.P4_6
                    + player.P4_7
                    + player.P4_8
                    + player.P4_9
                    + player.P4_10
                    + player.P4_11
                    + player.P4_12
                    + player.P4_13
                    + player.P4_14
                    + player.P4_15
                    + player.P4_16
                    + player.P4_17
                    + player.P4_18
                    + player.P4_19
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
        'rejected',
        'happy',
        'well_being',
    ]


    # def app_after_this_page(self, upcoming_apps):
    #   return "dictator"


page_sequence = [
    Introduction,
    benef_start,
    wait_for_benef_1,
    benef_2,
    wait_for_benef_3_2,
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
    Results,
    survey,
]
