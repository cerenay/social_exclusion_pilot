from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Offer(Page):
    form_model = 'group'
    form_fields = ['sent']

    def is_displayed(self):
        return self.player.id_in_group == 1

class offer_proxy(Page):
    form_model = 'player'
    form_fields = ['send_proxy']

    def is_displayed(self):
        return self.player.id_in_group == 2

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'
    after_all_players_arrive = 'set_points'
    after_all_players_arrive = 'set_payoff1'

class survey_end(Page):
    form_model = 'player'
    form_fields = ['easy',
                   'comments',
                   'age',
                   'gender',
                   'edu']

    def vars_for_template(self):
        prolific_id = self.player.participant.label
        link = "https://app.prolific.co/submissions/complete?cc=1111111"+str(prolific_id)
        return {
            'link': link
        }




class Results(Page):
    def vars_for_template(self):
        return dict(offer=Constants.endowment - self.group.sent,
                    payoff1=self.player.payoff1,
                    points=self.player.participant.vars['points']+self.player.participant.vars['first_income'],
                    payoff=self.player.payoffin,
                    curr_payoff1=self.player.payoff1/10,
                    curr_points=(self.player.participant.vars['points']+self.player.participant.vars['first_income'])/10
                    )


page_sequence = [Introduction, Offer, offer_proxy, ResultsWaitPage, Results, survey_end]
