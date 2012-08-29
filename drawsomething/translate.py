# -*- coding: utf-8 -*-

import google_translate


def translate(word, target):
    return google_translate.translate(word, target, 'en', flat=True)
