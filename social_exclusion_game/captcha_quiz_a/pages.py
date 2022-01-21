from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants, cmp, distance_and_ok
from django.conf import settings



class Transcribe(Page):
    form_model = 'player'
    form_fields = ['transcribed_text']

    def vars_for_template(self):
        # specify info for progress bar
        print('Player.total_round_num on pages:', 30)
        self.subsession.total_round_num = 30
        if self.subsession.total_round_num > 700:
            self.subsession.total_round_num = 700
        if self.subsession.total_round_num < 1:
            self.subsession.total_round_num = 1
        total = self.subsession.total_round_num
        page = self.subsession.round_number
        progress = page / total * 30

        return {
            'image_path': 'captcha_quiz/paragraphs/{}.jpg'.format(
                self.round_number),
            'reference_text': Constants.reference_texts[self.round_number - 1],
            'debug': False,
            # 'debug': True,
            'required_accuracy': 30,
            'page': page,
            'total': total,
            'num_rounds': 30,
            'progress': progress

        }

    def transcribed_text_error_message(self, transcribed_text):
        reference_text = Constants.reference_texts[self.round_number - 1]
        distance, ok = distance_and_ok(transcribed_text, reference_text,
                                       0)
        if ok:
            self.player.cmp_dst = distance
        else:
            return "The answer should be exactly the same as on the image."



    # def app_after_this_page(self, upcoming_apps):
    #    #total = self.subsession.total_round_num
    #    total = self.session.config['num_rounds']
    #    now = self.player.round_number
    #    if total == now:
    #        return "mpl"

    def get_timeout_seconds(self):
        import time
        if 'timeout_captcha' not in self.participant.vars:
            self.participant.vars['timeout_captcha'] = time.time() + 300
        return self.participant.vars['timeout_captcha'] - time.time()

    def is_displayed(self):
        import time
        if 'timeout_captcha' not in self.participant.vars:
            self.participant.vars['timeout_captcha'] = time.time() + 300
        return self.participant.vars['timeout_captcha'] - time.time() > 1



class Wait_for_timer(Page):
    def app_after_this_page(self, upcoming_apps):
        # total = self.subsession.total_round_num
        total = 30
        now = self.player.round_number
        if total == now:
            return "mpl"

    def get_timeout_seconds(self):
        import time
        if 'timeout_captcha' not in self.participant.vars:
            self.participant.vars['timeout_captcha'] = time.time() + 300
        return self.participant.vars['timeout_captcha'] - time.time()

    def is_displayed(self):
        import time
        if 'timeout_captcha' not in self.participant.vars:
            self.participant.vars['timeout_captcha'] = time.time() + 300
        return (self.participant.vars['timeout_captcha'] - time.time() > 1) and (
                    self.round_number == 30)


page_sequence = [Transcribe, Wait_for_timer]
