---
layout: page
title: Systematically organizing data
permalink: /modules/strategies/strat-organize
---

One particularly rewarding strategy on almost *any* math problem is to systematically organize the relevant data.


## Example 1

This example deals with [partitions](https://en.wikipedia.org/wiki/Partition_(number_theory)), ie. decreasing sequences of positive integers which add up to a fixed number.
For example, the following are all partitions of $$7$$:

$$(7),\ \ (3,2,2),\ \ (6,1),\ \ (4,1,1,1).$$

However, $$(5,1)$$ is not a partition of $$7$$ because it doesn't add up to $$7$$ and $$(2,3,2)$$ is not a partition of $$7$$ because it's not a decreasing sequence.

**Problem:** Find all the partitions of $$7$$.

To solve this, we can start to write down all of the possibilities as we think of them, but when we do that it starts to get pretty difficult to see if we repeat any or miss any.
Instead, we should *systematically organize* the possibilities, in order to make sure we don't miss any.
Our idea is to list them in reverse alphabetical order.

$$
\begin{align*}
(7)         \\ 
(6,1)       \\ 
(5,2)       \\ 
(5,1,1)     \\ 
(4,3)       \\
(4,2,1)     \\
(4,1,1,1)   \\
(3,3,1)     \\
(3,2,2)     \\
(3,2,1,1)   \\
(3,1,1,1,1) \\
(2,2,2,1  ) \\
(2,2,1,1,1) \\
(2,1,1,1,1,1) \\
(1,1,1,1,1,1,1)
\end{align*}
$$




