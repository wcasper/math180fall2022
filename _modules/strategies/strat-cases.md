---
layout: page
title: Break it into cases
permalink: /modules/strategies/strat-cases
---

For some problems it is very useful to reduce the problem into several distinct subcases.

## Example 1

**Problem:**
Show that if $$n$$ is an integer then $$2n^2 + n + 1$$ is not divisible by $$3$$.

To show this, we break the problem up into three distinct cases, depending on the remainder of dividing $$n$$ by $$3$$.
Specifically, we know that for some integer $$k$$ we must have $$n = 3k$$, $$n = 3k+1$$ or $$n = 3k+2$$.

* Case 1: ($$n = 3k$$)

In this case, we can write

$$2n^2 + n + 1 = 2(3k)^2 + (3k) + 1 = 18k^2 + 3k + 1 = 3(6k^2 + k) + 1.$$

Since $$1$$ is not divisible by $$3$$, we see that $$2n^2  + n + 1$$ can't be either.

* Case 2: ($$n = 3k+1$$)

In this case, we write

$$2n^2 + n + 1 = 2(3k+1)^2 + (3k+1) + 1 = 18k^2 + 15k + 2 = 3(6k^2 + 5k) + 2.$$

Since $$2$$ is not divisible by $$3$$, we see that $$2n^2  + n + 1$$ can't be either.

* Case 3: ($$n = 3k+2$$)

In this case, we write

$$2n^2 + n + 1 = 2(3k+2)^2 + (3k+2) + 1 = 18k^2 + 27k + 11 = 3(6k^2 + 9k+3) + 2.$$

Since $$2$$ is not divisible by $$3$$, we see that $$2n^2  + n + 1$$ can't be either.

## Example 2

In the dead of night, you and three companions are fleeing from [actual cannibal Shia LeBeouf](https://en.wikipedia.org/wiki/Shia_LaBeouf_(song)).
You come to a bridge that you must cross as quickly as possible to get to safety.  However, the bridge is narrow and can only hold two people at a time!
Furthermore, there is on moonlight and you have only one flashlight amongst you, which you must use while crossing the bridge.

As you are uninjured, you can cross the bridge in a minute flat.  Your friend Mary can cross it in two minutes.  However, beaten up as they are, Ted takes $$5$$ minutes and Kelly takes $$8$$ minutes.

**Problem:**
Determine how all four of you can cross the bridge as swiftly as possible.
You know that Shia LeBeouf will catch up to you in 16 minutes!  Can you survive??!?!

To solve this problem, first realize that every time two people cross the bridge, one will have to go back in order for more people to use the torch to cross.
For example, you and Mary could cross (taking two minutes), then you can return (taking one minute), and then cross with Ted (taking 5 minutes), return once more (taking one minute), and cross for the last time with Kelly (taking 8 minutes) for a grand total of 16 minutes.  However, Shia LeBeouf will be on top of you then!  If you can do it no faster, you are surely doomed.

To find the fastest strategy we can list all the possible combinations of crossings.  Of course, since everyone can cross with no more than two return trips, it makes sense that the fastest time will use two return trips.  Also, since Kelly and Ted take so long to cross, if they have to cross more than once the total elapsed time will be more than $$16$$ minutes.  Finally, the optimal time will occur if whoever returns with the flashlight is whoever is fastest person to have already crossed.
Labelling you, Mary, Ted, and Kelly as A,B,C, and D respectively, the sensible possibilities are

| Sequence                                     | Time (minutes) |
|----------------------------------------------|----------------|
| A+B go, A returns, A+C go, A returns, A+D go | 16             |
| A+B go, A returns, A+D go, A returns, A+C go | 16             |
| A+B go, A returns, C+D go, B returns, A+B go | 15             |
| A+C go, A returns, A+B go, A returns, A+D go | 16             |
| A+C go, A returns, A+D go, A returns, A+B go | 16             |
| A+C go, A returns, B+D go, B returns, A+B go | 18             |
| A+D go, A returns, A+C go, A returns, A+D go | 16             |
| A+D go, A returns, A+B go, A returns, A+C go | 16             |
| A+D go, A returns, B+C go, B returns, A+B go | 18             |

As we see from all of the above cases, we can survive!  The fastest strategy will take only $$15$$ minutes.


