# -*- coding: utf-8 -*-

import enchant
import itertools


def get_words(chars, length):
    """
    Brute force all permutations to generate all possible words
    """
    d = enchant.Dict('en_US')

    candidates = set()
    for p in itertools.permutations(chars, length):
        candidates.add(''.join(p))

    words = []
    for c in candidates:
        if d.check(c):
            words.append(c)

    return words
