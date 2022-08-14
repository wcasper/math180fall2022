---
layout: page
title: Guess and check
permalink: /modules/strategies/strat-guess
---

On some problems, it makes sense to try some reasonable guesses and see what happens.

## Example 1 

**Problem:**
Find all real roots of the polynomial

$$x^3-3x^2+49x-147.$$

To do this, we can remember the following helpful fact: if $$k$$ is an integer root of a polynomial, then $$k$$ must divide the degree zero coefficient.
Thus what we are looking for is one of the divisors of $$147$$.
The divisors of $$147$$ are $$\pm1, \pm3, \pm7, \pm21, \pm49,$$ and $$\pm147$$

For simplicity, we start by guessing the smaller ones.  It turns out $$\pm 1$$ are not roots, but $$3$$ is a root.
Therefore by long division we can factor

$$x^3-3x^2+49x-147 = (x-3)(x^2+49).$$

From this we see that the *only* real root of the polynomial is $$3$$.



