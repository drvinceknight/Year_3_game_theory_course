# OR 3: Lesson Plan Lecture 18
## Routing games 1

### Aims of lecture

At the end of this lecture students will be to:

- Define a routing game;
- Define optimal flow for a game;
- Define Nash flow for a game.

### Timeline

#### Before the lecture

- Invite students to view video on Pigou's example.
- Ask students to play a very simple routing game online.

#### During the lecture

Look at Pigou's example

Ask class to put hand up and choose which way they are going.

Go through this example:

Three vector definition: f=(alpha_0, alpha_1, alpha_2:

alpha_0 - cost: alpha_0 + (alpha_0 + alpha_1) ^ 2
alpha_1 - cost: 2 + (alpha_0 + alpha_1) ^ 2
alpha_2 - cost: 3  [note that alpha_2 = 4 - alpha_0 - alpha_1]

C(f) = \sum_{p\in P}c_p(f_p)f_p

What paths do we have?

Draw P0, P1, P2

Can re write as:

C(f) = \sum_{e\in E}c_e(f_e)f_e

so

C(1,2,1) = 1 * 1 + 2 * 2 + 3 * 3 ^ 2 + 1 * 1
         = 1 + 4 + 27 + 3 = 35

Optimal flow:

min C(alpha_0, alpha_1, 4 - alpha_0 - alpha_1) = 12 + (alpha_0 + alpha_1)^3 + alpha_0^2 - 3 alpha_0 - alpha_ 1

such that 0 <= alpha_0 + alpha_1 <= 4 and  alpha_0, alpha_1 >= 0

Show region in which we are going to optimise function (triangle bounded by 4 - alpha_0):

Can use Lagrange multipliers etc or can just look at each region (easier).

- Middle of triangle:

alpha_1 = 4 - alpha_0

dC/dalpha_0 = 3(alpha_0 + alpha_1)^2 + 2alpha_0 -3

dC/dalpha_1 = 3(alpha_0 + alpha_1)^2 - 1

local optima: alpha_0 + alpha_1 = sqrt(3) / 3

replace a_1 = sqrt(3)/3 - alpha_0 in to eqn for dC/dalpha_0:

dC/dalpha_0 = 3*3 / 9 + 2 alpha_0 - 3

        => alpha_0 = =1
        => alpha_1 = sqrt(3) / 3 -1 <= 0

        THIS IMPLIES THAT OPTIMA WILL BE ON ONE OF THE BOUNDARIES

- Triangular boundary: alpha_1 = 4 - alpha_0

C(alpha_0) = 12 + 4^3 + alpha_0^2 - 3 alpha_0 - 4 + alpha_0
  = alpha_0^2 - 2 alpha_0 + 72

dC/dalpha_0 = 0 => 2alpha_0 - 2 = 0
                   alpha_0 = 1

this gives C(1,3) = 71 (we know this is not a minimum from previously calculated value)

- Bottom boundary of triangle

alpha_1 = 0

C(alpha_0) = 12 + alpha_0 ^ 3 + alpha_0 ^ 2 - 3 alpha_0
           = alpha ^ 3 + alpha_0 ^ 2 - 3 alpha_0 + 12

dC/dalpha_0 = 3x^2 + 2x - 3 = 0

    x = sqrt(10) / 3 - 1/3 approx .72

C(sqrt(10) / 3 - 1/3, 0) approx 10.73 (possible!)

- Final boundary (the left one)

C(0,alpha_1) = 12 + alpha_1 ^ 3 - alpha_1

dC/dalpha_1 = 3alpha_1^2 - 1
            => alpha_1 =  sqrt(3) / 3

C(0, sqrt(3) / 3) = 11.62

Thus minima is at

alpha_0 = sqrt(10)/3 - 1 / 3
alpha_1 = 0
alpha_2 = 4 + 1/3 -sqrt(10)/3

****
Now for the game theoretic approach
****

At the above, on P0 the latency is:

sqrt(10)/3 - 1 / 3 + (sqrt(10)/3 - 1 / 3) ^ 2 approx 1.24

On P1 latency is (no one uses it so we do not actually care):

2 + (sqrt(10)/3 - 1 / 3) ^ 2 approx = 2.52

On P2 latency is:

3

So people on P2 would move to P0:

alpha_0+alpha_0^2 = 3 (still assuming no one uses P1):

alpha_0 = (sqrt(13) - 1) / 2 approx 1.3

Latency is now 3 overall but let us check that P1 does not offer an advantage:

2 + ((sqrt(13) - 1) / 2 ) ^ 2 approx 3.7

So Nash flow given by:

alpha_0 = (sqrt(13) - 1) / 2
alpha_1 = 0
alpha_2 = 4 - (sqrt(13) - 1) / 2

#### After the lecture

Students given reading and exercises.

### Assessment

Assessment of the content covered in this lecture will be through examination questions asking students to define non-atomic routing games and solve from basic principles the Nash flow and optimal flow.
