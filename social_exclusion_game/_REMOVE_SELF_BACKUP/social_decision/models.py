from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


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
