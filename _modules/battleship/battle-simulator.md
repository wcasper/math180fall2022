---
layout: page
title: Battleship Simulator
permalink: /modules/battleship/battleship-simulator
---



### Static firing algorithms

The most basic kind of Battleship firing algorithm you can make is a **static firing algorithm**, one where the locations and the order of the shots you want to make is specified entirely at the beginning.  In other words, at the start you enumerate the entries in the board in the order you want to shoot them.  Whenever you get a hit, you proceed with a typical sinking procedure to finish off the ship, before continuing where you left off with your previous series.  Contrast this kind of firing algorithm with a **dynamic firing algorithm** where the next shot that you take can depend entirely on the state of the board.

The simulator below allows you to test the performance of a static firing algorithm.  
* Click the squares in the first box in the firing order that you wish to specify.
* Use the *undo button* if you need to change the order of the sequence or the *clear button* to start over completely.
* It is not necessary to select all squares.  Any squares not specified in the order will be chosen in a random order as necessary at the end.
* Then click the *simulate button* to generate a random Battleship fleet and calculate how many shots your algorithm takes to sink it.
* You can click the *simulation button* several times with the same firing algorithm to get an average performance over a sample of several random fleets.

<head>
<meta charset='utf-8'>
<link rel="stylesheet" href="battle-simulator.css">
</head>


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


