"""sopel-inclusivity

Inclusive language plugin for Sopel IRC bots
"""
from __future__ import annotations

import random

from sopel import plugin


# Works for generic "hi, guys", but maybe not "you (specific group of) guys"
greet = ['team', 'all', 'pals', 'gang', 'crew', 'people', 'everyone', 'friends',
         "y'all"]
# Works for specific group, but not really generic
yall = ["y'all", 'you all', 'you folks']


@plugin.rule('(hey|hi|yo|hello|howdy|um|er|oh)[,.?!:;]? guys')
def hi_guys(bot, trigger):
    bot.reply('Did you mean {}?'.format(random.choice(greet)))


@plugin.search('you guys')
def you_guys(bot, trigger):
    bot.reply('Did you mean {}?'.format(random.choice(yall)))
