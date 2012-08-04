Drawsomething
=============

Help you guess drawsomething words by brute force all permutations.

Depends
-------

* pyenchant (for spell checking)
* google-translate (for words translation)

Install Guide
-------------

Take OS X for example.

Enchant is a program used for spell checking.

As pyenchant is only a python binding for enchant, we need to install enchant first. And we also need to install aspell with en dict because enchant use aspell as backend.

    $ brew install aspell --lang=en
    $ brew install enchant
    $ pip install pyenchant google-translate

Usage
-----

    from drawsomething import get_words
    words = get_words('esttxyz', 4)

Example
-------

    $ python example.py -l 4 -c esttxyz
