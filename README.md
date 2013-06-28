# Jygsaw
Jygsaw is a graphics library for Jython which makes graphics programming easy to learn. At the same time, it is powerful, flexible, and extensible, making it ideal for beginners and experienced programmers alike.

Jygsaw takes many cues from the [Processing language](http://processing.org), but it uses Python, which is a powerful, dynamic programming language with clear and readable syntax, and runs on the Java Virtual Machine, making it portable and fast.

Here's a quick demo (taken from a Processing demo) to show you what Jygsaw looks like.


```
:::python
from jygsaw.graphics import *


def draw():
    recursive_circle(width() / 2, 280, 6)


# Recursively draw smaller circles
def recursive_circle(x, radius, level):
    tt = int(126 * level / 4.0)
    fill(tt)
    circle(x, height() / 2, radius)
    if (level > 1):
        level = level - 1
        recursive_circle(x - radius / 2, radius / 2, level)
        recursive_circle(x + radius / 2, radius / 2, level)


canvas(640, 360)
no_stroke()

on_draw(draw)
jygsaw_start()
```

## Installation
Simply use `jython setup.py install`. If you are in a virtualenv using jython, `python setup.py install` will work, too.

## Code
Jygsaw is developed on the Jython platform, using Java's Swing library.

Our git repository is hosted [on Bitbucket](https://bitbucket.org/haplesshero13/cs98library/).

### Testing
#### Jython 2.7+
Run `jython -m unittest discover`.

This will test the version of the code that lives in the current working directory, *not* the system-installed version.

#### Jython < 2.7
Install `unittest2`. The easiest way to do this is using `virtualenv` to create a local Jython installation in your current working directory. For example:

```
:::bash
$ cd cs98library
$ easy_install virtualenv
$ virtualenv -p jython venv
$ source venv/bin/activate
$ pip install unittest2
$ unit2 discover
```

#### Running individual tests (any version of Jython)
You can run any test against the *system-installed* version of Jygsaw.

```
:::bash
$ cd jygsaw/test
$ jython name_of_test.py
```

### Demos
You can run any demo using the local copy of Jygsaw (found in `jygsaw/`) by running, for example, `jython demos/keyboard.py`.

If you change directory into `demos/` and run demos, the demos run using the system-installed version of Jygsaw, so make sure to reinstall Jygsaw in order to run the demos using the latest codebase!

### Building Documentation
First make sure you have Sphinx installed under Jython. Assuming you have already installed Jython (and possibly Python), one way to do this is using `virtualenv`:

```
:::bash
$ cd cs98library
$ easy_install virtualenv
$ virtualenv -p jython venv
$ source venv/bin/activate
```

Now when you type `python --version` in the command line you should get `Jython 2.5.3` or whatever version of Jython you have installed, and you should be able to build the docs.

```
:::bash
$ pip install sphinx
$ cd doc
$ make html
```

The documentation will appear in `doc/_build/html`.

## Authors
* Aaditya Talwai
* Avery Yen
* Carla Galarza
* David Lam
* Janet Kim
* Jennifer Lure
* Kyle Lawson

