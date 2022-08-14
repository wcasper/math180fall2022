---
layout: page
title: Rewriting expressions
permalink: /modules/strategies/strat-rewrite
---

Sometimes the key to solving a problem is to rewrite the problem in a new and revealing way.

## Example 1

One particularly alluring example of this comes from a famous  story of Gauss as a young student.
Indesposed from a night of carousing about town, Gauss's teacher found themselves indisposed first thing in the morning.
To occupy their class while they recovered, they asked every student to solve the following problem

**Problem:**
Calculate the sum of the first $$100$$ positive integers

$$1 + 2 + \dots + 100.$$

Since the class was full of very young people, their teacher expected this to take a fair amount of time.  However, Gauss figured out almost instantly that thw answer was $$5050$$!  A very impressive feat, especially for someone so young.

The key idea Gauss used was to write the sum he was trying to compute both forwards *and* backwards.

$$\begin{array}{lllllll}
1   & +2  & +3  & +4  & +5  & +\dots & + 100\\
100 & +99 & +98 & +97 & +96 & +\dots & + 1
\end{array}$$

Of course, it doesn't matter whether we add them forwards or backwards, the result should be the same.

Now Gauss made the key observation: the sum of each column above is $$101$$.
Therefore if we were to add the sums of all the columns together, we would add $$101$$ to itself $$100$$ times, getting $$100\cdot101$$.
But that's will be exactly the same as twice the sum we were looking for!
Hence $$1 + 2 + 3 + \dots + 100 = (100\cdot 101)/2$$.

We can generalize this right away to find that for any integer $$n\geq 1$$:

$$1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2}$$


## Example 2

Another great example of this strategy in action comes from **geometric series**.

**Problem:**
Let $$r$$ be a real number different from $$1$$ and let $$n>0$$ be an integer.
Calculate the sum of the first $$n$$ powers of $$r$$.

$$1 + r + r^2 + r^3 + \dots + r^n.$$

To solve this, we let $$S = 1 + r + r^2 + \dots + r^n$$, and realize that

$$\frac{S - 1}{r} = \frac{r + r^2 + r^3 + \dots + r^n}{r} = 1 + r + r^2 + \dots + r^{n-1}.$$

and also

$$S - r^n = 1 + r + r^2 + \dots + r^{n-1}.$$

Therefore

$$\frac{S-1}{r} = S-r^n.$$

Now multiply both sides of this by $$r$$ to get

$$S-1 = rS-r^{n+1}.$$

Adding $$1$$ to both sides and subtracting $$rS$$ from both sides, we get

$$S-rS = 1-r^{n+1}.$$

On the left hand side, we can factor out the common factor of $$S$$ to get

$$(1-r)S = 1-r^{n+1}.$$

Finally, dividing by $$1-r$$, we see $$S = (1-r^{n+1})/(1-r)$$, ie.

$$1 + r + r^2 + \dots + r^n = \frac{1-r^{n+1}}{1-r}.$$

