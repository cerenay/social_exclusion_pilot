from otree.api import *


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
            if waiting_too_long(player):
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

def waiting_too_long(player: Player):
    participant = player.participant
    import time
# assumes you set wait_page_arrival in PARTICIPANT_FIELDS.
    return time.time() - participant.wait_page_arrival > 60*3


# FUNCTIONS



# PAGES
class GBAT(WaitPage):
    template_name = 'start/GBAT.html'
    group_by_arrival_time = True

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        # if it's a solo group (1 player), skip this app
        # and go to the next app (which in this case is a
        # single-player task)
        if len(player.get_others_in_group()) < 3:
            return "solo"
        else:
            return upcoming_apps[0]

class MyPage(Page):
    template_name = 'start/MyPage.html'


class effort(Page):
    template_name = 'start/effort.html'



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
        return "captcha_quiz"


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [GBAT]
