#Jygsaw

Jygsaw is a graphics library for Jython which makes graphics programming easy to learn. 
At the same time, it's flexible and extensible, making it ideal for beginners and 
experienced programmers alike.

Jygsaw takes many cues from the [Processing Language](http://processing.org), but it uses 
Python, which is a powerful, dynamic programming language with clear and readable syntax, 
and runs on the Java Virtual Machine, making it portable.

Here's a quick demo (taken from a Processing demo) to show you what Jygsaw looks like.


```python
from jygsaw.graphics import *


def draw():
    drawCircle(width() / 2, 280, 6)

def drawCircle(x, radius, level):
    tt = int(126 * level / 4.0)
    fill(tt)
    circle(x, height() / 2, radius)
    if (level > 1):
        level = level - 1
        drawCircle(x - radius / 2, radius / 2, level)
        drawCircle(x + radius / 2, radius / 2, level)

canvas(640, 360)
noStroke()
onDraw(draw)
jygsawMain(.01)
```

## Code
Jygsaw is developed on the Jython platform, using Java's Swing library.

Our git repository is hosted 
[on BitBucket](https://bitbucket.org/haplesshero13/cs98library/).

You can run any demo using the local copy of Jygsaw (found in `jygsaw/`) by running, 
for example, `jython demos/keyboard.py`.

If you change directory into `demos/` and run demos, the demos are run using the 
system-installed version of Jygsaw, so make sure to reinstall Jygsaw in order to 
run the demos using the latest codebase!


#About Us

Jygsaw was written by a group of students at 
[Dartmouth College](http://www.dartmouth.edu), led by one 
[Professor Devin Balkcom](http://www.cs.dartmouth.edu/~devin) 
as part of their senior culminating experience. These students are all Computer Science 
majors:

* Aaditya Talwai '13
* Avery Yen '13
* Carla Galarza '13
* David Lam '11
* Janet Kim '13
* Jennifer Lure '13
* Kyle Lawson '13

## Future

Although Jygsaw is currently limited to graphics, it is an ever
growing library. We intend to add more features like a physics
package and a sound package, as well as an easy to use tool to allow
you to build jython programs into the executable of your choice.

We also intend to create more tutorials with more interactive elements
for the website.

## Inspiration
Jygsaw's design was heavily influenced by both [Processing](http://www.processing.org) 
and the CS1 python library written by Professor Devin Balkcom for use in the Computer 
Science 1 class at Dartmouth College.

## Contact

If you'd like to contact us with bugs, ideas, questions, etc. you can email us at 
<jygsaw@cs.dartmouth.edu>.
