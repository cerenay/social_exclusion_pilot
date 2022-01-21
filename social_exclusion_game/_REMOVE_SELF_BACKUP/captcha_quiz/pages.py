from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants, cmp, distance_and_ok
from django.conf import settings


class Transcribe(Page):
    form_model = 'player'
    form_fields = ['transcribed_text']

    def vars_for_template(self):
        # specify info for progress bar
        print('Player.num_rounds on pages:', 30)
        total = 30
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


class Results(Page):
    def is_displayed(self):
        # return self.round_number == self.player.total_round_num
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        table_rows = []
        for prev_player in self.player.in_all_rounds():
            row = {
                'round_number': prev_player.round_number,
                'reference_text_length': len(Constants.reference_texts[prev_player.round_number - 1]),
                'transcribed_text_length': len(prev_player.transcribed_text),
                'distance': prev_player.levenshtein_distance,
            }
            table_rows.append(row)

        return {'table_rows': table_rows}

    def app_after_this_page(self, upcoming_apps):
        return "exclusion"


class Wait_for_timer(Page):
    def app_after_this_page(self, upcoming_apps):
        # total = self.subsession.total_round_num
        total = self.session.config['num_rounds']
        now = self.player.round_number
        if total == now:
            return "exclusion"



page_sequence = [Transcribe]
