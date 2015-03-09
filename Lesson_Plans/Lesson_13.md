# OR 3: Lesson Plan Lecture 13
## Nash equilibrium and Evolutionary stable strategies

### Aims of lecture

At the end of this lecture students will be able to:

- Calculate ESS in certain Pairwaise contest games;
- Describe the connection between Nash Equilibria and ESS;

### Timeline

#### Before the lecture

- Online set of games? Quiz??

#### During the lecture

Build a road.
Get two players to turn around and decide side of road: they are not allowed to speak.
Show side of road: walk to each other.
Repeat until we get equilibrium.

Show some of code I showed in Namibia (and also code for RPSLS).

Discuss how this game corresponds to:

[1,1],[-1,-1]
[-1,-1],[1,1]

We have: S={L, R}, sigma=(mu, 1-mu) and chi=(x,1-x).

u(sigma, chi) = 1 * mu * x + 1 * (1-mu) * (1-x) - 1 * x * (1-mu) - 1 * (1-x) * mu
                  = 1 - 2 * x - 2 * mu + 4 * mu * x
                  = (2 * x - 1) * (2 * mu - 1)

What are potential ESS?

- If everyone goes left: chi=(1,0)

u(sigma, chi) = (2 * mu - 1 )

best response is mu = 1, so potential is mu^*=1

- If everyone goes right: chi=(0,1)

u(sigma, chi) = (1 - 2 * mu )

best response is mu = 0, so potential is mu^*=0

- What about mixed? sigma_m = (mu, 1-mu)

u(L, chi) = u(R, chi)
     2x-1 = 1-2x

     this implies x = 1/2, so potential is mu^*=1/2

Now let us check evolutionary stability of these potential ones:

sigma^* = (mu^*, 1-mu^*) and sigma=(mu, 1-mu)

chi_epsilon = sigma^* + epsilon(sigma - sigma^*)
            = (mu^*+epsilon(mu-mu^*), 1 - mu^* - epsilon(mu-mu^*))

To check stability we will consider:

delta = u(sigma^*, chi_epsilon) - u(sigma,chi_epsilon)
      = mu^*u(L,chi_epsilon)+(1-mu^*)u(R,chi_epsilon - muu(L,chi_epsilon)+(1-mu)u(R,chi_epsilon
      = u(L, chi_epsilon)(mu^*-mu) + u(R, chi_epsilon)(mu-mu^*)
      = (mu^*-mu)(u(L,chi_epsilon)-u(R,chi_epsilon))

[The above always works right?]

Plugging our numbers in:

delta = (mu^*-mu)(2x_epsilon-1-1+2x_epsilon)
      = (mu^*-mu)(4x_epsilon - 2)

Now, we just plug in the potential values:

- mu^*=1

    delta = (1-mu)(-2+4+4epsilon(mu-1))
          = (1-mu)(2+4epsilon(mu-1))

          which is positive for small enough epsilon.

- mu^*=0

    delta = -mu(-2+4epsilon)

          which is positive for small enough epsilon.

- mu^*=1/2

    delta = (1/2-mu)4epsilon(mu-1/2)

    which is negative for all mu, epsilon


***
Now look at theorem
***

In our case:

3 NEs

2 pures match 1)

1 mixed:

u(sigma^*, sigma^*) = u(sigma^*, sigma) = 0 [By definition of NE]

but sigma = (mu, 1-mu)

u(sigma, sigma) = (2mu-1)^2

which for mu != 1/2 is >0 so not an ESS.

#### After the lecture

Students given homework sheet 4 (Finite and infinitely repeated games)
### Assessment

Assessment of the content covered in this lecture will be through examination questions asking student to write out extensive form game representations of games and interpret such representations.
