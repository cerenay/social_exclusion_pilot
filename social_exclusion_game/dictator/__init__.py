from otree.api import *


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
    pass


class Group(BaseGroup):
    sent = models.IntegerField(
        doc="""Amount dictator decided to send""",
        min=0,
        max=Constants.endowment,
        label="I will send:",
    )


class Player(BasePlayer):
    payoff1 = models.IntegerField()
    points = models.IntegerField()
    first_income = models.IntegerField()
    payoffin = models.IntegerField()
    send_proxy = models.IntegerField(
        min=0,
        max=Constants.endowment,
        label="I will send:",
    )
    ##Questionnairre after all
    easy = models.IntegerField(
        blank=False,
        choices=[
            [1, 'Very difficult'],
            [2, 'Difficult'],
            [3, 'Neither difficult nor easy'],
            [4, 'Easy'],
            [5, 'Very easy'],
        ],
    )
    comments = models.StringField(blank=True)
    age = models.IntegerField(label='How old are you?', min=10, max=90)
    gender = models.StringField(
        choices=['I do not want to report my gender', 'Male', 'Female', 'Other'],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    edu = models.StringField(
        choices=[
            'Less than high school',
            'High school graduate',
            'Some College',
            '2 Years Degree',
            '4 Years Degree',
            'Professional degree',
            'Doctorate',
        ],
        label='What is your highest academic achievement?',
        widget=widgets.RadioSelect,
    )


# FUNCTIONS
def creating_session(subsession: Subsession):
    subsession.group_randomly()


def set_payoff1(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p2.payoff1 = group.sent
    p1.payoff1 = Constants.endowment - group.sent


def get_points(player: Player):
    participant = player.participant
    player.points = participant.points


def get_first_income(player: Player):
    participant = player.participant
    player.first_income = participant.first_income


# PAGES
class Introduction(Page):
    pass


class Offer(Page):
    form_model = 'group'
    form_fields = ['sent']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1


class offer_proxy(Page):
    form_model = 'player'
    form_fields = ['send_proxy']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2


class Wait_start(WaitPage):
    template_name = 'dictator/Wait_start.html'
    after_all_players_arrive = 'set_payoffs'
    after_all_players_arrive = 'set_payoff1'


class survey_end(Page):
    form_model = 'player'
    form_fields = ['easy', 'comments', 'age', 'gender', 'edu']

    @staticmethod
    def vars_for_template(player: Player):
        prolific_id = player.participant.label
        link = "https://app.prolific.co/submissions/complete?cc=3FD1BF2D"
        return {'link': link}


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant,
        return dict(
            offer=Constants.endowment - player.group.sent,
            payoff1=player.payoff1,
            points= player.participant.points+ player.participant.first_income,
            curr_points = (player.participant.points+ player.participant.first_income)/10,
            curr_payoff1=player.payoff1 / 10
        )


page_sequence = [Introduction, Offer, offer_proxy, Wait_start, Results, survey_end]
