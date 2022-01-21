from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Wait_start(WaitPage):
    template_name = 'exclusion/Wait_start.html'
    group_by_arrival_time = True


class Introduction(Page):
    def vars_for_template(self):
        return{
            'color' : self.player.colour
        }



class history_0(Page):


    def vars_for_template(self):
        my_partners = self.player.get_others_in_group()
        return dict(
            my_partners = my_partners,
            position = self.player.position
        )


class benef_start(Page):
    def vars_for_template(self):
        my_partners = self.player.get_others_in_group()
        return{
            'id': self.player.id_in_group,
            'my_partners' : my_partners}

    def is_displayed(self):
        return self.player.position == 'Beneficiary'
    form_model = 'group'
    form_fields = ['P1_1', 'P2_1', 'P3_1', 'P4_1', 'benef_2']

class wait_for_benef_1(WaitPage):
    template_name = 'exclusion/wait_for_benef_1.html'
    def vars_for_template(self):
        my_partners = self.player.get_others_in_group()
        return{
            'my_partners' : my_partners,
            'benef_start' : self.player.first_benef
        }


class Waiting(WaitPage):
    pass

class history_1(Page):
    def vars_for_template(self):
        return{
            'P1' :self.player.group.P1_1+(self.player.P1_initial/2),
            'P2': self.player.group.P2_1+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+(self.player.P3_initial/2),
            'P4': self.player.group.P4_1+(self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1/20)*40),
            'P2_p': self.player.P2_initial+((self.player.group.P2_1/20)*40),
            'P3_p': self.player.P3_initial+((self.player.group.P3_1/20)*40),
            'P4_p': self.player.P4_initial+((self.player.group.P4_1/20)*40)
        }


class benef_2(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_2


    form_model = 'group'
    form_fields = ['P1_2', 'P2_2', 'P3_2', 'P4_2' ,'benef_3']


    def vars_for_template(self):
        my_partners = self.player.get_others_in_group()
        return dict(
            my_partners = my_partners,
            position = self.player.position,
            first_benef = self.player.first_benef
        )

class wait_for_benef_2(WaitPage):
    template_name = 'exclusion/wait_for_benef_2.html'

    def vars_for_template(self):
        return{
            'benef_2': self.player.group.benef_2,
             'P1' :self.player.group.P1_1+(self.player.P1_initial/2),
            'P2': self.player.group.P2_1+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+(self.player.P3_initial/2),
            'P4': self.player.group.P4_1+(self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1/20)*40),
            'P2_p': self.player.P2_initial+((self.player.group.P2_1/20)*40),
            'P3_p': self.player.P3_initial+((self.player.group.P3_1/20)*40),
            'P4_p': self.player.P4_initial+((self.player.group.P4_1/20)*40)

        }

class history_2(Page):
    def vars_for_template(self):
        return{
            'P1' :self.player.group.P1_1+self.player.group.P1_2+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+ (self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2) / 20) * 40

        }

class benef_3(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_3
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_2,
            'P1': self.player.group.P1_1 + self.player.group.P1_2 + (self.player.P1_initial / 2),
            'P2': self.player.group.P2_1 + self.player.group.P2_2 + (self.player.P2_initial / 2),
            'P3': self.player.group.P3_1 + self.player.group.P3_2 + (self.player.P3_initial / 2),
            'P4': self.player.group.P4_1 + self.player.group.P4_2 + (self.player.P4_initial / 2),
            'P1_p': self.player.P1_initial + ((self.player.group.P1_1 + self.player.group.P1_2) / 20) * 40,
            'P2_p': self.player.P2_initial + ((self.player.group.P2_1 + self.player.group.P2_2) / 20) * 40,
            'P3_p': self.player.P3_initial + ((self.player.group.P3_1 + self.player.group.P3_2) / 20) * 40,
            'P4_p': self.player.P4_initial + ((self.player.group.P4_1 + self.player.group.P4_2) / 20) * 40
        }

    form_model = 'group'
    form_fields = ['P1_3', 'P2_3', 'P3_3', 'P4_3' ,'benef_4']

class wait_for_benef_3(WaitPage):
    template_name = 'exclusion/wait_for_benef_3.html'

    def vars_for_template(self):
        return{
            'benef_3': self.player.group.benef_3,
             'P1' :self.player.group.P1_1+self.player.group.P1_2+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+ (self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2) / 20) * 40


        }

class history_3(Page):
    def vars_for_template(self):
        return{
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3,
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3,
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3,
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3,
            'P1_p': ((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3)/20) * 40,
            'P2_p': ((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3) / 20) * 40,
            'P3_p': ((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3) / 20) * 40,
            'P4_p': ((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3) / 20) * 40

        }


class benef_4(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_4
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_3,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+ self.player.group.P2_3+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_4', 'P2_4', 'P3_4', 'P4_4' ,'benef_5']

class wait_for_benef_4(WaitPage):
    template_name = 'exclusion/wait_for_benef_4.html'

    def vars_for_template(self):
        return{
            'benef_4': self.player.group.benef_4,
             'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+ self.player.group.P2_3+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3) / 20) * 40
        }


class benef_5(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_5
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_4,
            'P1': self.player.group.P1_1 + self.player.group.P1_2 + self.player.group.P1_3 + self.player.group.P1_4 + (self.player.P1_initial / 2),
            'P2': self.player.group.P2_1 + self.player.group.P2_2 + self.player.group.P2_3 + self.player.group.P2_4 + (self.player.P2_initial / 2),
            'P3': self.player.group.P3_1 + self.player.group.P3_2 + self.player.group.P3_3 + self.player.group.P3_4 + (self.player.P3_initial / 2),
            'P4': self.player.group.P4_1 + self.player.group.P4_2 + self.player.group.P4_3 + self.player.group.P4_4 + (self.player.P4_initial / 2),
            'P1_p': self.player.P1_initial + ((self.player.group.P1_1 + self.player.group.P1_2 + self.player.group.P1_3 + self.player.group.P1_4) / 20) * 40,
            'P2_p': self.player.P2_initial + (( self.player.group.P2_1 + self.player.group.P2_2 + self.player.group.P2_3 + self.player.group.P2_4) / 20) * 40,
            'P3_p': self.player.P3_initial + ((self.player.group.P3_1 + self.player.group.P3_2 + self.player.group.P3_3 + self.player.group.P3_4) / 20) * 40,
            'P4_p': self.player.P4_initial + ((self.player.group.P4_1 + self.player.group.P4_2 + self.player.group.P4_3 + self.player.group.P4_4) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_5', 'P2_5', 'P3_5', 'P4_5' ,'benef_6']

class wait_for_benef_5(WaitPage):
    template_name = 'exclusion/wait_for_benef_5.html'

    def vars_for_template(self):
        return{
            'benef_5': self.player.group.benef_5,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4) / 20) * 40
        }




class benef_6(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_6
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_5,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5) / 20) * 40


        }

    form_model = 'group'
    form_fields = ['P1_6', 'P2_6', 'P3_6', 'P4_6' ,'benef_7']

class wait_for_benef_6(WaitPage):
    template_name = 'exclusion/wait_for_benef_6.html'

    def vars_for_template(self):
        return{
            'benef_6': self.player.group.benef_6,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5) / 20) * 40
        }


class benef_7(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_7
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_6,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_7', 'P2_7', 'P3_7', 'P4_7' ,'benef_8']

class wait_for_benef_7(WaitPage):
    template_name = 'exclusion/wait_for_benef_7.html'

    def vars_for_template(self):
        return{
            'benef_7': self.player.group.benef_7,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6) / 20) * 40
        }



class benef_8(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_8
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_7,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_8', 'P2_8', 'P3_8', 'P4_8' ,'benef_9']

class wait_for_benef_8(WaitPage):
    template_name = 'exclusion/wait_for_benef_8.html'

    def vars_for_template(self):
        return{
            'benef_8': self.player.group.benef_8,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7) / 20) * 40
        }



class benef_9(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_9
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_8,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_9', 'P2_9', 'P3_9', 'P4_9' ,'benef_10']

class wait_for_benef_9(WaitPage):
    template_name = 'exclusion/wait_for_benef_9.html'

    def vars_for_template(self):
        return{
            'benef_9': self.player.group.benef_9,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8) / 20) * 40
        }

class benef_10(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_10
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_9,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_10', 'P2_10', 'P3_10', 'P4_10' ,'benef_11']

class wait_for_benef_10(WaitPage):
    template_name = 'exclusion/wait_for_benef_10.html'

    def vars_for_template(self):
        return{
            'benef_10': self.player.group.benef_10,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9) / 20) * 40
        }


class benef_11(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_11
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_10,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_11', 'P2_11', 'P3_11', 'P4_11' ,'benef_12']

class wait_for_benef_11(WaitPage):
    template_name = 'exclusion/wait_for_benef_11.html'

    def vars_for_template(self):
        return{
            'benef_11': self.player.group.benef_11,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10) / 20) * 40
        }


class benef_12(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_12
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_11,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_12', 'P2_12', 'P3_12', 'P4_12' ,'benef_13']

class wait_for_benef_12(WaitPage):
    template_name = 'exclusion/wait_for_benef_12.html'

    def vars_for_template(self):
        return{
            'benef_12': self.player.group.benef_12,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11) / 20) * 40
        }


class benef_13(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_13
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_12,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_13', 'P2_13', 'P3_13', 'P4_13' ,'benef_14']

class wait_for_benef_13(WaitPage):
    template_name = 'exclusion/wait_for_benef_13.html'

    def vars_for_template(self):
        return{
            'benef_13': self.player.group.benef_13,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12) / 20) * 40
        }


class benef_14(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_14
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_13,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_14', 'P2_14', 'P3_14', 'P4_14' ,'benef_15']

class wait_for_benef_14(WaitPage):
    template_name = 'exclusion/wait_for_benef_14.html'

    def vars_for_template(self):
        return{
            'benef_14': self.player.group.benef_14,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13) / 20) * 40
        }


class benef_15(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_15
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_14,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_15', 'P2_15', 'P3_15', 'P4_15' ,'benef_16']

class wait_for_benef_15(WaitPage):
    template_name = 'exclusion/wait_for_benef_15.html'

    def vars_for_template(self):
        return{
            'benef_15': self.player.group.benef_15,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14) / 20) * 40
        }

class benef_16(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_16
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_15,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_16', 'P2_16', 'P3_16', 'P4_16' ,'benef_17']

class wait_for_benef_16(WaitPage):
    template_name = 'exclusion/wait_for_benef_16.html'

    def vars_for_template(self):
        return{
            'benef_16': self.player.group.benef_16,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15) / 20) * 40
        }


class benef_17(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_17
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_16,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_17', 'P2_17', 'P3_17', 'P4_17' ,'benef_18']

class wait_for_benef_17(WaitPage):
    template_name = 'exclusion/wait_for_benef_17.html'

    def vars_for_template(self):
        return{
            'benef_17': self.player.group.benef_17,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16) / 20) * 40
        }

class benef_18(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_18
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_17,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16+self.player.group.P1_17+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16+self.player.group.P2_17+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16+self.player.group.P3_17+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16+self.player.group.P4_17+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16+self.player.group.P1_17)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16+self.player.group.P2_17) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16+self.player.group.P3_17) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16+self.player.group.P4_17) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_18', 'P2_18', 'P3_18', 'P4_18' ,'benef_19']

class wait_for_benef_18(WaitPage):
    template_name = 'exclusion/wait_for_benef_18.html'

    def vars_for_template(self):
        return{
            'benef_18': self.player.group.benef_18,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16+self.player.group.P1_17+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16+self.player.group.P2_17+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16+self.player.group.P3_17+ (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16+self.player.group.P4_17+ (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16+self.player.group.P1_17)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16+self.player.group.P2_17) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16+self.player.group.P3_17) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16+self.player.group.P4_17) / 20) * 40
        }


class benef_19(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_19
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_18,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16+self.player.group.P1_17+ self.player.group.P1_18+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16+self.player.group.P2_17+self.player.group.P2_18+ (self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16+self.player.group.P3_17+self.player.group.P3_18+  (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16+self.player.group.P4_17+self.player.group.P4_18+  (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16+self.player.group.P1_17+self.player.group.P1_18)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16+self.player.group.P2_17+self.player.group.P2_18) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16+self.player.group.P3_17+self.player.group.P3_18) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16+self.player.group.P4_17+self.player.group.P4_18) / 20) * 40

        }

    form_model = 'group'
    form_fields = ['P1_19', 'P2_19', 'P3_19', 'P4_19' ,'benef_20']

class wait_for_benef_19(WaitPage):
    template_name = 'exclusion/wait_for_benef_19.html'

    def vars_for_template(self):
        return{
            'benef_19': self.player.group.benef_19,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16+self.player.group.P1_17+ self.player.group.P1_18+ (self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16+self.player.group.P2_17+self.player.group.P2_18+ (self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16+self.player.group.P3_17+self.player.group.P3_18+  (self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16+self.player.group.P4_17+self.player.group.P4_18+  (self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16+self.player.group.P1_17+self.player.group.P1_18)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16+self.player.group.P2_17+self.player.group.P2_18) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16+self.player.group.P3_17+self.player.group.P3_18) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16+self.player.group.P4_17+self.player.group.P4_18) / 20) * 40
        }



class benef_20(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.player.group.benef_20
    def vars_for_template(self):
        return{
            'prev': self.player.group.benef_19,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16+self.player.group.P1_17+ self.player.group.P1_18+self.player.group.P1_19+(self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16+self.player.group.P2_17+self.player.group.P2_18+self.player.group.P2_19+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16+self.player.group.P3_17+self.player.group.P3_18+self.player.group.P3_19+(self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16+self.player.group.P4_17+self.player.group.P4_18+self.player.group.P4_19+(self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16+self.player.group.P1_17+self.player.group.P1_18+self.player.group.P1_19)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16+self.player.group.P2_17+self.player.group.P2_18+self.player.group.P2_19) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16+self.player.group.P3_17+self.player.group.P3_18+self.player.group.P3_19) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16+self.player.group.P4_17+self.player.group.P4_18+self.player.group.P4_19) / 20) * 40

        }

class wait_for_benef_20(WaitPage):
    template_name = 'exclusion/wait_for_benef_20.html'

    def vars_for_template(self):
        return{
            'benef_20': self.player.group.benef_20,
            'P1' :self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16+self.player.group.P1_17+ self.player.group.P1_18+self.player.group.P1_19+(self.player.P1_initial/2),
            'P2':self.player.group.P2_1+ self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16+self.player.group.P2_17+self.player.group.P2_18+self.player.group.P2_19+(self.player.P2_initial/2),
            'P3': self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16+self.player.group.P3_17+self.player.group.P3_18+self.player.group.P3_19+(self.player.P3_initial/2),
            'P4': self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16+self.player.group.P4_17+self.player.group.P4_18+self.player.group.P4_19+(self.player.P4_initial/2),
            'P1_p': self.player.P1_initial+((self.player.group.P1_1+self.player.group.P1_2+self.player.group.P1_3+self.player.group.P1_4+self.player.group.P1_5+self.player.group.P1_6+self.player.group.P1_7+self.player.group.P1_8+self.player.group.P1_9+self.player.group.P1_10+self.player.group.P1_11+self.player.group.P1_12+self.player.group.P1_13+self.player.group.P1_14+self.player.group.P1_15+self.player.group.P1_16+self.player.group.P1_17+self.player.group.P1_18+self.player.group.P1_19)/20) * 40,
            'P2_p': self.player.P2_initial+((self.player.group.P2_1+self.player.group.P2_2+self.player.group.P2_3+self.player.group.P2_4+self.player.group.P2_5+self.player.group.P2_6+self.player.group.P2_7+self.player.group.P2_8+self.player.group.P2_9+self.player.group.P2_10+self.player.group.P2_11+self.player.group.P2_12+self.player.group.P2_13+self.player.group.P2_14+self.player.group.P2_15+self.player.group.P2_16+self.player.group.P2_17+self.player.group.P2_18+self.player.group.P2_19) / 20) * 40,
            'P3_p': self.player.P3_initial+((self.player.group.P3_1+self.player.group.P3_2+self.player.group.P3_3+self.player.group.P3_4+self.player.group.P3_5+self.player.group.P3_6+self.player.group.P3_7+self.player.group.P3_8+self.player.group.P3_9+self.player.group.P3_10+self.player.group.P3_11+self.player.group.P3_12+self.player.group.P3_13+self.player.group.P3_14+self.player.group.P3_15+self.player.group.P3_16+self.player.group.P3_17+self.player.group.P3_18+self.player.group.P3_19) / 20) * 40,
            'P4_p': self.player.P4_initial+((self.player.group.P4_1+self.player.group.P4_2+self.player.group.P4_3+self.player.group.P4_4+self.player.group.P4_5+self.player.group.P4_6+self.player.group.P4_7+self.player.group.P4_8+self.player.group.P4_9+self.player.group.P4_10+self.player.group.P4_11+self.player.group.P4_12+self.player.group.P4_13+self.player.group.P4_14+self.player.group.P4_15+self.player.group.P4_16+self.player.group.P4_17+self.player.group.P4_18+self.player.group.P4_19) / 20) * 40
        }


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoff2'
    after_all_players_arrive = 'set_points'

class Results(Page):
    def vars_for_template(self):
        first = self.player.first_income
        return{
            'points': c(self.player.points+first),
            'payoff': self.player.payoff2,
            'P1_p': self.player.P1_initial + ((self.player.group.P1_1 + self.player.group.P1_2 + self.player.group.P1_3 + self.player.group.P1_4 + self.player.group.P1_5 + self.player.group.P1_6 + self.player.group.P1_7 + self.player.group.P1_8 + self.player.group.P1_9 + self.player.group.P1_10 + self.player.group.P1_11 + self.player.group.P1_12 + self.player.group.P1_13 + self.player.group.P1_14 + self.player.group.P1_15 + self.player.group.P1_16 + self.player.group.P1_17 + self.player.group.P1_18 + self.player.group.P1_19) / 20) * 40,
            'P2_p': self.player.P2_initial + ((self.player.group.P2_1 + self.player.group.P2_2 + self.player.group.P2_3 + self.player.group.P2_4 + self.player.group.P2_5 + self.player.group.P2_6 + self.player.group.P2_7 + self.player.group.P2_8 + self.player.group.P2_9 + self.player.group.P2_10 + self.player.group.P2_11 + self.player.group.P2_12 + self.player.group.P2_13 + self.player.group.P2_14 + self.player.group.P2_15 + self.player.group.P2_16 + self.player.group.P2_17 + self.player.group.P2_18 + self.player.group.P2_19) / 20) * 40,
            'P3_p': self.player.P3_initial + ((self.player.group.P3_1 + self.player.group.P3_2 + self.player.group.P3_3 + self.player.group.P3_4 + self.player.group.P3_5 + self.player.group.P3_6 + self.player.group.P3_7 + self.player.group.P3_8 + self.player.group.P3_9 + self.player.group.P3_10 + self.player.group.P3_11 + self.player.group.P3_12 + self.player.group.P3_13 + self.player.group.P3_14 + self.player.group.P3_15 + self.player.group.P3_16 + self.player.group.P3_17 + self.player.group.P3_18 + self.player.group.P3_19) / 20) * 40,
            'P4_p': self.player.P4_initial + ((self.player.group.P4_1 + self.player.group.P4_2 + self.player.group.P4_3 + self.player.group.P4_4 + self.player.group.P4_5 + self.player.group.P4_6 + self.player.group.P4_7 + self.player.group.P4_8 + self.player.group.P4_9 + self.player.group.P4_10 + self.player.group.P4_11 + self.player.group.P4_12 + self.player.group.P4_13 + self.player.group.P4_14 + self.player.group.P4_15 + self.player.group.P4_16 + self.player.group.P4_17 + self.player.group.P4_18 + self.player.group.P4_19) / 20) * 40

        }

    def before_next_page(self):
        participant = self.player.participant
        self.participant.vars["points"] = self.player.points
        self.participant.vars["first_income"] = self.player.first_income



class survey(Page):
    form_model = 'player'
    form_fields = ['exclusion',
                   'inclusion',
                   'fair',
                   'fair_benef',
                   'fair_benef_other',
                   'fair_benef_own',
                   'rejected',
                   'happy',
                   'well_being'
                   ]

    #def app_after_this_page(self, upcoming_apps):
     #   return "dictator"


page_sequence = [
    Wait_start,
    Introduction,
    benef_start,
    wait_for_benef_1,
    benef_2,
    wait_for_benef_2,
    benef_3,
    wait_for_benef_3,
    benef_4,
    wait_for_benef_4,
    benef_5,
    wait_for_benef_5,
    benef_6,
    wait_for_benef_6,
    benef_7,
    wait_for_benef_7,
    benef_8,
    wait_for_benef_8,
    benef_9,
    wait_for_benef_9,
    benef_10,
    wait_for_benef_10,
    benef_11,
    wait_for_benef_11,
    benef_12,
    wait_for_benef_12,
    benef_13,
    wait_for_benef_13,
    benef_14,
    wait_for_benef_14,
    benef_15,
    wait_for_benef_15,
    benef_16,
    wait_for_benef_16,
    benef_17,
    wait_for_benef_17,
    benef_18,
    wait_for_benef_18,
    benef_19,
    wait_for_benef_19,
    benef_20,
    wait_for_benef_20,
    ResultsWaitPage,
    Results,
    survey
]
