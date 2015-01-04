---
layout     : post
categories : content
title      : Chapter 7 - Extensive form games and backwards induction
comments   : true
slug       : extensiveformgames
---

## Recap

In the [previous chapter]({{site.baseurl}}/Content/Chapter_06-Nash_Equilibria_in_mixed_strategies)

- We completed our look at normal form games;
- Investigated using best responses to identify Nash equilibria in mixed strategies;
- Proved the Equality of Payoffs theorem which allows us to compute the Nash equilibria for a game.

In this Chapter we start to look at extensive form games in more detail.

## Extensive form games

If we recall Chapter 1 we have seen how to represent extensive form games as a tree.

![Bob and Celine. \label{L01-img03}](images/L01-img03.png)

We will now consider the properties that define an extensive form game game tree:

1. Every node is a successor of the (unique) initial node.

![A tree with two initial nodes.\label{L07-img01}](images/L07-img01.png)

2. Every node apart from the initial node has exactly one predecessor. The initial node has no predecessor.

![A tree with node c having multiple predecessors. \label{L07-img02}](images/L07-img02.png)

3. All edges extending from the same node have different action labels.

![Nodes with same action labels.\label{L07-img03}](images/L07-img03.png)

4. Each information set contains decision nodes for one player.

![Information sets with different action labels.\label{L07-img04}](images/L07-img04.png)

5. All nodes in a given information set must have the same number of successors (with the same action labels on the corresponding edges).

![Information set with different number of action edges. \label{L07-img05}](images/L07-img05.png)

6. We will only consider games with "perfect recall", ie we assume that players remember their own past actions as well as other past events.

![A game without perfect recall.\label{L07-img06}](images/L07-img06.png)

7. If a player's action is not a discrete set we can represent this as shown.

![A game tree with continuous strategy set.\label{L07-img07}](images/L07-img07.png)

As an example consider the following game (sometimes referred to as "ultimatum bargaining"):

> Consider two individuals: a seller and a buyer. A seller can set a price \\(p\\) for a particular object that has value \\(K\\) to the buyer and no value to the seller. Once the sellers sets the price the buyer can choose whether or not to pay the price. If the buyer chooses to not pay the price then both players get a payoff of 0.

We can represent this.

![The seller buyer game.\label{L07-img08}](images/L07-img08.png)

How we can we analyse normal form games?

## Backwards induction

To analyse such games we assume that players not only attempt to optimize their overall utility but optimize their utility conditional on any information set.

### Definition of sequential rationality

---

**Sequential rationality:** An optimal strategy for a player should maximise that player's expected payoff, conditional on every information set at which that player has a decision.

---

With this notion in mind we can now define an analysis technique for extensive form games:

### Definition of backward induction

---

**Backward induction:** This is the process of analysing a game from back to front. At each information set we remove strategies that are dominated.

---

### Example

Let us consider the game shown.

![Running example for backward induction.\label{L07-img09}](images/L07-img09.png)

We see that at node \\((d)\\) that Z is a dominated strategy. So that the game reduces to as shown.

![Running example step 1.\label{L07-img10}](images/L07-img10.png)

Player 1s strategy profile is (Y) (we will discuss strategy profiles for extensive form games more formally in the next chapter). At node \\((c)\\) A is a dominated strategy so that the game reduces as shown.

![Running example step 2.\label{L07-img11}](images/L07-img11.png)

Player 2s strategy profile is (B). At node \\((b)\\) D is a dominated strategy so that the game reduces as shown.

![Running example step 3.\label{L07-img12}](images/L07-img12.png)

Player 2s strategy profile is thus (C,B) and finally strategy W is dominated for player 1 whose strategy profile is (X,Y).

**This outcome is in fact a Nash equilibria!** Recalling the original tree neither player has an incentive to move.

### Theorem of existence of Nash equilibrium in games of perfect information.

---

Every finite game with perfect information has a Nash equilibrium in pure strategies. Backward induction identifies an equilibrium.

---

### Proof

---

Recalling the properties of **sequential rationality** we see that no player will have an incentive to deviate from the strategy profile found through backward induction. Secondly ever finite game with perfect information can be solved using backward inductions which gives the result.

---

## Stackelberg game

Let us consider the Cournot duopoly game of Chapter 5. Recall:

> Suppose that two firms 1 and 2 produce an identical good (ie consumers do not care who makes the good). The firms decide at the same time to produce a certain quantity of goods: \\(q_1,q_2\geq 0\\). All of the good is sold but the price depends on the number of goods:

>$$p=K-q_1-q_2$$

> We also assume that the firms both pay a production cost of \\(k\\) per bricks.

However we will modify this to assume that there is a leader and a follower, ie **the firms do not decide at the same time**. This game is called a Stackelberg leader follower game.

Let us represent this as a normal form game.

![A Stackelberg leader follower game.\label{L07-img13}](images/L07-img13.png)

We use backward induction to identify the Nash equilibria. The dominant strategy for the follower is:

$$q_2^*(q_1)=\frac{K-k-q_1}{2}$$

The game thus reduces as shown.

![A step of backward induction in the Stackelberg game.\label{L07-img14}](images/L07-img14.png)

The leader thus needs to maximise:

$$u_1(q_1)=(K-q_1-\frac{K-k-q_1}{2})q_1-kq_1=(\frac{K-q_1+k}{2})q_1-kq_1$$

Differentiating and equating to 0 gives:

$$q_1^*=\frac{K-k}{2}$$
which in turn gives:
$$q_2^*=\frac{K-k}{4}$$

The total amount of goods produced is \\(\frac{3(K-k)}{4}\\) whereas in the Cournot game the total amount of good produced was \\(\frac{2(K-k)}{3}\\). Thus more goods are produced in the Stackelberg game.
