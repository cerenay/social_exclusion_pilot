from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    template_name = 'start/MyPage.html'

class effort(Page):
    template_name= 'start/effort.html'


class GBAT(WaitPage):

    group_by_arrival_time = True

    def app_after_this_page(self, upcoming_apps):
        if len(self.player.get_others_in_group())== 3:
            return upcoming_apps[0]
        else:
            return "end_1"


class comprehension_test(Page):
    form_model = 'player'
    form_fields = ['Instr1',
                   'Instr2',
                   'Instr3',
                   'Instr4',
                   'comp_clicks']

    def error_message(self, values):
        if values["Instr1"] != 1:
            return 'Your answer to the first question is incorrect.'
        if values["Instr2"] != 2:
            return 'Your answer to the second question is incorrect.'
        if values["Instr3"] != 1:
            return 'Your answer to the third question is incorrect.'
        if values["Instr4"] != 1:
            return 'Your answer to the last question is incorrect.'

    def vars_for_template(self):
        prolific_id = self.player.participant.label

    def app_after_this_page(self, upcoming_apps):
        return "captcha_quiz"


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass







page_sequence = [GBAT, MyPage, effort, comprehension_test]
