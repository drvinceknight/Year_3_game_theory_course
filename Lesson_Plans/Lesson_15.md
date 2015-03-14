# OR 3: Lesson Plan Lecture 15
## Stochastic Games

### Aims of lecture

At the end of this lecture students will be able to:

- Define a stochastic game;
- Obtain Nash equilibria in some stochastic games;

### Timeline

#### Before the lecture

- NA

#### During the lecture

Describe stochastic games briefly.

Describe Prisoner's Dilemma stochastic game (but with maximising):

Game x:

[2,2],[0,3]
[3,0],[1,1]

Game y:

[0,0]

Transitions of game x:

[.75,.25],[0,1]
[0,1],[.5,.5]

Transitions of game y:

[0,1]

Play round robin with delta = 1/2 (so game ends in two ways: transition to y and also delta condition).
(Same teams as before)

Now obtain equilibrium behaviour:

Let u be future games to P1 in x
Let v be future games to P2 in x

Thus game becomes:

[2+3*delta*u/4,2+3delta*v/4],[0,3]
[3,0],[1+delta * u/2, 1+delta * u/2]

with delta=1/2 this gives:

[2+3*u/8,2+3v/8],[0,3]
[3,0],[1+u/4, 1+u/4]

4 potential NE:

- (r1,c1):

    2 + 3u/8 >= 3 => 2 >= 8/3 approx 2.6

    If equal then:

        2 + 3u/8 = u => u 16/5 approx 3.2 [This is possible]

        Same for v.

- (r1,c2):

    2 + 3u/8 <= 3 => 2 <= 8/3 approx 2.6

    but in this case: v = 3 so not possible.

    [Similarly for (r2, c1)]

- (r2,c2):

    1 + u/4 >= 0 => u >= -4

    If equal then:

        u + 1 + u/4 => u = 4/3

#### After the lecture

Students will be given reading and some practice exercises.

### Assessment

Assessment of the content covered in this lecture will be through examination questions asking students to define and solve stochastic games.
