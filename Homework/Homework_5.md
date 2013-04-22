# Homework sheet 5 - Matching games, cooperative games and routing games

1. Obtain stable suitor optimal and reviewer optimal matchings for the following matching games:

---

![Matching game 1](images/E05-img01.png)

---

![Matching game 2](images/E05-img02.png)

---

![Matching game 3](images/E05-img03.png)

---

![Matching game 4](images/E05-img04.png)

---

2. Given a stable matching with $n$ suitors and reviewers:

i. Is it possible to find three pairs such that if the matching among them is changed, each suitor will be matched to a reviewer that he/she prefers and each reviewer will be matched to a suitor that he/she prefers?
ii. Generalize this conclusion to a set of $k$ pairs, for every $4\leq k\leq n$.

3. For the following cooperative games:

i. Verify if the game is monotonic.
ii. Verify if the game is super additive.
iii. Obtain the Shapley value.

$$
v_1(C)=\begin{cases}
5,&\text{if }C=\{1\}\\
3,&\text{if }C=\{2\}\\
2,&\text{if }C=\{3\}\\
12,&\text{if }C=\{1,2\}\\
5,&\text{if }C=\{1,3\}\\
4,&\text{if }C=\{2,3\}\\
13,&\text{if }C=\{1,2,3\}\\
\end{cases}
$$

$$
v_2(C)=\begin{cases}
6,&\text{if }C=\{1\}\\
0,&\text{if }C=\{2\}\\
5,&\text{if }C=\{1,2\}\\
\end{cases}
$$

$$
v_4(C)=\begin{cases}
6,&\text{if }C=\{1\}\\
6,&\text{if }C=\{2\}\\
13,&\text{if }C=\{3\}\\
6,&\text{if }C=\{1,2\}\\
13,&\text{if }C=\{1,3\}\\
13,&\text{if }C=\{2,3\}\\
26,&\text{if }C=\{1,2,3\}\\
\end{cases}
$$

$$
v_4(C)=\begin{cases}
6,&\text{if }C=\{1\}\\
7,&\text{if }C=\{2\}\\
0,&\text{if }C=\{3\}\\
8,&\text{if }C=\{4\}\\
7,&\text{if }C=\{1,2\}\\
6,&\text{if }C=\{1,3\}\\
12,&\text{if }C=\{1,4\}\\
7,&\text{if }C=\{2,3\}\\
12,&\text{if }C=\{2,4\}\\
8&\text{if }C=\{3,4\}\\
7,&\text{if }C=\{1,2,3\}\\
24,&\text{if }C=\{1,2,4\}\\
12,&\text{if }C=\{1,3,4\}\\
12,&\text{if }C=\{2,3,4\}\\
25,&\text{if }C=\{1,2,3,4\}\\
\end{cases}
$$

4. Prove that the Shapley value has the following properties:

- Efficiency
- Null player
- Symmetry
- Additivity

Note that this does not prove that the Shapley value is the only vector that has those properties (it in fact is though).

5. Calculate the Nash flow and the optimal flow for the routing games shown\text{ in Figures \ref{E05-img05} and \ref{E05-img06}}.

![Routing game 1\label{E05-img05}](images/E05-img05.png)
![Routing game 2\label{E05-img06}](images/E05-img06.png)

6. For a routing game the 'Price of Anarchy' is defined as:

$$\text{PoA}=\frac{C(\tilde f)}{C(f^*)}$$

For the game shown\text{ in Figure \ref{E05-img07}} (a generalisation of "Pigou's example") obtain the PoA as a function of $\alpha$.

![A generalization of Pigou's example\label{E05-img07}](images/E05-img07.png)

Now obtain the PoA for the game shown\text{ in Figure \ref{E05-img08}} as a function of $\Lambda, \alpha$ and $\beta$. For what value of $\Lambda$ is the PoA at it's maximum?

![A further generalization of Pigou's example\label{E05-img08}](images/E05-img08.png)
