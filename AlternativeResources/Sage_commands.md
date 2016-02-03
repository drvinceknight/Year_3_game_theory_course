---
layout     : post
categories : alternativeresources
title      : Sage help sheet
comments   : true
slug       : sagecommandsforgametheory
---

This sheet includes a list of Sage commands that could be of use to you during this course.

**You can find a worksheet containing all of these commands [here](https://cloud.sagemath.com/projects/9d1b4517-a8e4-4d63-b083-71ea3b945737/files/Game Theory: Sage Help Sheet.sagews).**
Just copy that in to your own project and you can go ahead and use it or just use the embedded cells here (although you will not be able to save any output).

The School of Mathematics has started teaching programming to all first year students and has also introduced the open source mathematics software [Sage](http://sagemath.org/).

From time to time I will be demonstrating things using Sage, if you would like to use Sage: watch [this video](http://www.youtube.com/watch?v=3E9LvXV_zrA&feature=youtu.be) about setting up an account on the University server.

\textbf{Note the requirement to use your Cardiff University username as a username for a Sage account}.

You can always type `help(function)` to get help for any Sage `function`. There is a lot of help online and the official website is a good place to start: [sagemath.org/](http://sagemath.org/)


## Rearranging expressions

You will often have simple expressions like \\(7x-18(1-x)\\) that need simplifying (sometimes they will be more complex than that obviously).
These commands show you how to carry this out:

    sage: exp = 7 * x - 18 * (1 - x)
    sage: exp

If your expression was more complicated you could use `simplify(exp)`, `expand(exp)` and/or `factor(exp)`.

<div class="compute"><script type="text/x-sage">
exp = 7 * x - 18 * (1 - x)
exp
</script></div>

## Plotting functions

To plot a function \\(f:x\to 35x-2\\) type:

    sage: f(x) = 35 * x - 2
    sage: plot(f, x, 0, 1)

The 3rd and 4th arguments are telling Sage to plot for \\(0\leq x \leq 1\\).

<div class="compute"><script type="text/x-sage">
f(x) = 35 * x - 2
plot(f, x, 0, 1)
</script></div>

## Solving equations

Linear equations appear all the time in this course. To solve \\(7x-2(1-x)=3x+6(1-x)\\):

    sage: solve(7 * x - 2 * ( 1 - x) == 3 * x + 6 * (1 - x), x)

<div class="compute"><script type="text/x-sage">
solve(7 * x - 2 * ( 1 - x) == 3 * x + 6 * (1 - x), x)
</script></div>

## Differentiation

To obtain: \\(\frac{du_1}{du_1}\\) where \\(u_1=(K - q_1 - q_2)q_1 - kq_1\\):

    sage: K, q1, q2, k = var('K, q1, q2, k') # We need to tell Sage that these are symbolic variables
    sage: u1 = (K - q1 - q2) * q1 - k * q1
    sage: diff(u1, q1)

<div class="compute"><script type="text/x-sage">
K, q1, q2, k = var('K, q1, q2, k') # We need to tell Sage that these are symbolic variables
u1 = (K - q1 - q2) * q1 - k * q1
diff(u1, q1)
</script></div>

If we wanted to find the point at which this equates to zero we would write the following:

    sage: du = diff(u1, q1)
    sage: solve(du = 0, q1)

<div class="compute"><script type="text/x-sage">
K, q1, q2, k = var('K, q1, q2, k') # We need to tell Sage that these are symbolic variables
u1 = (K - q1 - q2) * q1 - k * q1
du = diff(u1, q1)
solve(du == 0, q1)
</script></div>

## Infinite sums

Sage can be used to obtain expressions like \\(\sum_{i=0}^{\infty}\left(\frac{1}{3}\right)^i\\):

    sage: i = var('i')
    sage: sum((1 / 3) ^ i, i, 0, oo)

<div class="compute"><script type="text/x-sage">
i = var('i')
sum((1 / 3) ^ i, i, 0, oo)
</script></div>

Sage can also be used to check symbolic expressions of this nature. For example you can quickly check what  the expression for \\(\sum_{i=0}^{\infty} x^i\\) is:

    sage: i = var('i')
    sage: assume(abs(x) < 1)
    sage: sum(x ^ i, i, 0, oo)

<div class="compute"><script type="text/x-sage">
i = var('i')
assume(abs(x) < 1)
sum(x ^ i, i, 0, oo)
</script></div>

### Permutations

To quickly obtain all permutations of a set of the set \\(\{1,2,3\}\\):

    sage: p = Permutations([1,2,3])
    sage: list(p)

<div class="compute"><script type="text/x-sage">
p = Permutations([1, 2, 3])
list(p)
</script></div>

### Contour plots

I find 3D surface plots messy and unclear. Here is how to obtain a contour plot of the function: \\(f: x,y \to 3x-y+2\\)

    sage: y = var('y')
    sage: f(x,y) = 3 * x + y - ( 2 - y)
    sage: contour_plot(f, (0,1), (0,1), colorbar=True, axes_labels=['$x$', '$y$'], cmap='summer')

(There are various options that can be passed to the cmap argument: try `import matplotlib.cm; matplotlib.cm.datad.keys()` to list them)

<div class="compute"><script type="text/x-sage">
y = var('y')
f(x,y) = 3 * x + y - ( 2 - y)
contour_plot(f, (0,1), (0,1), colorbar=True, axes_labels=['$x$', '$y$'], cmap='summer')
</script></div>

### Minimizing functions

You might need to minimize the following function \\(c:\alpha, \beta\to \alpha ^ 3 + 3\beta/2 + \alpha ^ 2 + 2\alpha\beta+\beta^2-2\alpha-2\beta+1\\) with the following constraints: \\(0\leq \alpha \leq 1\\) and \\(0\leq \beta \leq 1\\). Here is how to do that in Sage:

    sage: f = lambda p: p[0] ^ 3 + 3 / 2 * p[1] ^ 2 + p[0] ^ 2 + 2 * p[0] * p[1] + p[1] ^ 2 - 2 * (p[0] + p[1]) + 1
    sage: c_1 = lambda p: p[0]
    sage: c_2 = lambda p: 1 - p[0]
    sage: c_3 = lambda p: p[1]
    sage: c_4 = lambda p: 1 - p[1]
    sage: a = minimize_constrained(f, [c_1, c_2, c_3, c_4], [0, 0])
    sage: a

<div class="compute"><script type="text/x-sage">
f = lambda p: p[0] ^ 3 + 3 / 2 * p[1] ^ 2 + p[0] ^ 2 + 2 * p[0] * p[1] + p[1] ^ 2 - 2 * (p[0] + p[1]) + 1
c_1 = lambda p: p[0]
c_2 = lambda p: 1 - p[0]
c_3 = lambda p: p[1]
c_4 = lambda p: 1 - p[1]
a = minimize_constrained(f, [c_1, c_2, c_3, c_4], [0, 0])
a
</script></div>

For more details on minimization take a look at [this page](http://www.sagemath.org/doc/reference/numerical/sage/numerical/optimize.html).

### Finding Nash equilibria of Normal Form Games

You can easily obtain the Nash Equilibria for a generic Normal Form game:

    sage: A = matrix([[1, 5],[2, 3]])
    sage: B = matrix([[3, 5],[4, 1]])
    sage: g = NormalFormGame([A, B])
    sage: g.obtain_nash()

<div class="compute"><script type="text/x-sage">
A = matrix([[1, 5],[2, 3]])
B = matrix([[3, 5],[4, 1]])
g = NormalFormGame([A, B])
g.obtain_nash()
</script></div>

You can also just pass a single matrix for a zero sum game:

    sage: C = matrix([[0, -1, 1],[1, 0, -1], [-1, 1, 0]])
    sage: g = NormalFormGame([C])
    sage: g.obtain_nash()

<div class="compute"><script type="text/x-sage">
C = matrix([[0, -1, 1],[1, 0, -1], [-1, 1, 0]])
g = NormalFormGame([C])
g.obtain_nash()
</script></div>

[Read the documentation for a good overview of the capabilities as well as a good set of examples](http://www.sagemath.org/doc/reference/game_theory/sage/game_theory/normal_form_game.html).

### Calculate the shapley value

You can easily obtain the stable matching for a game:

    sage: cf = {():0, (1): 3, (2): 4, (3): 2, (1, 2): 3, (1, 3): 5, (2, 3): 10, (1, 2, 3): 12}
    sage: g = CooperativeGame(cf)
    sage: g.shapley_value()

<div class="compute"><script type="text/x-sage">
cf = {():0, (1): 3, (2): 4, (3): 2, (1, 2): 3, (1, 3): 5, (2, 3): 10, (1, 2, 3): 12}
g = CooperativeGame(cf)
g.shapley_value()
</script></div>

[More info available here](http://www.sagemath.org/doc/reference/game_theory/sage/game_theory/cooperative_game.html).

### Obtain a stable matching

You can quickly obtain a stable matching

```python

sage: suitr_pref = {'J': ('A', 'D', 'C', 'B'),
....:               'K': ('A', 'B', 'C', 'D'),
....:               'L': ('B', 'D', 'C', 'A'),
....:               'M': ('C', 'A', 'B', 'D')}
sage: reviewr_pref = {'A': ('L', 'J', 'K', 'M'),
....:                 'B': ('J', 'M', 'L', 'K'),
....:                 'C': ('K', 'M', 'L', 'J'),
....:                 'D': ('M', 'K', 'J', 'L')}
sage: m = MatchingGame([suitr_pref, reviewr_pref])
sage: m.solve()
```

<div class="compute"><script type="text/x-sage">
suitr_pref = {'J': ('A', 'D', 'C', 'B'),
              'K': ('A', 'B', 'C', 'D'),
              'L': ('B', 'D', 'C', 'A'),
              'M': ('C', 'A', 'B', 'D')}
reviewr_pref = {'A': ('L', 'J', 'K', 'M'),
                'B': ('J', 'M', 'L', 'K'),
                'C': ('K', 'M', 'L', 'J'),
                'D': ('M', 'K', 'J', 'L')}
m = MatchingGame([suitr_pref, reviewr_pref])
m.solve()
</script></div>

[More info available here](http://www.sagemath.org/doc/reference/game_theory/sage/game_theory/matching_game.html).
