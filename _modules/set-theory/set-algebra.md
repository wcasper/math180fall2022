---
layout: page
title: The algebra of sets
---

There are several natural operations for creating new sets out of old ones.

* the **union** of two sets $$A$$ and $$B$$ is the set of all the elements in $$A$$ and $$B$$ combined

$$A\cup B = \{x: x\in A\ \text{or}\ x\in B\}.$$

* the **intersection** of two sets $$A$$ and $$B$$ is the set of all the elements $$A$$ and $$B$$ have in common

$$A\cap B = \{x: x\in A\ \text{and}\ x\in B\}.$$

* the **Cartesian product** or simply **product** of two sets $$A$$ and $$B$$ is the set of all pairs of elements

$$A\times B= \{(a,b): a\in A,\ b\in B\}.$$

* the **complement** of a set $$A$$ is the set of all the elements in the universe $$U$$ not in $$A$$

$$A' = \{x\in U: x\notin A\}.$$

Here $$U$$ is the "universe" that we are working inside, whose value should be determined from the context.

Put together, these operations satisfy several natural properties.  One such property is **distributivity**:

$$A\cap(B\cup C) = (A\cap B)\cup (A\cap C)$$

$$A\cup(B\cap C) = (A\cup B)\cap (A\cup C)$$

Additionally, taking complements swaps unions and intersections.  This is sometimes referred to as **De Morgan's law:**

$$(A\cup B)' = A'\cap B'$$

$$(A\cap B)' = A'\cup B'$$

**Question:** Decide if each of the following statements about algebra with sets is TRUE or FALSE.
* (A) the complement of $$A'$$ is $$A$$
* (B) $$A\cup B=B$$ if and only if $$B\subseteq A$$
* (C) $$A\cap B=B$$ if and only if $$B\subseteq A$$
<details>
  <summary>
  Reveal answer for (A).
  </summary>
  TRUE.  Carefully working through the definition, you should be able to see that taking the complement of a complement gets you back to where you started.
</details>
<details>
  <summary>
  Reveal answer for (B).
  </summary>
  FALSE.  Actually the first statement is equivalent to A being a subset of B
</details>
<details>
  <summary>
  Reveal answer for (C).
  </summary>
  TRUE.  Try drawing a Venn diagram to see that these two conditions are the same.
</details>

<br/>


