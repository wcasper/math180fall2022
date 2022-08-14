---
layout: page
title: Battleship Commander Competition Results
permalink: /modules/battleship/competition-results
---

<p align="center"><img src="fig/captainpic.jpg" width="50%"/></p>

## After-action report
The battle was long and hard fought, and the strategies bold.

| Group | Algorithm | Average Shots to Sink |
| ----- | --------- | --------------------- |
|       |  Random Guess | 59.5941 |
|   1   | Counter-Clockwise Search | 59.9771 |
|   2   | Dark Knight Search | 59.5636 |
|   3   | Checkered Dart Board Search | 60.3797 | 
|   4   | Spider Web Search | 57.5274 | 
|   5   | Iterated Guess Search | 57.3763 | 
|   6   | Polygon earch | 57.3138 | 
|   7   | X Factor Search | 53.782 | 
|   8   | Swirl Search | **53.1018**  | 

Congratulations to **Monika Chhay**, **Isaias Gallardo-Anell**, and **Vicky Li** for their impressive victory!
You may pick up your spoils of war in your Professor's office (MH 160-A) later this week.  Send me an email with the time and day you can stop by.

### Strategies

The strategies were excellent and ranged from the simple to the very elaborate.  Here are some brief descriptions of each algorithm.  Note that the part of the algorithm for sinking a ship after one was found was pretty routine, so it's omitted here.

* The **Counter-Clockwise Search**:  This algorithm divides the board up into four quadrants, like in the x,y-plane.  We randomly select a point to search in the first quadrant, and then search the same point in the other three quadrants proceeding counter-clockwise.  
* The **Dark Knight Search**:  In this algorithm, we perform a knight move (like in chess) from the possition of a random missed shot in order to guess a new shot position.
* The **Checkered Dart Board Search**:  In this algorithm, we divide the board into a series of three rings sort of like a dart board, which are checkered.  We fire at the center and the four corners, and then within the various rings in a checkered pattern.
* The **Spider Web Search**: We search in a pattern that looks kind of like a spider web from Minecraft.  Starting from the center, we move toward each of the four corners sequentually, forming a big X.  Then we fill in a series of rings around it to create a web we have searched.  If the fleet still isn't sunk, we start randomly guessing the remaining positions.
* The **Iterated Guess Search**: This algorithm was probably the most elaborate to code.  Starting with a random missed position, we move to a random position N spaces away (where N is the length of the smallest remaining ship) which has enough space to potentially contain one of the missing ships.  If no such position is available, do the same procedure from a previous hit position.
* The **Polygon Search**:  We search randomly in two concentric polygon patterns.  If the fleet is not sunk after filling out both polygon shapes, we randomly select remaining spaces until we sink the fleet.
* The **X Factor Search**: First we create a big X by searching from the center to each of the four corners.  Then depending on the length of the smallest remaining ship N, we search in a grid pattern skipping every N-1 spaces in each row.  We specifically use the grid pattern which already has the most spaces guessed already, so that we have less spaces to check.
* THe **Swirl Search**: The algorithm starts in the center and then makes an very cool swirl which eminates out to the boundary, skipping every other space.  Then  we start from the center again and make another swirl that does not overlap with the first and which completes the search of the entire board in a checkerboard way.
Notably the algorithm is completely deterministic: no random choices were ever needed.
