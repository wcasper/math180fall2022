---
layout: page
title: Generalize the problem
permalink: /modules/strategies/strat-general
---

One broad theme mathematically moving forward through your classes is that many times a problem becomes simpler when we *generalize* it.
Below we see a couple of slick examples of this.

## Example 1 

Sometimes by generalizing, we can make an expression familiar.

**Problem:**

Calculate the sum

$$1 + \frac{2}{7} + \frac{3}{7^2} + \frac{4}{7^3} + \frac{5}{7^4} + \dots + \frac{2020}{7^{2020-1}}$$

To solve this, we generalize by replacing $$1/7$$ with $$r$$ to get

$$1 + 2r + 3r^2 + 4r^3 + 5r^4 + \dots + 2020r^{2020-1}.$$

We can recognize this as the *derivative* of the geometric sum

$$1 + r + r^2 + r^3 + r^4 + r^5 + \dots + r^{2020}$$

we know that this sum is $$\frac{1-r^{2021}}{1-r}$$, so that

$$
\begin{align*}
1 + 2r + 3r^2 + 4r^3 + 5r^4 + \dots + 2020r^{2020-1}
& = \frac{d}{dr}\left(\frac{1-r^{2021}}{1-r}\right)\\
& = \frac{2020r^{2021}-2021r^{2020}+1}{(1-r)^2}
\end{align*}$$

Now inserting the value of $$r = 1/7$$, we get that

$$1 + \frac{2}{7} + \frac{3}{7^2} + \frac{4}{7^3} + \frac{5}{7^4} + \dots + \frac{2020}{7^{2020-1}}\approx 1.361111.$$


## Example 2

One of Feynmann's favorite methods is *differentiation under the integral* which we will apply here in conjunction with our generalization strategy.

**Problem:**

Calculate the integral

$$\int xe^x dx.$$

To do this, we can realize this as the special case of $$r = 1$$ for the integral

$$\int xe^{rx} dx.$$

By differentiation under the integral

$$
\begin{align*}
\int xe^{rx} dx
  & = \int\frac{d}{dr}e^{rx}dx = \frac{d}{dr}\int e^{rx}dx\\
  & = \frac{d}{dr}\frac{1}{r}e^{rx} = \left(\frac{x}{r}-\frac{1}{r^2}\right)e^{rx}.
\end{align*}$$

Taking $$r = 1$$, we find

$$\int xe^x dx = (x-1)e^{rx}.$$



