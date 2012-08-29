Drawsomething
=============

Help you guess drawsomething words by brute force all permutations.

Depends
-------

- pyenchant
- google-translate

Install Guide
-------------

Take OS X for example.

Drawsomething depends on enchant to do spell checking.

As pyenchant is only a python binding for enchant, we need to install enchant first. And we also need to install aspell with en dict because enchant use aspell as backend.

::

    $ brew install aspell --lang=en
    $ brew install enchant
    $ pip install pyenchant google-translate

Usage
-----

One line script to generate all possible words.

::

    >>> import drawsomething
    >>> drawsomething.get_words('esttxyz', 4)
    ['ttys', 'sexy', 'yest', 'text', 'sett', 'zest', 'stet', 'test']


The `example.py` is an simple script to list all possible words with translations.

::

    $ python example.py -l 4 -c esttxyz
    ttys ttys中
    sexy 性感
    yest
    text 文本
    sett
    zest 热情
    stet
    test 测试
