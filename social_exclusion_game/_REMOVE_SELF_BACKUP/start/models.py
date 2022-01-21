from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'cerenay'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'start'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

    def group_by_arrival_time_method(subsession, waiting_players):
        if len(waiting_players) >= 4:
            return waiting_players[:4]
        for player in waiting_players:
            if player.waiting_too_long==1:
                # make a single-player group.
                return [player]

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Instr1 = models.IntegerField(blank=False, choices=[[1, 'Correct'], [2, 'False']])
    Instr2 = models.IntegerField(blank=False, choices=[[1, 'Correct'], [2, 'False']])
    Instr3 = models.IntegerField(blank=False, choices=[[1, 'Correct'], [2, 'False']])
    Instr4 = models.IntegerField(blank=False, choices=[[1, 'Correct'], [2, 'False']])
    comp_clicks = models.IntegerField()

    def get_wait_page_arrival(self):
        if "wait_page_arrival" in self.participant.vars:
            self.wait_page_arrival = self.participant.vars["wait_page_arrival"]


    def waiting_too_long(self):
        import time
        if time.time() - self.player.participant.vars["wait_page_arrival"] > 60:
            self.waiting_too_long = 1