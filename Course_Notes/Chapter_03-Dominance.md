# OR 3: Chapter 2 - Normal Form Games

## Recap

In the [previous lecture](Chapter_03-Normal_Form_Games.html) we discussed:

- Normal form games;
- Mixed strategies and expected utilities.

We spent some time talking about predicting rational behaviour in the above games but we will now look a particular tool in a formal way.

## Dominant strategies

In certain games it is evident that certain strategies should never be used by a rational player. To formalise this we need a couple of definitions.

### Definition

---

In an $n$ player normal form game when considering player $i$ we denotes by $s_{-i}$ a fixed strategy profile for all other players in the game.

---

For example in a 3 player game where $S_i=\{A,B\}$ for all $i$ a valid strategy profile is $s=(A,A,B)$ while $s_{-2}=(A,B)$ denotes the incomplete strategy profile where player 1 and 3 are playing A and B (respectively).

This notation now allows us to define an important notion in game theory.

### Definition


---

In an $n$ player normal form game. A pure strategy $s_i\in S_i$ is said to be **strictly dominated** if there is a strategy (pure or mixed) $\sigma_i\in \Delta S_i$ such that $u_i(\sigma_i,s_{-i})>u_{i}(s_i,s_{-i})$ for all $s_{-i}\in S_{-i}$ of the other players.

---

When attempting to predict rational behaviour we can elimate dominated strategies.

$$\begin{pmatrix}
(0,1)&(3,5)\\
(5,10)&(-1,34)
\end{pmatrix}$$

If we let $S_1=\{r_1, r_2\}$ and $S_2=\{s_1, s_2\}$ we see that:

$$u_2(s_2,r_1)>u_2(s_1,r_1)$$
and
$$u_2(s_2,r_2)>u_2(s_1,r_2)$$

so $s_1$ is a strictly dominated strategy for player 2. As such we can elimante it from the game when attempting to predict rational behaviour.  This gives the following game:

$$\begin{pmatrix}
(3,5)\\
(-1,34)
\end{pmatrix}$$

At this point it is straightforward to see that $r_2$ is a strictly dominated strategy for player 1 giving the following predicted strategy profile: $s=(r_1,s_2)$.

### Definition

---

In an $n$ player normal form game. A pure strategy $s_i\in S_i$ is said to be **weakly dominated** if there is a strategy (pure or mixed) $\sigma_i\in \Delta S_i$ such that $u_i(\sigma_i,s_{-i})\leq u_{i}(s_i,s_{-i})$ for all $s_{-i}\in S_{-i}$ of the other players and there exists a strategy profile $\bar s\in S_{-i}$ such that $u_i(\sigma_i,\bar s)< u_{i}(s_i,s_{-i})$ .

---

We can once again predict rational behaviour by eliminating weakly dominated strategies.

As an example consider the following two player game:

$$\begin{pmatrix}
(3,3)&(2,2)\\
(2,1)&(2,1)
\end{pmatrix}$$

Using the same convention as before for player 2, $s_1$ weakly dominates $s_2$ and for player 1, $r_1$ weakly dominates $r_2$ giving the following predicted strategy profile $(r_1,s_1)$.

## Common knowledge of rationality

An important aspect of game theory and the tool that we have in fact been using so far is to assume that players are rational. However we can (and need) to go further:

- The players are rational;
- The players all know that the other players are rational;
- The players all know that the other players know that they are rationals;
- ...

This chain of assumptions is called **Common knowledge of rationality** (CKR). By applying the CKR assumption we can attempt to predict rational behaviour through the iterated elimination of dominated strategies (as we have been doing above).

### Example

Les us try to predict rational behaviour in the following game using iterated elimination of dominated strategies:

$$\begin{pmatrix}
(1,0)&(1,2)&(0,1)\\
(0,3)&(0,1)&(2,0)
\end{pmatrix}$$

**Initially** player 1 has no dominated strategies. For player 2, $s_3$ is dominated by $s_2$. Now $r_2$ is dominated by $r_1$ for player 1. Finally, $s_1$ is dominated by $s_2$. Thus $(r_1,s_2)$ is a predicted rational outcome.

### Example

Les us try to predict rational behaviour in the following game using iterated elimination of dominated strategies:

$$\begin{pmatrix}
(10,1)&(5,1)&(4,-2)\\
(10,1)&(5,0)&(1,1)
\end{pmatrix}$$

- $r_1$ weakly dominated by $r_2$
- $s_1$ strictly dominated by $s_3$
- $s_1$ weakly dominated by $s_2$

Thus $(r_1,s_1)$ is a predicted rational outcome.


## Not all games can be solved using dominance

Consider the following two games:

$$\begin{pmatrix}
(3,2)&(0,0)\\
(1,1)&(2,3)
\end{pmatrix}$$

$$\begin{pmatrix}
(1,3)&(4,2)&(2,2)\\
(4,0)&(0,3)&(4,1)\\
(2,5)&(3,4)&(5,6)
\end{pmatrix}
$$

Why can't we predict rational behaviour using dominance?
