import random

from otree.api import *


doc = """
Captcha quiz
"""


def cmp(a, b):
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n
    current = range(n + 1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if a[j - 1] != b[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)
    return current[n]


def distance_and_ok(input_text, reference_text, max_error_rate):
    error_threshold = len(reference_text) * max_error_rate
    distance = cmp(input_text, reference_text)
    ok = distance <= error_threshold
    return distance, ok


class Player(BasePlayer):
    total_round_num = models.IntegerField()
    transcribed_text = models.StringField()
    cmp_dst = models.IntegerField()
    completed = models.IntegerField(initial=0)
    num_rounds = models.IntegerField(initial=0)

def transcribed_text_error_message(player: Player, transcribed_text):
    reference_text = Constants.reference_texts[player.round_number - 1]
    distance, ok = distance_and_ok(transcribed_text, reference_text, 0)
    if ok:
        player.cmp_dst = distance
    else:
        return "The answer should be exactly the same as on the image."




class Constants(BaseConstants):
    name_in_url = 'stage_1'
    players_per_group = 4
    progress_bar = True
    reference_texts = [
        "W93BX",
        "JA3V8",
        "RBSKW",
        "HJ9PV",
        "TSMS9",
        "459CT",
        "R84CH",
        "D4TSH",
        "3M56R",
        "HAPK3",  # 10
        "VSJS",
        "CJR69H",
        "YBJWY",
        "BD8W",
        "ARKUH",
        "PRRCBU",
        "WPVA",
        "VEHKX",
        "5UDWEJ",
        "5RRT9R",  # 20
        "8NWTTS",
        "CSBHT",
        "U5BS89",
        "KR9RY",
        "WNW6",
        "TYXXWS",
        "SRXK",
        "36HX",
        "KVW34",
        "SE9K",  # 30
    ]
    num_rounds = 30
    allowed_error_rates = [0, 0.03]


class Subsession(BaseSubsession):
    total_round_num = models.IntegerField()


class Group(BaseGroup):
    total_round_num = models.IntegerField()


# FUNCTIONS
    @staticmethod
    def transcribed_text_error_message(player: Player, transcribed_text):
        reference_text = Constants.reference_texts[player.round_number - 1]
        distance, ok = distance_and_ok(transcribed_text, reference_text, 0)
        if ok:
            player.cmp_dst = distance
        else:
            return "The answer should be exactly the same as on the image."

# PAGES
class Transcribe(Page):
    form_model = 'player'
    form_fields = ['transcribed_text']

    @staticmethod
    def vars_for_template(player: Player):
        # specify info for progress bar
        print('Player.num_rounds on pages:', 30)
        total = 30
        page = player.subsession.round_number
        progress = page / total * 30
        return {
            'image_path': 'captcha_quiz/paragraphs/{}.jpg'.format(player.round_number),
            'reference_text': Constants.reference_texts[player.round_number - 1],
            'debug': False,
            # 'debug': True,
            'required_accuracy': 30,
            'page': page,
            'total': total,
            'num_rounds': 30,
            'progress': progress,
        }

    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        if 'timeout_captcha' not in participant.vars:
            participant.timeout_captcha = time.time() + 60*4
        return participant.timeout_captcha - time.time()

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        import time
        if 'timeout_captcha' not in participant.vars:
            participant.timeout_captcha = time.time() + 60*4
        return participant.timeout_captcha - time.time() > 1



    # def app_after_this_page(self, upcoming_apps):
    #    #total = self.subsession.total_round_num
    #    total = self.session.config['num_rounds']
    #    now = self.player.round_number
    #    if total == now:
    #        return "mpl"


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        # return self.round_number == self.player.total_round_num
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        table_rows = []
        for prev_player in player.in_all_rounds():
            row = {
                'round_number': prev_player.round_number,
                'reference_text_length': len(
                    Constants.reference_texts[prev_player.round_number - 1]
                ),
                'transcribed_text_length': len(prev_player.transcribed_text),
                'distance': prev_player.levenshtein_distance,
            }
            table_rows.append(row)
        return {'table_rows': table_rows}

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        return "exclusion"


class Wait_for_timer(Page):
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        # total = self.subsession.total_round_num
        total = 30
        now = player.round_number
        if total == now:
            return "exclusion"

    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        if 'timeout_captcha' not in participant.vars:
            participant.timeout_captcha = time.time() + 300
        return participant.timeout_captcha - time.time()

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        import time
        if 'timeout_captcha' not in participant.vars:
            participant.timeout_captcha = time.time() + 300
        return (participant.timeout_captcha - time.time() > 1) and (
                    player.round_number == 30
        )


page_sequence = [Transcribe, Wait_for_timer]
