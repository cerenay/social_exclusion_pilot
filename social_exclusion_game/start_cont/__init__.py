from otree.api import *
import random
import itertools


author = 'cerenay'
doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'start_cont'
    players_per_group = 4
    num_rounds = 1


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):

    Instr1 = models.IntegerField(blank=False, choices=[[1, 'Correct'], [2, 'False']])
    Instr2 = models.IntegerField(blank=False, choices=[[1, 'Correct'], [2, 'False']])
    Instr3 = models.IntegerField(blank=False, choices=[[1, 'Correct'], [2, 'False']])
    Instr4 = models.IntegerField(blank=False, choices=[[1, 'Correct'], [2, 'False']])
    comp_clicks = models.IntegerField()
    position = models.StringField()
    trying = models.IntegerField()
    colour = models.StringField()
    prolific_id = models.StringField(default = str(" "))

# FUNCTIONS

# PAGES

class MyPage(Page):
    template_name = 'start_cont/MyPage.html'


class effort(Page):
    template_name = 'start_cont/effort.html'
    def before_next_page(player: Player, timeout_happened):
        player.prolific_id = player.participant.label


class comprehension_test(Page):
    form_model = 'player'
    form_fields = ['Instr1', 'Instr2', 'Instr3', 'Instr4', 'comp_clicks']

    @staticmethod
    def error_message(player: Player, values):
        if values["Instr1"] != 2:
            return 'Your answer to the first question is incorrect.'
        if values["Instr2"] != 1:
            return 'Your answer to the second question is incorrect.'
        if values["Instr3"] != 2:
            return 'Your answer to the third question is incorrect.'
        if values["Instr4"] != 1:
            return 'Your answer to the last question is incorrect.'

    @staticmethod
    def vars_for_template(player: Player):
        prolific_id = player.participant.label

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        return "captcha_quiz_a"


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, effort, comprehension_test]
