# Sage commands that are useful on this course

This sheet includes a list of Sage commands that could be of use to you during this course.

The School of Mathematics has started teaching programming to all first year students and has also introduced the open source mathematics software [Sage](http://sagemath.org/).

From time to time I will be demonstrating things using Sage, if you would like to use Sage: watch this video about setting up an account on the University server:

<iframe width="560" height="315" src="//www.youtube.com/embed/3E9LvXV_zrA" frameborder="0" allowfullscreen></iframe>

\textbf{Note the requirement to use your Cardiff University username as a username for a Sage account}.

You can always type `help(function)` to get help for any Sage `function`.

## Rearranging equations

You will often have simple expressions like $7x-18(1-x)$ that need simplifying (sometimes they will be more complex than that obviously).
These commands show you how to carry this out:

~~~{.python}
sage: exp = 7 * x - 18 * (1 - x)
sage: exp
~~~

If your expression was more complicated you could use `simplify(exp)`, `expand(exp)` and/or `factor(exp)`.

## Plotting functions

To plot a function $f:x\to 35x-2$ type:

_~~{.python}
To plot a function $f:x\to 35x-2$ type:
t(f,(0,1),(0,1),colorbar=True,axes_labels=['$x$','$y$'], cmap='rainbow')
sage: f(x) = 35 * x - 2
sage: plot(f, x, 0, 1)
~~~

The 3rd and 4th arguments are telling Sage to plot for $0\leq x \leq 1$.

## Solving equations

Linear equations appear all the time in this course. To solve $7x-2(1-x)=3x+6(1-x)$:

~~~{.python}
sage: solve(7 * x - 2 * ( 1 - x) == 3 * x + 6 * (1 - x), x)
~~~

## Differentiation

To obtain: $\frac{du_1}{du_1}$ where $u_1=(K - q_1 - q_2)q_1 - kq_1$:

~~~{.python}
sage: K, q1, q2, k = var('K, q1, q2, k') # We need to tell Sage that these are symbolic variables
sage: u1 = (K - q1 - q2) * q1 - k * q1
sage: diff(u1, q1)
~~~

If we wanted to find the point at which this equates to zero we would write the following:

~~~{.python}
sage: du = diff(u1, q1)
sage: solve(du = 0, q1)
~~~

## Infinite sum

Sage can be used to obtain expressions like $\sum_{i=0}^{\infty}\left(\frac{1}{3}\right)^i$:

~~~{.python}
sage: i = var('i')
sage: sum((1 / 3) ^ i, i, 0, oo)
~~~

Sage can also be used to check symbolic expressions of this nature. For example you can quickly check what  the expression for $\sum_{i=0}^{\infty} x^i$is:

~~~{.python}
sage: i = var('i')
sage: assume(abs(x) < 1)
sage: sum(x ^ i, i, 0, oo)
~~~

### Permutations

To quickly obtain all permutations of a set of the set \{1,2,3\}:

~~~{.python}
sage: permutations([1,2,3])
~~~

### Contour plots

I find 3D surface plots messy and unclear. Here is how to obtain a contour plot of the function: $f: x,y \to 3x-y+2$

~~~{.python}
y = var('y')
f(x,y) = 3 * x + y - ( 2 - y)
contour_plot(f,(0,1),(0,1),colorbar=True,axes_labels=['$x$','$y$'], cmap='summer')
~~~

(There are various options that can be passed to the cmap argument: try `import matplotlib.cm; matplotlib.cm.datad.keys()` to list them)

### Minimizing functions

You might need to minimize the following function $c:\alpha, \beta\to \alpha ^ 3 + 3\beta/2 + \alpha ^ 2 + 2\alpha\beta+\beta^2-2\alpha-2\beta+1$ with the following constraints: $0\leq \alpha \leq 1$ and $0\leq \beta \leq 1$. Here is how to do that in Sage:

~~~{.python}
sage: f = lambda p: p[0] ^ 3 + 3 / 2 * p[1] ^ 2 + p[0] ^ 2 + 2 * p[0] * p[1] + p[1] ^ 2 - 2 * (p[0] + p[1]) + 1
sage: c_1 = lambda p[0]
sage: c_2 = lambda 1 - p[0]
sage: c_3 = lambda p[1]
sage: c_4 = lambda 1 - p[1]
sage: a = minimize_constrained(f, [c_1, c_2, c_3, c_4], [0, 0])
sage: a
~~~

For more details on minimization take a look at [this page](http://www.sagemath.org/doc/reference/numerical/sage/numerical/optimize.html).
