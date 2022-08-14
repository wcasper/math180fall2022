---
layout: page
title: Ultra Weakly Solved Games
permalink: /modules/tic-tac-toe/weakly-solved-games
---

<p align="center"><img src="fig/data-star-trek.jpg" width="60%"/></p>


### Who can force a win?

A fundamental question about any two-player game is which one of the players can force a win or tie.
Intriguingly, sometimes we can determine which player *has* such a strategy, even if we don't know what it is.
In a way, these are the most intriguing examples, since it involves a non-constructive existence argument and must leverage something fundamental about the nature of the game.
Games where we know which player has the strategy, but don't know what the strategy is, are called **ultra weakly solved games**.

### The Divisor Game

Consider, for example, the **Divisor Game** is a two-player game which has the following rules
* Fix a starting integer $$N$$.
* Each player takes turns choosing positive integer divisors of $$N$$.
* You cannot choose a positive integer divisor of $$N$$ which divides any previously chosen divisors.
* The player that is forced to choose $$N$$ loses.

1. Take ten minutes to play the divisor game with your group members for $$N = 2592 = 2^53^4$$.
Make sure to switch off, giving everyone a chance to play.
2. After everyone has played, talk about strategy.  Were there any particular strategies that worked very well?
3. Decide with your group which player can force a win or a tie.  Is it player 1 or player 2?  Can you explain why?

