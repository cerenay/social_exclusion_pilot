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


doc = """
One player decides how to divide a certain amount between himself and the other
player.

See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.

"""


class Constants(BaseConstants):
    name_in_url = 'stage_3'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'dictator/instructions.html'

    # Initial amount allocated to the dictator
    endowment = 10


class Subsession(BaseSubsession):

    def creating_session(subsession):
        subsession.group_randomly()

class Group(BaseGroup):

    sent = models.IntegerField(
        doc="""Amount dictator decided to send""",
        min=0,
        max=Constants.endowment,
        label="I will send",
    )

    def set_payoff1(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p2.payoff1 = self.sent
        p1.payoff1 = Constants.endowment - self.sent


    def set_points(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.points = self.player.participant.vars['points']
        p2.points = self.player.participant.vars['points']

    def set_first_income(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.first_income = self.player.participant.vars['first_income']
        p2.first_income = self.player.participant.vars['first_income']

    def set_payoffin(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p2.payoffin = self.sent+self.participant.vars["points"]
        p1.payoffin = Constants.endowment - self.sent +self.participant.vars["points"]



class Player(BasePlayer):

    def get_points(self):
        if "points" in self.participant.vars:
            self.points = self.participant.vars["points"]
        else:
            self.points = 0

    def get_first_income(self):
        if "first_income" in self.participant.vars:
            self.first_income = self.participant.vars["first_income"]
        else:
            self.points = 0

    payoff1 = models.IntegerField()
    points = models.IntegerField()
    first_income = models.IntegerField()
    payoffin = models.IntegerField()


    send_proxy= models.IntegerField(
        min=0,
        max=Constants.endowment,
        label="I will send",

    )

    ##Questionnairre after all
    easy = models.IntegerField(blank=False, choices=[[1, 'Very difficult'], [2, 'Difficult'],
                                                          [3, 'Neither difficult nor easy'], [4, 'Easy'],
                                                          [5, 'Very easy']])
    comments = models.StringField(blank=True)

    age = models.IntegerField(
        label='How old are you?',
        min=10, max=90)

    gender = models.StringField(
        choices=['I do not want to report my gender', 'Male', 'Female', 'Other'],
        label='What is your gender?',
        widget=widgets.RadioSelect)

    edu = models.StringField(
        choices=['Less than high school', 'High school graduate', 'Some College', '2 Year Degree', '4 Year Degree',
                 'Professional degree', 'Doctorate'],
        label='What is your highest academic achievement?',
        widget=widgets.RadioSelect
    )









