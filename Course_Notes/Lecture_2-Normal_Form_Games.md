# OR 3: Lecture 2 - Normal Form Games

## Recap

In the [previous lecture](Lecture_1-Introduction.html) we discussed:

- Interactive decision making;
- Normal form games;
- Normal form games and representing information sets.

We did this looking at a game called "the battle of the sexes":

![Celine and Bob with Information Set](images/L01-img05.png)

Can we think of a better way of representing this game?

## Normal form games

One other representation for a game is called the **normal form**.

### Definition

---

A $n$ player **normal form game** consists of:

1. A finite set of $n$ players;
2. Strategy spaces for the players: $S_1, S_2, S_3, \dots S_n$;
3. Payoff functions for the players: $u_i:S_{1}\times S_2\dots\times S_n\to \mathbb{R}$

---

The convention used in this course (unless otherwise stated) is that all players aim to choose from their strategies in such a way as to maximise their utilities.

A natural way of representing a two player normal form game is using a **bi-matrix**. If we assume that $S_1=\{r_i\;|\;1\leq i\leq m \}$ and $S_2=\{s_j\;|\;1\leq j\leq n \}$ then the following is a **bi-matrix** representation of the game considered:

![A bi matrix](images/L02-img01.png)

### Some examples

#### The battle of the sexes

>This is the game we've been looking at between Bob and Celine:

$$
\begin{pmatrix}
(3,2)&(0,0)\\
(1,1)&(2,3)
\end{pmatrix}
$$

#### Prisoners' Dilemma

>Suppose ...

$$
\begin{pmatrix}
(2,2)&(0,3)\\
(3,0)&(1,1)
\end{pmatrix}
$$

#### Hawk-Dove/Chicken

> Suppose...

$$
\begin{pmatrix}
(0,0)&(3,1)\\
(1,3)&(2,2)
\end{pmatrix}
$$

#### Coordination

> Suppose...

$$
\begin{pmatrix}
(1,1)&(0,0)\\
(0,0)&(1,1)
\end{pmatrix}
$$

#### Pareto Coordination

> Suppose...

$$
\begin{pmatrix}
(2,2)&(0,0)\\
(0,0)&(1,1)
\end{pmatrix}
$$

#### Pigs

> Suppose...

$$
\begin{pmatrix}
(4,2)&(2,3)\\
(6,-1)&(0,0)
\end{pmatrix}
$$

## Strategies

Discuss pure strategies
Discuss mixed strategies
