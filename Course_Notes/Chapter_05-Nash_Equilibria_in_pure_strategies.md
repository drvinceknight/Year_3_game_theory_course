# OR 3: Lecture 5 - Nash equilibria in pure strategies

## Recap

In the [previous lecture](Lecture_04-Best_RLecture_04-Best_RLecture_04-Best_RLecture_04-Best_Responses.html) we discussed:

- The definition of best responses;
- The connection between dominance and best responses;
- Best responses against mixed strategies.

So far we have been using various tools to loosely discuss 'predicting rational behaviour'. We will now formalise what we mean.

## Nash equilibria

---

In an $n$ player normal form game. A Nash equilibrium in **pure strategies** is a strategy profile $\tilde s$ such that:

$$u_i(\tilde s)\geq u_i(\bar s_i,\tilde s_{-i})\text{ for all }i$$

---

This implies that all strategies in the strategy profile $s$ are best responses to all the other strategies.

An important interpretation of this definition is that at the Nash equilibria no player has an incentive to deviate from their current strategy.

To find Nash equilibria in 2 player normal form games we can simply check every strategy pair and see whether or not a player has an incentive to deviate.

## Example

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

We see that we have 2 equilibria in pure strategies: $(r_1,s_3)$ and $(r_4,s_1)$

## Duopoly games
