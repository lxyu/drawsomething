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

One line script to generate all possible words:

::

    >>> import drawsomething
    >>> drawsomething.get_words('esttxyz', 4)
    ['ttys', 'sexy', 'yest', 'text', 'sett', 'zest', 'stet', 'test']


To list words with translations:

::

    >>> import drawsomething
    >>> words = drawsomething.get_words('esttxyz', 4)
    >>> for w in words:
    >>>     trans = drawsomething.translate(w, 'zh_cn').lower()
    >>>     print w, trans


The `drawsth` is a cli script to list all possible words:

::

    $ drawsth -l 4 -c esttxyz
    ttys ttys中
    sexy 性感
    yest
    text 文本
    sett
    zest 热情
    stet
    test 测试
