---
layout     : post
categories : content
title      : Chapter 5 - Nash equilibria in pure strategies
comments   : true
slug       : purestrategyne
---

<div class="video">
    <figure>
    <iframe width="560" height="315" src="//www.youtube.com/embed/yWKlqAo_c-A" frameborder="0" allowfullscreen></iframe>
    </figure>
</div>

## Recap

In the [previous chapter]({{site.baseurl}}/Content/Chapter_04-Best_Responses) we discussed:

- The definition of best responses;
- The connection between dominance and best responses;
- Best responses against mixed strategies.

So far we have been using various tools to loosely discuss 'predicting rational behaviour'. We will now formalise what we mean.

## Nash equilibria

### Definition of Nash equilibria

---

In an \\(N\\) player normal form game. A Nash equilibrium is a strategy profile \\(\tilde s = (\tilde s_1,\tilde s_2,\dots,\tilde s_N)\\) such that:

$$u_i(\tilde s)\geq u_i(\bar s_i,\tilde s_{-i})\text{ for all }i$$

---

This implies that all strategies in the strategy profile \\(\tau\\) are best responses to all the other strategies.

An important interpretation of this definition is that at the Nash equilibria no player has an incentive to deviate from their current strategy.

To find Nash equilibria in 2 player normal form games we can simply check every strategy pair and see whether or not a player has an incentive to deviate.

### Example

Identify Nash equilibria in pure strategies for the following game:

$$
\begin{pmatrix}
(0,3)&(1,2)&(7,8)&(1,4)\\
(2,6)&(1,2)&(3,0)&(1,3)\\
(3,1)&(1,2)&(3,-1)&(5,1)\\
(6,3)&(4,2)&(2,1)&(7,1)
\end{pmatrix}
$$

If we identify all best responses:

$$
\begin{pmatrix}
(0,3)&(1,2)&(\underline{7},\underline{8})&(1,4)\\
(2,\underline{6})&(1,2)&(3,0)&(1,3)\\
(3,1)&(1,\underline{2})&(3,-1)&(5,1)\\
(\underline{6},\underline{3})&(\underline{4},2)&(2,1)&(\underline{7},1)
\end{pmatrix}
$$

We see that we have 2 equilibria in pure strategies: \\((r_1,c_3)\\) and \\((r_4,c_1)\\)

## Duopoly game

We will now consider a particular normal form game attributed to Augustin Cournot.

---

> Suppose that two firms 1 and 2 produce an identical good (ie consumers do not care who makes the good). The firms decide at the same time to produce a certain quantity of goods: \\(q_1,q_2\geq 0\\). All of the good is sold but the price depends on the number of goods:

>$$p=K-q_1-q_2$$

> We also assume that the firms both pay a production cost of \\(k\\) per goods.

What is the Nash equilibria for this game?

---

Firstly let us clarify that this is indeed a normal form game:

1. 2 players;
2. The strategy space is \\(S_1=S_2=\mathbb{R}_{\geq 0}\\)
3. The utilities are given by:

$$u_1(q_1,q_2)=(K-q_1-q_2)q_1-kq_1$$

$$u_2(q_1,q_2)=(K-q_1-q_2)q_2-kq_2$$

Let us now compute the best responses for each firm (we'll in fact only need to do this for one firm given the symmetry of the problem).

$$\frac{du_1}{dq_1}=K-2q_1-q_2-k$$

Setting this to 0 gives the best response \\(q_1^\*=q_1^*(q_2)\\) for firm 1:

$$q_1^*(q_2)=\frac{K-k-q_2}{2}$$

By symmetry we have:

$$q_2^*(q_1)=\frac{K-k-q_1}{2}$$

Recalling the definition of a Nash equilibria we are attempting to find \\((\tilde q_1, \tilde q_2)\\) a pair of best responses. Thus \\(\tilde q_1\\) satisfies:

$$
\begin{cases}
\tilde q_1=q_1^*(\tilde q_2)\\
\tilde q_2=q_1^*(\tilde q_1)
\end{cases}
$$

$$\Leftrightarrow$$

$$
\begin{cases}
\tilde q_1=\frac{K-k-\tilde q_2}{2}\\
\tilde q_2=\frac{K-k-\tilde q_1}{2}
\end{cases}
$$

$$\Leftrightarrow$$

$$\begin{cases}
\tilde q_1=\frac{K-k}{3}\\
\tilde q_2=\frac{K-k}{3}\\
\end{cases}
$$
