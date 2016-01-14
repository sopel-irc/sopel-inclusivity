# coding=utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

import random

from sopel import module


# Works for generic "hi, guys", but maybe not "you (specific group of) guys"
greet = ['team', 'all', 'pals', 'gang', 'crew', 'people', 'everyone', 'friends',
         "y'all"]
# Works for specific group, but not really generic
yall = ["y'all", 'you all', 'you folks']


@module.rule('(hey|hi|yo|hello|howdy|um|er|oh)[,.?!:;]? guys')
def hi_guys(bot, trigger):
    bot.reply('Did you mean {}?'.format(random.choice(greet)))


@module.rule('.*you guys.*')
def you_guys(bot, trigger):
    bot.reply('Did you mean {}?'.format(random.choice(yall)))
