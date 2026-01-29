from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'quest'



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # One field per round
    choice_round_1 = models.CurrencyField(min=0, max=C.ENDOWMENT, label="How many EMUs out of 20 do you want to send to the other participant?")
    choice_round_2a = models.CurrencyField(min=0, max=C.ENDOWMENT, label="How many EMUs out of 20 do you want to send to the other participant?")
    choice_round_2b = models.CurrencyField(min=0, max=C.ENDOWMENT, label="How many EMUs out of 20 do you want to send to the other participant?")
    choice_round_3a = models.CurrencyField(min=0, max=C.ENDOWMENT, label="How many EMUs out of 20 do you want to send to the other participant?")
    choice_round_3b = models.CurrencyField(min=0, max=C.ENDOWMENT, label="How many EMUs out of 20 do you want to send to the other participant?")
    #choice_round_4 = models.CurrencyField(min=0, max=C.ENDOWMENT, label="If the recipient is from your group and did easy / hard task")
    #choice_round_5 = models.CurrencyField(min=0, max=C.ENDOWMENT, label="If the recipient is from the other group and did easy / hard task")

