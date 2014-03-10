# OR 3: Chapter 12 - Nash equilibrium and Evolutionary stable strategies

## Recap

In the [previous chapter](Chapter_11_Population_Games_and_Evolutionary_stable_strategies.md):

- We considered population games;
- We proved a result concerning a necessary condition for a population to be evolutionary stable;
- We defined Evolutionary stable strategies and looked at an example in a game against the field.

In this chapter we'll take a look at pairwise contest games and look at the connection between Nash equilibrium and ESS.

## Pairwise contest games

In a population game when considering a pairwise contest game we assume that individuals are randomly matched. The utilities then depend just on what the individuals do:

$$u(\sigma,\chi)=\sum_{s\in S}\sum_{s'\in S}\sigma(s)\chi(s')u(s,s')$$

As an example we're going to consider the "Hawk-Dove" game: a model of predator interaction. We have $S=\{H,D\}$ were:

- $H$: Hawk represents being "aggressive";
- $D$: Dove represents not being "aggressive".

At various times individuals come in to contact and must choose to act like a Hawk or like Dove over the sharing of some resource of value $v$. We assume that:

- If a Dove and Hawk meet the Hawk takes the resources;
- If two Doves meet they share the resources;
- If two Hawks meet there is a fight over the resources (with an equal chance of winning) and the winner takes the resources while the loser pays a cost $c>v$.

If we assume that $\sigma=(\omega,1-\omega)$ and $\chi=(h,1-h)$ the above gives:

$$u(\sigma,\chi)=\omega(1-h)v+(1-\omega)(1- h) \frac{v}{2}+\omega h \frac{v-c}{2} $$

It is immediate to note that no pure strategy ESS exists. In a population of Doves ($h=0$):

$$u(\sigma,(0,1))=\omega v+(1-\omega) \frac{v}{2}=(1+\omega)\frac{v}{2}$$

thus the best response is setting $\omega=1$ i.e. to play Hawk.

In a population of Hawks ($h=1$):

$$u(\sigma,(1,0))=\omega h \frac{v-c}{2} $$

thus the best response is setting $\omega=0$ i.e. to play Dove.

So we will now try and find out if there is a mixed-strategy ESS: $\sigma^*=(\omega^*,1-\omega^*)$. For $\sigma^*$ to be an ESS it must be a best response to the population it generates $\chi^*=(\omega^*,1-\omega^*)$. In this population the payoff to an arbitrary strategy $\sigma$ is:

$$u(\sigma,\chi^*)=(1-\omega^*)\frac{v}{2}+\left(\frac{v}{2}-\omega^*\right)\frac{\omega c}{2}$$

- If $\omega^*<v/c$ then a best response is $\omega=1$;
- If $\omega^*>v/c$ then a best response is $\omega=0$;
- If $\omega^*=v/c$ then there is indifference.

So the only candidate for an ESS is $\sigma^*=\left(v/c,1-v/c\right)$. We now need to show that $u(\sigma^*,\chi_{\epsilon})>u(\sigma,\chi_{\epsilon})$.

We have:

$$x_\epsilon=(v/c+\epsilon(\omega-v/c),1-v/c+\epsilon(\omega-v/c)$$

and:

$$\begin{aligned}
u(\sigma^*,\chi_{\epsilon})=\frac{v}{c}\left(\frac{v}{c}+\epsilon\left(\omega-\frac{v}{c}\right)\right)\frac{v-c}{2}+&\frac{v}{c}\left(1-\frac{v}{c}+\epsilon\left(\frac{v}{c}-\omega\right)\right)v\\
+&\left(1-\frac{v}{c}\right)\left(1-\frac{v}{c}+\epsilon\left(\frac{v}{c}-\omega\right)\right)\frac{v}{2}
\end{aligned}$$

$$\begin{aligned}
u(\sigma,x_{\epsilon})=\omega\left(\frac{v}{c}+\epsilon\left(\omega-\frac{v}{c}\right)\right)\frac{v-c}{2}+&\omega\left(1-\frac{v}{c}+\epsilon\left(\frac{v}{c}-\omega\right)\right)v\\
+&\left(1-\omega\right)\left(1-\frac{v}{c}+\epsilon\left(\frac{v}{c}-\omega\right)\right)\frac{v}{2}
\end{aligned}$$

This gives:

$$u(\sigma^*,\chi_{\epsilon})-u(\sigma,x_{\epsilon})=\frac{\epsilon c}{2}\left(\frac{v}{c}-\omega\right)^2>0$$

which proves that $\sigma^*$ is an ESS.

We will now take a closer look the connection between ESS and Nash equilibria.

## ESS and Nash equilibria

When considering pairwise contest population games there is a natural way to associate a normal form game.

### Definition

---

The **associated two player game** for a pairwise contest population game is the normal form game with payoffs given by: $u_1(s,s')=u(s,s')=u_2(s',s)$.

---

Note that the resulting game is symmetric (other contexts would give non symmetric games but we won't consider them here).

Using this we have the powerful result:

### Theorem relating an evolutionary stable strategy to the Nash equilibrium of the associated game

---

If $\sigma^*$ is an ESS in a pairwise contest population game then for all $\sigma\ne\sigma^*$:

1. $u(\sigma^*,\sigma^*)>u(\sigma,\sigma^*)$
OR
2. $u(\sigma^*,\sigma^*)=u(\sigma,\sigma^*)$ and $u(\sigma^*,\sigma)>u(\sigma,\sigma)$

Conversely, if either (1) or (2) holds for all $\sigma\ne\sigma^*$ in a two player normal form game then $\sigma$ is an ESS.

---

### Proof

---

If $\sigma^*$ is an ESS, then by definition:

$$u(\sigma^*,\chi_{\epsilon})>u(\sigma,\chi_{\epsilon})$$

which corresponds to:

$$(1-\epsilon)u(\sigma^*,\sigma^*)+\epsilon u(\sigma^*,\sigma)>(1-\epsilon)u(\sigma,\sigma^*)+\epsilon u(\sigma,\sigma)$$

- If condition 1 of the theorem holds then the above inequality can be satisfied for $\epsilon$ sufficiently small. If condition 2 holds then the inequality is satisfied.
- Conversely:

    - If $u(\sigma^*,\sigma^*)<u(\sigma,\sigma^*)$ then we can find $\epsilon$ sufficiently small such that the inequality is violated. Thus the inequality implies $u(\sigma^*,\sigma^*)\geq u(\sigma,\sigma^*)$.

    - If $u(\sigma^*,\sigma^*)= u(\sigma,\sigma^*)$ then $u(\sigma^*,\sigma)> u(\sigma,\sigma)$ as required.

This result gives us an efficient way of computing ESS. The first condition is in fact almost a condition for Nash Equilibrium (with a strict inequality), the second is thus a stronger condition that removes certain Nash equilibria from consideration. This becomes particularly relevant when considering Nash equilibrium in mixed strategies.

To find ESS in a pairwise context population game we:

1. Write down the associated two-player game;
2. Identify all symmetric Nash equilibria of the game;
3. Test the Nash equilibrium against the two conditions of the above Theorem.


### Example

Let us consider the Hawk-Dove game. The associated two-player game is:

$$
\begin{pmatrix}
\left(\frac{v-c}{2},\frac{v-c}{2}\right),(v,0)\\
(0,v),\left(\frac{v}{2},\frac{v}{2}\right)\\
\end{pmatrix}
$$

Recalling that we have $v<c$ so we can use the Equality of payoffs theorem to obtain the Nash equilibrium:

$$
\begin{aligned}
u_2(\sigma^*,H)&= u_2(\sigma^*,D)\\
q^*&=\frac{v}{c}
\end{aligned}
$$

Thus we will test $\sigma^*=(\frac{v}{c},1-\frac{v}{c})$ using the above theorem.

**Importantly** from the equality of payoffs theorem we immediately see that condition 1 does not hold as $u(\sigma^*,\sigma^*)=u(\sigma^*,H)=u(\sigma^*,D)$. Thus we need to prove that:

$$u(\sigma^*,\sigma)>u(\sigma,\sigma)$$

We have:

$$u(\sigma^*,\sigma)=\frac{v}{c}\omega\frac{v-c}{2}+\frac{v}{c}(1-\omega)v+(1-\frac{v}{c})(1-\omega)\frac{v}{c}$$
$$u(\sigma,\sigma)=\omega^2\frac{v-c}{2}+\omega(1-\omega)v+(1-\omega)^2\frac{v}{c}$$

After some algebra:

$$u(\sigma^*,\sigma)-u(\sigma,\sigma)=\frac{c}{2}(\frac{v}{c}-\omega)^2>0$$

Giving the required result.
