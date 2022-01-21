from os import environ


SESSION_CONFIGS = [
    dict(
        name='dictator',
        display_name="dictator",
        num_demo_participants=4,
        app_sequence=['dictator'],
    ),
    dict(
        name='captcha_quiz',
        display_name='captcha',
        num_demo_participants=4,
        app_sequence=['captcha_quiz_a'],
    ),
    dict(
        name='exclusion',
        display_name='Prolific_treatment',
        num_demo_participants=12,
        app_sequence=['start_1', 'start','start_cont','captcha_quiz_a','exclusion','dictator', 'solo'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.1, participation_fee=1.00, doc=""
)

PARTICIPANT_FIELDS = ['points', 'first_income', 'wait_page_arrival', 'timeout_captcha']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
    dict(name='prolific', display_name='Room for the Prolific study'),
    ]

ADMIN_USERNAME = 'admin_exclusion'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'nfr2022'

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '##(c!a70-$jxfmk0y79@lnwew)u5)#mcwo2_p(mfh0&cffb96^'

INSTALLED_APPS = ['otree']
