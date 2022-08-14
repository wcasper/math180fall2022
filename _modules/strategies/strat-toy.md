---
layout: page
title: Toy Examples
permalink: /modules/strategies/strat-toy
---

One really nice way to approach problems is to consider smaller or "toy" versions of a problem, in order to try to establish a pattern that we can apply to the general situation.


## Example 1 
We already saw an example in class, when we were asked to find the number of different placements of a $$3\times 1$$ ship in a $$10\times 10$$ Battleship board.
Starting with smaller boards, like a $$3\times 3$$ board or a $$5\times 5$$ board, it was easy to see a pattern that would work for the larger case!

## Example 2

**Problem:**
Calculate the sum $$S_n$$ of the first $$n$$ squares of integers.

$$S_n = 1^2 + 2^2 + 3^2 + 4^2 + \dots + n^2.$$

Our idea is to first work it out for small values of $$n$$.

|$$n$$|$$S_n$$|
|-----|-------|
|$$1$$|$$  1$$|
|$$2$$|$$  5$$| 
|$$3$$|$$ 14$$| 
|$$4$$|$$ 30$$| 
|$$5$$|$$ 55$$| 
|$$6$$|$$ 91$$| 
|$$7$$|$$140$$| 

We would like to use these smaller values of $$n$$ to establish a pattern for larger values.
Remembering that the sum of the integers $$1 + 2 + \dots + n$$ is $$n(n+1)/2$$, which is a quadratic polynomial in $$n$$, we can guess that $$S_n$$ will be some sort of cubic polynomial in $$n$$, ie.

$$S_n = a + bn + cn^2 + dn^3.$$

Using the first four entries of the chart in this expression, we get a linear system of four equations with four unknowns

$$\begin{align}
a + b + c + d &= 1\\
a + 2b + 4c + 8d &= 5\\
a + 3b + 9c + 27d &= 14\\
a + 4b + 16c + 64d &= 30
\end{align}$$

Solving this for $$a,b,c,$$ and $$d$$ we find $$a = 0$$, $$b = 1/6$$, $$c = 1/2$$ and $$d = 1/3$$.
Hence we conjecture

$$S_n = \frac{1}{6}n + \frac{1}{2}n^2 + \frac{1}{3}n^3.$$

We can check this formula actually works for all the values of $$n$$ in the table!
In fact, we can prove by [mathematical induction](https://en.wikipedia.org/wiki/Mathematical_induction) that it holds for all integers $$n\geq 1$$.

*Note:* there's an even better way to calculate the value of $$S_n$$ using the strategy of rewriting the expression [(link)][strat-rewrite].  Can you find it?

