# OR 3: Lesson Plan Lecture 14
## Random events and incomplete information

### Aims of lecture

At the end of this lecture students will be able to:

- Represent games of incomplete information in extensive form;
- Be familiar with utility functions;
- Be familiar with the principal agent game

### Timeline

#### Before the lecture

- Invite students to play some one shot games online (with incomplete information).

#### During the lecture

Get 3 players: 3 player round robin tournament.

Play following extensive form game:

P1:
    - Heads
    - Tails
        Flip coin (same information set as two above games)
            - Heads
                P2
                    - Heads
                    - Tails
            - Tails
                    - Heads
                    - Tails

Utilities:
    u(H, H, H) = (0, 0)
    u(H, H, T) = (-1, 1)
    u(H, T, H) = (1, -1)
    u(H, T, T) = (-1, 1)
    u(T, H, H) = (-1, 1)
    u(T, H, T) = (1, -1)
    u(T, T, H) = (-1, 1)
    u(T, T, T) = (0, 0)

Both players swap.

[Ask students if there is an optimal way to play player 2?]

Write normal form game representation:

S1 = {H,T}
S1 = {HH, HT, TH, TT}

Get this normal form game:

[1/2,-1/2],[-1/2,1/2],[0,0],[-1,1]
[-1,1],[-1/2,1/2],[0,0],[1/2,-1/2]

We see that TH is dominated:

[1/2,-1/2],[-1/2,1/2],[-1,1]
[-1,1],[-1/2,1/2],[1/2,-1/2]

Let us look at u2((x,1-x),s):

u2((x,1-x),HH) = -1/2x+1-x = 1-3x/2
u2((x,1-x),TT) = x - 1/2 + x / 2 = 3x/2-1/2

Plot the above with u2((x,1-x),HT)=1/2

sigma_2 = (y,z,0,1-y-z)

sigma_2 = (1,0,0,0) if x < 1/3 ; (0,1,0,0) 1/3<=x<2/3; (0,0,0,1) 2/3<=x

but if sigma_2 = (0, 1, 0, 1) then P1 is indifferent, thus NE is:

sigma_1 = (x, 1-x) for 1/3<=x<=2/3
sigma_2 = (0, 1, 0, 0)

(0,1,0,0) corresponds to HT which is Hs when Hs and Ts when Ts.

***

Point at utility theory
Point at principal agent game

#### After the lecture

Students will be given reading and some practice exercises.

### Assessment

Assessment of the content covered in this lecture will be through examination questions asking student to represent games and solve games similar to the principal agent game.
