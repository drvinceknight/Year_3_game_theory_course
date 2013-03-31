# OR 3: Chapter 15 - Matching games

## Recap

In the [previous chapter](Chapter_15_Matching_games.html):

- We defined matching games;
- We described the Gale-Shapley algorithm;
- We proved certain results regarding the Gale-Shapley algorithm.

In this Chapter we'll take a look at another type of game.

## Cooperative Games

In cooperative game theory the interest lies with understanding how coalitions form in competitive situations.

### Definition

---

A **characteristic function game** G is given by a pair $(n,v)$ where $n$ is the number of players and $v:2^{[n]}\to\mathbb{R}$ is a **characteristic function** which maps every coalition of players to a payoff.

---

Let's consider the following game:

> "3 players must share a taxi. Here are the costs for each individual journey:
> - Player 1: 6
> - Player 2: 12
> - Player 3: 42
> "

This is illustrated below:

![](images/L16-img01.png)

To construct the characteristic function we first obtain the power set (ie all possible coalitions) $2^{\{1,2,3\}}=\{\emptyset,\{1\},\{2\},\{3\},\{1,2\},\{1,3\},\{2,3\},\Omega\}$ where $\Omega$ denotes the set of all players ($\{1,2,3\}$).

The characteristic function is given below:

$$
v(S)=\begin{cases}
6,&\text{if }S=\{1\}\\
12,&\text{if }S=\{2\}\\
42,&\text{if }S=\{3\}\\
12,&\text{if }S=\{1,2\}\\
42,&\text{if }S=\{1,3\}\\
42,&\text{if }S=\{2,3\}\\
42,&\text{if }S=\{1,2,3\}\\
\end{cases}
$$

### Definition

---

A characteristic function game $G=(n,v)$ is called **monotone** is it satisfies $v(S_2)\geq v(S_1)$ for all $S_1\subseteq S_2$.

---

![](images/L16-img02.png)

Our taxi example is monotone, however the $G=(3,v_1)$ with $v_1$ defined as:

$$
v_1(S)=\begin{cases}
6,&\text{if }S=\{1\}\\
12,&\text{if }S=\{2\}\\
42,&\text{if }S=\{3\}\\
10,&\text{if }S=\{1,2\}\\
42,&\text{if }S=\{1,3\}\\
42,&\text{if }S=\{2,3\}\\
42,&\text{if }S=\{1,2,3\}\\
\end{cases}
$$

is not.

### Definition

---

A characteristic function game $G=(n,v)$ is called **superadditive** if it satisfies $v(S_1\cup S_2)\geq v(S_1)+v(S_2).$

---

![](images/L16-img03.png)

Our taxi example is not superadditive, however the $G=(3,v_2)$ with $v_2$ defined as:

$$
v_2(S)=\begin{cases}
6,&\text{if }S=\{1\}\\
12,&\text{if }S=\{2\}\\
42,&\text{if }S=\{3\}\\
18,&\text{if }S=\{1,2\}\\
48,&\text{if }S=\{1,3\}\\
55,&\text{if }S=\{2,3\}\\
80,&\text{if }S=\{1,2,3\}\\
\end{cases}
$$

is.

## Shapley Value

Solution concept
Required properties
Shapley value
