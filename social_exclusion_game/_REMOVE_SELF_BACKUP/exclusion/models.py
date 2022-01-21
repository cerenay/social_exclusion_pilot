from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import itertools
import json



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

    def creating_session(subsession):
        # randomize to treatments
        #conditions = itertools.cycle(['One', 'Two', 'Three', 'beneficiary'])
        colours = itertools.cycle(['Green', 'Purple', 'Green', 'Purple'])
        for player in subsession.get_players():
            #player.condition = next(conditions)
            player.colour = next(colours)
        for g in subsession.get_groups():
            players = g.get_players()
            for p in players:
                chosen_player = random.choice(players)
                p1 = g.get_player_by_id(1)
                p2 = g.get_player_by_id(2)
                p3 = g.get_player_by_id(3)
                p4 = g.get_player_by_id(4)
                p.position = 'Not beneficiary'
                p.luck = 0
                p.first_income = 0
            chosen_player.position = 'Beneficiary'
            chosen_player.luck =1
            chosen_player.first_income = 2
            if p1.position == 'Beneficiary':
                p1.first_benef = 1
                p2.first_benef = 1
                p3.first_benef = 1
                p4.first_benef = 1
                p1.P1_initial =2
                p2.P1_initial =2
                p3.P1_initial =2
                p4.P1_initial =2
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

class Group(BaseGroup):


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


    def set_points(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)
        p1.points = ((self.P1_1 + self.P1_2 + self.P1_3 + self.P1_4 + self.P1_5 + self.P1_6 + self.P1_7 + self.P1_8 + self.P1_9 + self.P1_10 + self.P1_11 + self.P1_12 + self.P1_13 + self.P1_14 + self.P1_15 + self.P1_16 + self.P1_17 + self.P1_18 + self.P1_19) / 20) * 40
        p2.points = ((self.P2_1 + self.P2_2 + self.P2_3 + self.P2_4 + self.P2_5 + self.P2_6 + self.P2_7 + self.P2_8 + self.P2_9 + self.P2_10 + self.P2_11 + self.P2_12 + self.P2_13 + self.P2_14 + self.P2_15 + self.P2_16 + self.P2_17 + self.P2_18 + self.P2_19) / 20) * 40
        p3.points = ((self.P3_1 + self.P3_2 + self.P3_3 + self.P3_4 + self.P3_5 + self.P3_6 + self.P3_7 + self.P3_8 + self.P3_9 + self.P3_10 + self.P3_11 + self.P3_12 + self.P3_13 + self.P3_14 + self.P3_15 + self.P3_16 + self.P3_17 + self.P3_18 + self.P3_19) / 20) * 40
        p4.points = ((self.P4_1 + self.P4_2 + self.P4_3 + self.P4_4 + self.P4_5 + self.P4_6 + self.P4_7 + self.P4_8 + self.P4_9 + self.P4_10 + self.P4_11 + self.P4_12 + self.P4_13 + self.P4_14 + self.P4_15 + self.P4_16 + self.P4_17 + self.P4_18 + self.P4_19) / 20) * 40


    def set_payoff2(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)
        p1.payoff2 = ((p1.P1_initial + self.P1_1 + self.P1_2 + self.P1_3 + self.P1_4 + self.P1_5 + self.P1_6 + self.P1_7 + self.P1_8 + self.P1_9 + self.P1_10 + self.P1_11 + self.P1_12 + self.P1_13 + self.P1_14 + self.P1_15 + self.P1_16 + self.P1_17 + self.P1_18 + self.P1_19) / 20) * 4
        p2.payoff2 = ((p2.P2_initial + self.P2_1 + self.P2_2 + self.P2_3 + self.P2_4 + self.P2_5 + self.P2_6 + self.P2_7 + self.P2_8 + self.P2_9 + self.P2_10 + self.P2_11 + self.P2_12 + self.P2_13 + self.P2_14 + self.P2_15 + self.P2_16 + self.P2_17 + self.P2_18 + self.P2_19) / 20) * 4
        p3.payoff2 = ((p3.P3_initial + self.P3_1 + self.P3_2 + self.P3_3 + self.P3_4 + self.P3_5 + self.P3_6 + self.P3_7 + self.P3_8 + self.P3_9 + self.P3_10 + self.P3_11 + self.P3_12 + self.P3_13 + self.P3_14 + self.P3_15 + self.P3_16 + self.P3_17 + self.P3_18 + self.P3_19) / 20) * 4
        p4.payoff2 = ((p4.P4_initial + self.P4_1 + self.P4_2 + self.P4_3 + self.P4_4 + self.P4_5 + self.P4_6 + self.P4_7 + self.P4_8 + self.P4_9 + self.P4_10 + self.P4_11 + self.P4_12 + self.P4_13 + self.P4_14 + self.P4_15 + self.P4_16 + self.P4_17 + self.P4_18 + self.P4_19) / 20) * 4


class Player(BasePlayer):




    def get_partner(self):
        return self.player.get_others_in_group()


    points = models.FloatField()
    payoff2 = models.IntegerField()
    first_benef = models.IntegerField()
    P1_initial=models.IntegerField()
    P2_initial=models.IntegerField()
    P3_initial=models.IntegerField()
    P4_initial=models.IntegerField()
    P1_luck=models.IntegerField()
    P2_luck=models.IntegerField()
    P3_luck=models.IntegerField()
    P4_luck=models.IntegerField()
    first_income=models.IntegerField()

##Questionnairre after Stage 2
    exclusion = models.IntegerField(blank=False, choices=[[1, 'Strongly disagree'], [2, 'Disagree'], [3, 'Neither disagree nor agree'], [4, 'Agree'], [5, 'Strongly agree']])
    inclusion = models.IntegerField(blank=False, choices=[[1, 'Strongly disagree'], [2, 'Disagree'], [3, 'Neither disagree nor agree'], [4, 'Agree'], [5, 'Strongly agree']])
    own_team = models.IntegerField(blank=False, choices=[[1, 'Strongly disagree'], [2, 'Disagree'], [3, 'Neither disagree nor agree'], [4, 'Agree'], [5, 'Strongly agree']])
    other_team = models.IntegerField(blank=False, choices=[[1, 'Strongly disagree'], [2, 'Disagree'], [3, 'Neither disagree nor agree'], [4, 'Agree'], [5, 'Strongly agree']])
    fair= models.IntegerField(blank=False, choices=[[1, 'Strongly disagree'], [2, 'Disagree'], [3, 'Neither disagree nor agree'], [4, 'Agree'], [5, 'Strongly agree']])
    fair_benef = models.IntegerField(blank=False, choices=[[1, 'Very unfair'], [2, 'Unfair'], [3, 'Neither unfair nor fair'], [4, 'Fair'], [5, 'Very fair']])
    fair_benef_own = models.IntegerField(blank=False, choices=[[1, 'Very unfair'], [2, 'Unfair'], [3, 'Neither unfair nor fair'], [4, 'Fair'], [5, 'Very fair']])
    fair_benef_other = models.IntegerField(blank=False, choices=[[1, 'Very unfair'], [2, 'Unfair'], [3, 'Neither unfair nor fair'], [4, 'Fair'], [5, 'Very fair']])
    rejected = models.IntegerField(blank=False, choices=[[1, 'Always'], [2, 'Often'], [3, 'About half the time'], [4, 'Seldom'], [5, 'Never']])
    happy = models.IntegerField(blank=False, choices=[[0, '0-Not happy  at all'], [1, '1-'],[2, '2-'], [3, '3-'], [4, '4-'], [5, '5-'],[6, '6-'],[7, '7-'],[8, '8-'],[9, '9-'],[10, '10-Extremely happy']])
    well_being = models.IntegerField(blank=False, choices=[[0, '-5- Much lower than before'], [1, '-4'], [2, '-3'], [3, '-2'], [4, '-1'], [5, '0- No change'],[6, '1'],[7, '2'],[8, '3'],[9, '4'],[10, '+5- Much higher than before'] ])
## Post-experiment questionnairre








####1st round

    #condition = models.StringField()
    colour = models.StringField()
    position = models.StringField()
    luck = models.IntegerField()
    initial = models.IntegerField()
    first_role = models.IntegerField()

####2nd round

