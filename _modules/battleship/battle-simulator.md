---
layout: page
title: Battleship Simulator
permalink: /modules/battleship/battleship-simulator
---


<head>
<meta charset='utf-8'>
<link rel="stylesheet" href="battle-simulator.css">
</head>


### Static firing algorithms

The most basic kind of Battleship firing algorithm you can make is a **static firing algorithm**, one where the locations and the order of the shots you want to make is specified entirely at the beginning.  In other words, at the start you enumerate the entries in the board in the order you want to shoot them.  Whenever you get a hit, you proceed with a typical sinking procedure to finish off the ship, before continuing where you left off with your previous series.

### Dynamic firing algorithms

In comparison with static firing algorithms, we can also consider a **dynamic firing algorithm** where the next shot that you take can depend on the current state of the board.  In other words, dynamic firing algorithms leverage what we already know about our hits and misses from shots already taken.  Dynamic firing algorithms are more complicated to describe, but they often perform better than static ones.


### Testing static algorithms

Programming dynamic firing algorithms can vary widely and may require in-depth programming.  Static algorithms on the other hand are easy to test and can be used as a point of inspiration in developing dynamic ones.

The simulator below allows you to test the performance of a static firing algorithm.  
* Click the squares in the first box in the firing order that you wish to specify.
* Use <button class="button-85">Undo</button> if you need to change the order of the sequence or <button class="button-85">Clear</button> to start over completely.
* It is not necessary to select all squares.  Any squares not specified in the order will be chosen in a random order as necessary at the end.
* Then click <button class="button-85">Simulate</button> to generate a random Battleship fleet and calculate how many shots your algorithm takes to sink it.
* You can click <button class="button-85">Simulate</button> several times with the same firing algorithm to get an average performance over a sample of several random fleets.

### Battleship simulator

<body>


<center>
<h3>Firing Sequence</h3>
<div id="firing-order">
</div>
</center>

<br/>
<center>
<button id='undo' class="button-85" role="button">Undo</button>
<button id='clear' class="button-85" role="button">Clear all</button>
<button id='simulate' class="button-85" role="button">Simulate!</button>
</center>

<br/>
<center>
<button id='simulate100' class="button-85" role="button">Simulate 100!</button>
</center>

<br/>
<center>
<h3>Simulated Fleet</h3>
<div id="battleship-fleet">
</div>
</center>

<center>
<p id="statistics">
</p>
</center>




<script src='battle-simulator.js'></script>
</body>


