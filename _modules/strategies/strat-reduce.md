---
layout: page
title: Reduce the problem
permalink: /modules/strategies/strat-reduce
---

Many times a problem can be solved by reducing it to a problem that we already know how to solve.

## Example 1

You are transported back in time to a classroom with a young Gauss.
An exasperated instructor has asked the class to solve the following problem.

**Problem:**
Compute the sum of the first $$100$$ *even* integers:

$$2 + 4 + 6 + 8 + \dots + 200.$$

To do this, we can realize

$$2 + 4 + 6 + 8 + \dots + 200 = 2(1 + 2 + 3 + 4 + \dots + 100).$$

Since Gauss already figured out the sum of the first $$100$$ integers is $$5050$$ (see [here](strat-rewrite)), we automatically know the answer is $$10100$$.


## Example 2

What if instead Gauss's teacher asked you to find the sum of the first $$100$$ odd integers?

**Problem:**
Calculate the sum of the first $$100$$ odd integers

$$1 + 3 + 5 + 7 + \dots + 199.$$

To do this, we can realize that the sum of the first $$100$$ integers is the same as the sum of the first $$200$$ integers, minus the sum of the first $$100$$ even integers:

$$1 + 3 + 5 + 7 + \dots + 199 = (1 + 2 + 3 + 4 + \dots + 200) - (2 + 4 + 6 + 8 + \dots + 200)$$ 

We know the first sum on the left hand side is $$(200\cdot201)/2 = 20100$$ (see [here](strat-rewrite)).
Moreover, we figuredout that the second sum on the right hand side is $$10100$$ in the previous example.  So the sum we want is

$$1 + 3 + 5 + 7 + \dots + 199 = 20100 - 10100 = 10000.$$



