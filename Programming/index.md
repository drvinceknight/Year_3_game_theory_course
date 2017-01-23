---
layout     : post
categories : content
title      : Programming
comments   : false
slug       : intro
---

There are various areas of Game theory that are suited to computer programming.

The two areas that naturally sit in this course are:

- The computation of equilibria;
- The study of the Iterated Prisoner's Dilemma

## A quick refresher of using Python

Note that this refresher uses **Python 3** and will also go over the use of
external libraries.

- I recommend using Anaconda as a distribution of Python. Go to
  [https://www.continuum.io/downloads](https://www.continuum.io/downloads) and
  follow the instructions there.
- Basics of Python using Jupyter notebooks.

    - [Code
      example](https://gist.github.com/drvinceknight/9e4e076e976fd6fdde3c11b78bfd5a27)
    - [Video walk through](https://youtu.be/zjnN9rtaSrA)

- External libraries.

    - [Code
      example](https://gist.github.com/drvinceknight/4bb764123a8a5dac33f2abb9a7f1150c)
    - [Video walk through](https://youtu.be/D7rPBULr058)

## Computation of equilibria

To compute equilibria there are 3 pieces of software available to you:

1. Cloud.sagemath (using Sage). Documentation:
   [doc.sagemath.org/html/en/reference/game_theory/index.html](http://doc.sagemath.org/html/en/reference/game_theory/index.html)

2. NashPy (a standalone Python library).

    - [Code
      example](https://gist.github.com/drvinceknight/9c5c424f7fb663f446c068ac71fa0f69)
    - [Video walk through](https://youtu.be/AZdP1yZscdg)

3. Gambit (a piece of software with a Python interface):
   [gambit.sourceforge.net/](http://gambit.sourceforge.net/).

## Studying the Iterated Prisoners' Dilemma

The main library used for the study of the Iterated Prisoners' Dilemma is the
Axelrod Python library.

- [Documentation](http://axelrod.readthedocs.io)
