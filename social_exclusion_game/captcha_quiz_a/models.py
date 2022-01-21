from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

doc = """
Captcha quiz, release 1.0.2, Made by JJ(jaejun.lees@gmail.com)
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


class Constants(BaseConstants):

    name_in_url = 'captcha_quiz'
    players_per_group = None
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
        "HAPK3", #10
        "VSJS",
        "CJR69H",
        "YBJWY",
        "BD8W",
        "ARKUH",
        "PRRCBU",
        "WPVA",
        "VEHKX",
        "5UDWEJ",
        "5RRT9R", #20
        "8NWTTS",
        "CSBHT",
        "U5BS89",
        "KR9RY",
        "WNW6",
        "TYXXWS",
        "SRXK",
        "36HX",
        "KVW34",
        "SE9K", #30
    ]

    num_rounds = len(reference_texts)
    allowed_error_rates = [0, 0.03]



class Subsession(BaseSubsession):
    total_round_num = models.IntegerField()
    def live_bid(self, data, data2):
        total_round_num = data2
    pass


class Group(BaseGroup):
    def live_bid(self, data, data2):
        Subsession.total_round_num = data2
#    pass


