Jygsaw
======

.. highlight:: python

Jygsaw is a graphics library for Jython which makes graphics programming
easy to learn. At the same time, it is powerful, flexible, and
extensible, making it ideal for beginners and experienced programmers
alike.

Jygsaw takes many cues from the `Processing
language <http://processing.org>`__, but it uses Python, which is a
powerful, dynamic programming language with clear and readable syntax,
and runs on the Java Virtual Machine, making it portable and fast.

Here's a quick demo (taken from a Processing demo) to show you what
Jygsaw looks like.

::

    from jygsaw import *


    def draw():
        recursiveCircle(width() / 2, 280, 6)


    def recursiveCircle(x, radius, level):
        circleColor = int(126 * level / 4.0)
        fill(circleColor)
        circle(x, height() / 2, radius)
        if (level > 1):
            level = level - 1
            recursiveCircle(x - radius / 2, radius / 2, level)
            recursiveCircle(x + radius / 2, radius / 2, level)


    canvas(640, 360)
    onDraw(draw)

Documentation
-------------

Installation
~~~~~~~~~~~~

Simply use ``jython setup.py install``. If you are in a virtualenv using jython, ``python setup.py install`` will work, too.

Code
----

Jygsaw is developed on the Jython platform, using Java's Swing library.

Our git repository is hosted `on
Bitbucket <https://bitbucket.org/haplesshero13/cs98library/>`__.

Building Documentation
~~~~~~~~~~~~~~~~~~~~~~

First make sure you have Sphinx installed under Jython. Assuming you
have already installed Jython (and possibly Python), one way to do this
is using ``virtualenv``:

::

    :::bash
    $ cd cs98library
    $ easy_install virtualenv
    $ virtualenv -p jython venv
    $ source venv/bin/activate

Now when you type ``python --version`` in the command line you should
get ``Jython 2.5.3`` or whatever version of Jython you have installed,
and you should be able to build the docs.

::

    :::bash
    $ pip install sphinx
    $ cd doc
    $ make html

The documentation will appear in ``doc/_build/html``.

Authors
-------

Balkcom's Army is:

-  Aaditya Talwai
-  Avery Yen
-  Carla Galarza
-  David Lam
-  Janet Kim
-  Jennifer Lure
-  Kyle Lawson

We are led by our fearless leader, Commander (Professor) Devin Balkcom.
