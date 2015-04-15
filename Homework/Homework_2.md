---
layout     : post
categories : homework
title      : Homework 2 - Nash equilibrium in normal form games
comments   : true
slug       : normalformgamesnashequilibria-hw
---

1. Compute the Nash equilibrium (if they exist) in pure strategies for the following games:

    $$\begin{pmatrix}
    (5,3)&(70,-1)&(4,2)\\
    (6,7)&(71,2)&(2,1)
    \end{pmatrix}$$

    $$\begin{pmatrix}
    (6,7)&(2,1)&(4,6)\\
    (0,4)&(3,8)&(2,3)\\
    (1,2)&(1,5)&(1,1)\\
    \end{pmatrix}$$

    $$\begin{pmatrix}
    (\pi,e)&(1-\pi,\sqrt(e))\\
    (\sqrt(2),1/e)&(2,1)
    \end{pmatrix}$$


2. For what values of \\(\alpha\\) does a Nash equilibrium exist in pure strategies for the following game:

    $$\begin{pmatrix}
    (3,5)&(2-\alpha,\alpha)\\
    (4\alpha,6)&(\alpha,\alpha^2)
    \end{pmatrix}$$

3. Consider the following game:

    Suppose two vendors (of an identical product) must choose their location along a busy street. It is anticipated that their profit is directly related to their position on the street.

    If we allow their positions to be represented by a points \\(x_1, x_2\\) on the \\([0,1]_{\mathbb{R}}\\) line segment then we have:

    $$u_1(x_1,x_2)=\begin{cases}x_1+(x_2-x_1)/2,&\text{if }x_1\leq x_2\\
    1-x_1+(x_2-x_1)/2,&\text{otherwise}
    \end{cases}$$
    and
    $$u_2(x_1,x_2)=\begin{cases}x_2+(x_2-x_1)/2,&\text{if }x_2\leq x_1\\
    1-x_2+(x_2-x_1)/2,&\text{otherwise}
    \end{cases}$$

    By considering best responses of each player, identify the Nash equilibrium for the game.

4. Consider the following game:

    $$\begin{pmatrix}
    (3,2)&(6,5)\\
    (1,4)&(2,3)
    \end{pmatrix}$$


    Plot the expected utilities for each player against mixed strategies and use this to obtain the Nash Equilibria.

5. Assume a soccer player (player 1) is taking a penalty kick and has the option of shooting left or right: \\(S_1=\\{\text{SL},\text{SR}\\}\\). A goalie (player 2) can either dive left or right: \\(S_2=\\{\text{DL}, \text{DR}\\}\\). The chances of a goal being scored are given below:

    $$\begin{pmatrix}
    .8&.15\\
    .2&.95
    \end{pmatrix}$$

    1. Assume the utility to player 1 if the probability of scoring and the utility to player 2 the probability of a goal not being scored. What is the Nash equilibrium for this game?

    2. Assume that player 1 now has a further strategy available: to shoot in the middle: \\(S_1=\\{\text{SL},\text{SM}, \text{SR}\\}\\) the probabilities of a goal being scored are now given:

    $$\begin{pmatrix}
    .8&.15\\
    .5&.5\\
    .2&.95
    \end{pmatrix}$$

    Obtain the new Nash equilibrium for the game.

6. In the notes the following theorem is given:

    ---

    Every normal form game with a ﬁnite number of pure strategies for each player, has at least one Nash equilibrium.

    ---

    Prove the theorem for 2 player games with \\(\|S_1\|=\|S_2\|=2\\). I.e. prove the above result in the special case of \\(2\times 2\\) games.

[Solution available]({{site.baseurl}}/Homework/Solution_2)
