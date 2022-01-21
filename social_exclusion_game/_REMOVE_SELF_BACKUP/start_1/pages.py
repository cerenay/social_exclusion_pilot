from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class welcome(Page):
    def before_next_page(self):
        import time
        self.participant.vars["wait_page_arrival"] = time.time()


page_sequence = [welcome]
