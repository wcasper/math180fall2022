---
layout: page
title: Basic Intro to Set Theory
permalink: /modules/set-theory/introduction
---

## What is a set

After paying appropriate homage to calculus, differential equations, and linear algebra, students journeys into higher mathematics all begin with the notion of a set.  Intuitively, a set is a collection of objects, called elements or members.  Often sets are described by listing the members in between curly brackets.  For starters

$$\{\times,\div,+,-\},\quad \{1,2,3\},\quad \{4,7,\heartsuit, \clubsuit, Q\}$$

are all examples of sets.  One of the most important examples of a set is the empty set $$\{\}$$, the set with no members.  Because of its distinguished role, we denote it by the special symbol $$\varnothing$$.  It's important to note that sets don't remember order or multiplicity, so the following all describe the same set

$$\{1,2,3\},\quad \{1,3,2\},\quad \{1,3,2,3\}$$

Members of sets can be just about anything.  Names, houses, planets, numbers, even other sets!  This latter idea is extremely important in the conception of the axiomatic construction of cardinal numbers, as explained in Gallery of the Infinite.  We explain this in a fun way here.

* We start out with nothing which we represent by $$\varnothing$$
* We've noticed we have nothing, which is something!  Let's put it in a collection

$$C_1 = \{\varnothing\}$$


* Now we have two different things: $$\varnothing$$, and $$C_1$$ so we can put them into a new collection

$$C_2 = \{\varnothing,C_1\} = \{\varnothing,\{\varnothing\}\}$$


* Now we have three different things: so we can put them into a new collection 

$$C_3 = \{\varnothing,C_1,C_2\} = \{\varnothing,\{\varnothing\},\{\varnothing,\{\varnothing\}\}\}.$$

Notice $$C_1$$ has one member, $$C_2$$ has two members, and $$C_3$$  has three members.  Continuing in this way, we can create sets with any number of members,  all created from nothing!

### More ways to Describe Sets

Oftentimes, the sets that we want to work with are large enough that it is impractical or impossible to describe them by listing their members.  Think about, for example, the set  of all possible poker hands.  There are $$2,598,960$$ possibilities, so if we start listing them out we will be here for a while!  Instead we can adopt a new notation

$$P = \{x | x\ \text{is a poker hand}\}.$$

In other words, we can describe sets in terms of conditions.  Here is another example, describing all real numbers between -1 and 1.

$$\{x | x\ \text{is a real number and $-1\leq x \leq 1$}\}.$$

### Membership and Inclusion

If $$S$$ is a set, then the statement $$x\in S$$ means that "$$x$$ is a member of $$S$$" or "$$x$$ is an element of $$S$$".  We say that a set $$T$$ is a subset of $$S$$ if every member of $$T$$ is also a member of $$S$$.  In this case, we write $$T\subseteq S$$.
