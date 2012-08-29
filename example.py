#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from drawsomething import get_words
from drawsomething import translate

TRANSLATE_TO = 'zh_cn'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--chars', help="Input all chars given")
    parser.add_argument('-l', '--length', type=int, help="Input word length")
    args = parser.parse_args()

    if not args.chars or not args.length:
        parser.print_help()
        return

    words = get_words(args.chars, args.length)
    for w in words:
        trans = translate(w, TRANSLATE_TO).lower()
        if w != trans:
            print w, trans
        else:
            print w


if __name__ == '__main__':
    main()
