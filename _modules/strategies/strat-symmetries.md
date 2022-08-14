---
layout: page
title: Symmetries
permalink: /modules/strategies/strat-symmetries
---

In lots of problems, the problem can be simplified or even solved by exploiting symmetries in the problem.

## Example 1 
A farmer needs to construct an animal pen in the shape of a rectangle.
He has enough materials to construct a $$1000$$ meters of fencing.

**Problem:**
What are the unique dimensions of the pen that maximize the area enclosed?

To solve this problem, let $$x$$ be the width of the pen and $$y$$ be the length.
Then the area that we are trying to optimize is $$A = xy$$.
Notice that if $$x = a$$ and $$y=b$$ maximize the area, then so do $$x = b$$ and $$y=a$$.
Since the optimal dimensions are unique, it follows that $$a = b$$.

The optimal dimensions will use up all the supplies, so $$2a + 2b = 1000$$.  Since $$a = b$$, this means $$2a + 2a = 1000$$, ie. $$4a = 1000$$ so that $$a = 250$$.
Consequently the optimal dimensions are a width of $$250$$ and a length of $$250$$.

*Note:* It is not always true that when we are trying to optimize a symmetric function $$f(x,y)$$ that the optimum will occur at a symmetric point.  Can you think of a counter-example?


