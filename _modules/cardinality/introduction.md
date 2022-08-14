---
layout: page
title: Cardinality Introduction
permalink: /modules/cardinality/introduction
---

## Cardinality
The **cardinality** $$\lvert A\rvert$$ of a set $$A$$ measures the number of elements of a set.

Here are some examples.
* The cardinality of $$\{1,2,\Delta\}$$ is $$3$$.
* The cardinality of $$\{\heartsuit,\diamondsuit,\clubsuit,\spadesuit\}$$ is $$4$$.

Cardinality is also generalized to infinite sets, starting with the observation of Cantor that for finite sets, two sets have the same cardinality if and only if there is a bijection between them.

**Definition 1:** We say sets $$A$$ and $$B$$ have the same cardinality ($$\lvert A\rvert = \lvert B\rvert$$) if there exists a bijective function from $$A$$ to $$B$$.

Likewise, by observing generalizations about the existence of injections or surjections in the finite case, we can obtain inequalities between cardinalities.

**Definition 2:** We say $$A$$ has cardinality less than or equal to $$B$$ ($$\lvert A\rvert \leq \lvert B\rvert$$) if there exists an injective function (one-to-one function) from $$A$$ to $$B$$.

**Definition 3:** We say $$A$$ has cardinality greater than or equal to $$B$$ ($$\lvert A\rvert \geq \lvert B\rvert$$) if there exists a surjective function (onto function) from $$A$$ to $$B$$.

Now one of the most beautiful things about this is that these three definitions are mutually compatible, even in the infinite situation!  For example one can show $$\lvert A\rvert \leq \lvert B\rvert$$ if and only if $$\lvert B\rvert\geq \lvert A\rvert$$.  This is captured by the next theorem.

**Theorem:** Let $$A$$ and $$B$$ be sets.  There exists an injective function $$f: A\rightarrow B$$ if and only if there exists a surjective function $$g: B\rightarrow A$$.  Consequently $$\lvert A\rvert \leq \lvert B\rvert$$ if and only if $$\lvert B\rvert\geq \lvert A\rvert$$.

This theorem which shows consistency between the intuitively motivated definitions above tells mathematicians that they are on the right track and that their definitions are "right" or "natural".  Adding to this sense of compatibility, we can prove $$\lvert A\rvert\leq \lvert B\rvert$$ and $$\lvert A\rvert \geq \lvert B\rvert$$ implies $$\lvert A\rvert = \lvert B\rvert$$.

**Theorem:** Let $$A$$ and $$B$$ be sets.  There exists both an injective function $$f: A\rightarrow B$$ and a surjective function $$g: A\rightarrow B$$ if and only if there exists a bijective function $$h: A\rightarrow B$$.  Consequently $$\lvert A\rvert\leq \lvert B\rvert$$ and $$\lvert A\rvert \geq \lvert B\rvert$$ if and only if $$\lvert A\rvert = \lvert B\rvert$$.



