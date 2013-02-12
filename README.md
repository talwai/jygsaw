# Jygsaw
Jygsaw is a graphics library for Jython which makes graphics programming easy to learn. At the same time, it is powerful, flexible, and extensible, making it ideal for beginners and experienced programmers alike.

Jygsaw takes many cues from the [Processing language](http://processing.org), but it uses Python, which is a powerful, dynamic programming language with clear and readable syntax, and runs on the Java Virtual Machine, making it portable and fast.

Here's a quick demo (taken from a Processing demo) to show you what Jygsaw looks like.


```
:::python
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

```

## Documentation

### Installation
Do stuff.
### Tutorial
Write stuff.
### Reference
Stuff happens.

## Code
Jygsaw is developed on the Jython platform, using Java's Swing library.

Our git repository is hosted [on Bitbucket](https://bitbucket.org/haplesshero13/cs98library/).

## Authors
Balkcom's Army is:

* Aaditya Taalwi
* Avery Yen
* Carla Galarza
* David Lam
* Janet Kim
* Jennifer Lure
* Kyle Lawson

We are led by our fearless leader, Commander (Professor) Devin Balkcom.