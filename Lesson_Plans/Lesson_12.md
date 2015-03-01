# OR 3: Lesson Plan Lecture 12
## Population Games and Evolutionary stable strategies

### Aims of lecture

At the end of this lecture students will be able to:

- Familiar with concepts of Evolutionary game theory.
- Test for ESS in games against the field.

### Timeline

#### Before the lecture

- Invite students to watch video on Evolutionary game theory

#### During the lecture

Demonstrate concepts of evolutionary game theory using playing cards (see: http://drvinceknight.blogspot.co.uk/2014/03/a-very-brief-interactive-look-at.html)
    - Consider all playing down
    - All playing Up
    - Half playing down
    - Randomly playing

    Conclusions are that have two stable strategies and also that can have population induced from strategy.

Go through basic theorem for necessity of stability.

Go through example of computers (with assumption that they are not able to talk to each other):

> Two operating systems: W and L.

Assume x is number of W users and population vector X = (x, 1-x)

Assume following utilities:

u(W,X) = 1 + 2x
u(L,X) = 2 + 2(1-x)

3 potential ESS?

- sigma_W = (1,0)
- sigma_L = (0,1)
- sigma_M = (x,1-x)

For last one:

1+2x = 2 + 2(1-x)
x=3/4

Now consider general post entry population:

X_epsilon = (1-epsilon)sigma^* + epsilon sigma
          = sigma^* + epsilon (sigma - sigma^*) # Remember that sigma is vector

Let:

delta = u(sigma^*,X_epsilon) - u(sigma,X_epsilon)

if delta > 0 then ESS (by definition).

Consider general case:

sigma = (mu, 1-mu)
sigma^* = (mu^*, 1-mu^*)  # So this is one of the 3 from previously

delta = mu^*u(W,X_epsilon)+(1-mu^*)u(L,X_epsilon) -
            muu(W,X_epsilon)-(1-mu)u(L,X_epsilon)

delta = u(W,X_epsilon)(mu^*-mu) - u(L,X_epsilon)(mu^*-mu)
delta = (mu^*-mu)(u(W,X_epsilon) - u(L,X_epsilon))

we can now substitute:

delta = (mu^*-mu)(1+2(mu^*+epsilon(mu-mu^*)) - 2 - 2(1-mu^*+epsilon(mu^*-mu))
      = (mu^*-mu)(-3+4mu^*+4epsilon(mu-mu^*))

Now all we need to do is put the different potential strategies in and identify the sign of delta! :)

1. mu^* = 1

delta = (1-mu)(1+4epsilon(mu-1))

delta > 0 iff 1+4epsilon(mu-1) > 0

we know that 1+4epsilon(mu-1) > 1-4epsilon
which is > 0 if epsilon < 1/4

so ESS.

2. mu^* = 0

delta = -mu(-3+4epsilon)

delta > 0 iff -3 + 4epsilon < 0

this holds as long as epsilon < 3/4

so ESS.

3. mu^* = 3 / 4

delta = (3/4 - mu)(4epsilon(mu - 3/4))
      = (3/4 - mu)(3/4-mu)(-4epsilon) < 0

not a stable NE.

#### After the lecture

Students will be given reading and some practice exercises.
### Assessment

Assessment of the content covered in this lecture will be through examination questions asking student to prove whether or not we have ESS.
