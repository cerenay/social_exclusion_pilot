from otree.api import *


author = 'Your name here'
doc = """
Game with sender and receiver. 
"""


class Constants(BaseConstants):
    name_in_url = 'social_decision'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
