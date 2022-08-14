---
layout: page
title: Shobu Homework 2
permalink: /modules/shobu/homework2
---

<p align="center"><img src="fig/shobot.jpeg" width="50%"/></p>

The game designers of Shobu, Manolis Vranas and Jamie Sajdak, have decided to create an online implementation of their game, including a mode where you can play against the computer!  Having heard of your vast experience and detailed analysis of the game in this class, they want you to help them to design the AI for the computer.  In other words, they want you to help create a **Shobot** (copyright, trademark, patent pending).

What you must do is create a detailed strategy for what the Shobot should do for any particular move during an entire game.  You are allowed to vary the strategy depending on whether the Shobot is Player 1 or Player 2, however both instances must be covered!

* Write a detailed description of the strategy that should be programmed into the computer.  You can be very specific if you need to in certain instances!
* Make sure that your strategy takes care of every possible game state, so that the computer knows what it should do for its next move regardless of the current board state.  There should be no ambiguity!  Remember: computers can't do anything you don't tell them to do!
* After your strategy, include a justification for why you think this strategy is good.  Maybe you tested it thoroughly in manual gameplay.  Or perhaps there is some central strategic principle guiding your idea like (1) trying to keep your pieces in the center of the board or (2) knocking off the opponents pieces whenever possible.  Explain this!

Once your algorithms are finished and submitted, they will be coded in Python by your instructor and tested against one another in what we are calling **The Ultimate Shobot Gauntlet of Champions** (copyright, trademark, patent pending).  The teams whose algorithms win the most games will win a **real world prize**!


### Examples of simple strategies
The following are examples of strategies which are very simple and thoroughly described, but probably not the best.  They are just here to give your group a starting point.
* **Strategy 1: (Random)** Pick each move entirely randomly from the available legal moves.
* **Strategy 2: (All-out attack)**
- If there is a move that can push an opponents piece off of any board, then do that for your move.  If there are multiple such opportunities, push the one on the board where the opponent has the least stones.  If there are still multiple opportunities, just choose the one of the options at random.
- If there are no available ways to push an opponents stone off of a board, then just randomly make any available legal move.

* **Strategy 3: (The Pacifist)**
- If there is a piece of yours that is threateded to be pushed off of the board, then save it if there is a move to do so.  If there are multiple such saves available, then randomly pick one.
- If no pieces are threatened, then randomly move one of your pieces such that it goes to a spot where it is still safe.  If this is not possible, just choose and perform a random legal move.


