# OR 3: Chapter 1
## Introduction

### What is game theory?

#### Coffee house example
Let us consider the very simple situation where **you** decide where to meet your **friends**. You have some information about their behaviour:

- 20% of the time they go to coffee house A;
- 80% of the time they go to coffee house B.

If you wanted to maximise your chance of meeting your friends: what should you do?

![A simple decision tree](images/L01-img01.png)

The above tree shows that if **you** were to choose your location first it would be in your interest of choosing coffee house B. This gives you an 80% chance of being in the same location as your **friends**.

In general these sorts of decisions are not at the mercy of chance. **You** would probably choose to go to coffee house A or B and simply let your friends know where you are so that they could make an informed decision. This consecutive making of decisions is a type of game.

![A simple decision tree](images/L01-img02.png)

In this game the outcome (whether or not your friends and you have a coffee together) depends on the actions of all the players.

#### 2/3rds of the average game

Let us consider another type of game:

1. Every player must write a whole number between 0 and 100 on the provided sheet.

2. The winner of the game will be the player whose number is closest to 2/3rd of the average of all the numbers written by all the players.

### Extensive Form Games

#### Description

We will now return to the tree diagrams drawn previously. In game theory trees are used to represent a type of game called: **extensive form games**.

**Definition**

An $n$ player extensive form game **of complete information** consists of:

1. A finite set of $n$ players;
2. A rooted tree (which we refer to as the _game tree_);
3. Each leaf of the tree has an $n$-tuple of payoffs;

**Example**

Let's consider the following game.

> Two friends must decide what movie to watch at the cinema. Bob would like to watch a comedy and Celine would like to watch a sports movie. Importantly they would both rather spend their evening together then apart.

Represents the game as well as the utilities of Bob and Celine.

![Bob and Celine](images/L01-img03.png)

If we assume that this is the order with which decisions take place it should be relatively straightforward to predict what will happen:

1. Bob sees that no matter what he picks Celine will pick the same type of movie;
2. Bob can thus pick a comedy to ensure that he gets a slightly higher utility.

(This is actually using a process called **backward induction** but we'll see that properly a bit later.)

Of course we can simply represent this game in a different way (remember that in the above description we did not mention who would be making the initial decision.

![Celine and Bob](images/L01-img04.png)

In this case is should again be relatively straightforward to predict what will happen:

1. Celine sees that no matter what he picks Bob will pick the same type of movie;
2. Celine can thus pick a comedy to ensure that he gets a slightly higher utility.

The main assumption we are making here is concerned with the amount of information available to both players at different points of the game. In both cases we have here assumed that the information available at nodes **b** and **c** is different. This is not always the case.

#### Information sets


**Definition**

Two nodes of a game tree are said to be part of the same information set if the player at that node cannot differentiate between them.

We represent nodes being part of the same information set using dashed line. In our example with Celine and Bob if both players must decide on a movie without knowing what the other will do we see that node **b** and **c** now have the same information set.

![Celine and Bob with Information Set](images/L01-img05.png)

It is now a lot more difficult to try and predict the outcome of this situation.
