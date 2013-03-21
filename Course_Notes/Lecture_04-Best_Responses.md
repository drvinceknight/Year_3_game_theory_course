# OR 3: Lecture 2 - Normal Form Games

## Recap

In the [previous lecture](Lecture_3-Dominance.html) we discussed:

- Predicting rational behaviour using dominated strategies;
- The CKR;

We did discover certain games that did not have any dominated strategies.

## Best response functions

### Definition

---

In an $n$ player normal form game. A strategy $s^*$ for player $i$ is a best response to some strategy profile $s_{-i}$ if and only if $u_i(s^*,s_{-i})\geq u_{i}(s,s_{-i})$ for all $s\in S_i$.

---

We can now start to predict rational outcomes in pure strategies by identifying all best responses to a strategy.

$$\begin{pmatrix}
(1,3)&(4,2)&(2,2)\\
(4,0)&(0,3)&(4,1)\\
(2,5)&(3,4)&(5,6)
\end{pmatrix}
$$

We will underline the best responses for each strategy giving:

$$\begin{pmatrix}
(1,\underline{3})&(\underline{4},2)&(2,2)\\
(\underline{4},0)&(0,\underline{3})&(4,1)\\
(2,5)&(3,4)&(\underline{5},\underline{6})
\end{pmatrix}
$$

We see that $(r_1,s_1)$ represented a pair of best responses. What can we say about the long term behaviour of this game?

## Connection between best responses and dominance

## Best responses against mixed strategies

We can identify best responses against mixed strategies. Let us take a look at the matching pennies game:

$$\begin{pmatrix}
(1,-1)&(-1,1)\\
(-1,1)&(1,-1)
\end{pmatrix}$$

If we assume that player 2 plays a mixed strategy $\sigma_2=(x,1-x)$ we have:

$$u_1(r_1,\sigma_2)=1-2x$$

and

$$u_1(r_2,\sigma_2)=2x-1$$

![](plots/L04-plot01.png)

1. If $x<1/2$ then $r_1$ is a best response for player 1.
2. If $x>1/2$ then $r_1$ is a best response for player 1.
3. If $x=1/2$ then player 1 is indifferent.

Let us repeat this exercise for the battle of the sexes game.

$$\begin{pmatrix}
(3,2)&(0,0)\\
(1,1)&(2,3)
\end{pmatrix}$$

If we assume that player 2 plays a mixed strategy $\sigma_2=(x,1-x)$ we have:

$$u_1(r_1,\sigma_2)=3x$$

and

$$u_1(r_2,\sigma_2)=2-x$$

![](plots/L04-plot02.png)

1. If $x<1/2$ then $r_2$ is a best response for player 1.
2. If $x>1/2$ then $r_1$ is a best response for player 1.
3. If $x=1/2$ then player 1 is indifferent.
