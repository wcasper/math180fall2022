---
layout: page
title: Example Competition Strategies
permalink: /modules/battleship/old-strategies
---

<p align="center"><img src="fig/battleship_battle.jpg" width="50%"/></p>
<h4 style="text-align: center;"><strong>Pure Random</strong></h4>
<p>Firing blocks are selected randomly from the board.&nbsp; Whenever a hit occurs, follow up by sinking the ship (and any other ships incidentally identified in the process), and then go back to randomly selecting open spaces for the next shot until the enemy fleet is sunk.</p>
<h4 style="text-align: center;"><strong>Random Checkerboard</strong></h4>
<p>View the board as a checkerboard, with half the squares <span style="color: #ba372a;"><strong>red</strong></span> and half <strong>black</strong>.&nbsp; Randomly select black blocks from the board.&nbsp; Whenever a hit occurs, follow up by sinking the ship (and any other ships incidentally identified in the process), and then go back to randomly selecting open <strong>black</strong> squares for the next shot until the enemy fleet is sunk.</p>
<h4 style="text-align: center;"><strong>Red vs Blue</strong></h4>
<p>This strategy refines the random checkerboard strategy by first searching a further refined grid in order to guarantee sinking the carrier.&nbsp; Color diagonals A1-J10, A5-F10, A9-B10, E1-J6, and I1-J2 <span style="color: #ba372a;"><strong>red</strong></span>.&nbsp; Also color diagonals C1-J8, A3-H10, G1-J4, A7-D10 <span style="color: #236fa1;"><strong>blue</strong></span>.&nbsp; &nbsp;Now first fire randomly at the <span style="color: #ba372a;"><strong>red</strong></span> squares.&nbsp; Whenever a hit occurs, follow up by sinking the ship (and any other ships incidentally identified in the process).&nbsp; Then go back to firing at <span style="color: #ba372a;"><strong>red</strong></span> squares only if the carrier has not been sunk, or else randomly at <span style="color: #ba372a;"><strong>red</strong></span> and <span style="color: #236fa1;"><strong>blue</strong></span> squares if the carrier has already been sunk.</p>
<h4 style="text-align: center;"><strong>Random Switch Parity</strong></h4>
<p>This strategy offers an interesting variant of the "checkerboard" random algorithms above, where we split objects into different colored groups.&nbsp; We say that two numbers have the <strong>same parity</strong> if they are both even or both odd, and <strong>opposite parity</strong> if one is even and one is odd.&nbsp; Likewise, we say that two letters have <strong>opposite parity</strong> if one of the letters is one of the following: A,C,E,G, or I and the other letter is one of the following: B,D,F,H,J.&nbsp; Starting with an initial shot any random place on the board, always choose the next shot randomly from the available spaces but such that the new letter and number both have opposite parity to the letter and number of the previous shot.&nbsp; (Unless no such shot is left on the board, in which case, shoot with the same parity as the previous shot).&nbsp; Whenever a hit occurs, follow up by sinking the ship (and any other ships incidentally identified in the process), and then go back to the algorithm described above.</p>
<h4 style="text-align: center;"><strong>Conic Search</strong></h4>
<p>We call this the conic search, because one-dimensional cones look like X's.&nbsp; Given any starting center cell, we will fire shots in an X pattern, proceeding outward from the center first in a northwest direction, then northeast, southwest, and finally southeast.&nbsp; In each case,&nbsp; we try all the squares in the X pattern sequentially from the center until we hit the boundary.&nbsp; Our first X has center at A5.&nbsp; Each time we finish a particular X pattern, we start a new one whose center is two squares to the right of the previous (eg. A5 then C5 then E5 ...).&nbsp; Whenever a hit occurs, follow up by sinking the ship (and any other ships incidentally identified in the process), and then go back to the algorithm described above.</p>
<h4 style="text-align: center;"><strong>Union Jack Search</strong></h4>
<p style="text-align: left;">We call this the Union Jack search, since the pattern drawn out looks like a superimposed cross and X centered in the board.&nbsp; The premise is to follow a very specific shot order as described in the following diagram.</p>
<table style="border-collapse: collapse; width: 79.848%; height: 319px; margin-left: auto; margin-right: auto;" border="1">
    <tbody>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"></td>
            <td style="width: 7.96997%; height: 29px;"><strong>A</strong></td>
            <td style="width: 9.2145%; height: 29px;"><strong>B</strong></td>
            <td style="width: 9.89163%; height: 29px;"><strong>C</strong></td>
            <td style="width: 8.96954%; height: 29px;"><strong>D</strong></td>
            <td style="width: 4.52167%; height: 29px;"><strong>E</strong></td>
            <td style="width: 9.0312%; height: 29px;"><strong>F</strong></td>
            <td style="width: 9.429%; height: 29px;"><strong>G</strong></td>
            <td style="width: 9.92215%; height: 29px;"><strong>H</strong></td>
            <td style="width: 14.1132%; height: 29px;"><strong>I</strong></td>
            <td style="width: 29.384%; height: 29px;"><strong>J</strong></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>1</strong></td>
            <td style="width: 7.96997%; height: 29px;">5</td>
            <td style="width: 9.2145%; height: 29px;">44-50</td>
            <td style="width: 9.89163%; height: 29px;">44-50</td>
            <td style="width: 8.96954%; height: 29px;">44-50</td>
            <td style="width: 4.52167%; height: 29px;">22</td>
            <td style="width: 9.0312%; height: 29px;">44-50</td>
            <td style="width: 9.429%; height: 29px;">44-50</td>
            <td style="width: 9.92215%; height: 29px;">44-50</td>
            <td style="width: 14.1132%; height: 29px;">44-50</td>
            <td style="width: 29.384%; height: 29px; text-align: center;">7</td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>2</strong></td>
            <td style="width: 7.96997%; height: 29px;">38-43</td>
            <td style="width: 9.2145%; height: 29px;">15</td>
            <td style="width: 9.89163%; height: 29px;">65-100</td>
            <td style="width: 8.96954%; height: 29px;">65-100</td>
            <td style="width: 4.52167%; height: 29px;">23</td>
            <td style="width: 9.0312%; height: 29px;">65-100</td>
            <td style="width: 9.429%; height: 29px;">65-100</td>
            <td style="width: 9.92215%; height: 29px;">65-100</td>
            <td style="width: 14.1132%; height: 29px;">18</td>
            <td style="width: 29.384%; height: 29px;">51-57</td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>3</strong></td>
            <td style="width: 7.96997%; height: 29px;"><strong></strong>38-43</td>
            <td style="width: 9.2145%; height: 29px;">65-100</td>
            <td style="width: 9.89163%; height: 29px;">14</td>
            <td style="width: 8.96954%; height: 29px;">65-100</td>
            <td style="width: 4.52167%; height: 29px;">24</td>
            <td style="width: 9.0312%; height: 29px;">65-100</td>
            <td style="width: 9.429%; height: 29px;">65-100</td>
            <td style="width: 9.92215%; height: 29px;">17</td>
            <td style="width: 14.1132%; height: 29px;">65-100</td>
            <td style="width: 29.384%; height: 29px;">51-57</td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>4</strong></td>
            <td style="width: 7.96997%; height: 29px;"><strong></strong>38-43</td>
            <td style="width: 9.2145%; height: 29px;">65-100</td>
            <td style="width: 9.89163%; height: 29px;">65-100</td>
            <td style="width: 8.96954%; height: 29px;">13</td>
            <td style="width: 4.52167%; height: 29px;">25</td>
            <td style="width: 9.0312%; height: 29px;">65-100</td>
            <td style="width: 9.429%; height: 29px;">16</td>
            <td style="width: 9.92215%; height: 29px;">65-100</td>
            <td style="width: 14.1132%; height: 29px;">65-100</td>
            <td style="width: 29.384%; height: 29px;">51-57</td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>5</strong></td>
            <td style="width: 7.96997%; height: 29px;">30</td>
            <td style="width: 9.2145%; height: 29px;">31</td>
            <td style="width: 9.89163%; height: 29px;">32</td>
            <td style="width: 8.96954%; height: 29px;">33</td>
            <td style="width: 4.52167%; height: 29px;">1</td>
            <td style="width: 9.0312%; height: 29px;">3</td>
            <td style="width: 9.429%; height: 29px;">34</td>
            <td style="width: 9.92215%; height: 29px;">35</td>
            <td style="width: 14.1132%; height: 29px;">36</td>
            <td style="width: 29.384%; height: 29px;">37</td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>6</strong></td>
            <td style="width: 7.96997%; height: 29px;"><strong></strong>38-43</td>
            <td style="width: 9.2145%; height: 29px;">65-100</td>
            <td style="width: 9.89163%; height: 29px;">65-100</td>
            <td style="width: 8.96954%; height: 29px;">9</td>
            <td style="width: 4.52167%; height: 29px;">2</td>
            <td style="width: 9.0312%; height: 29px;">4</td>
            <td style="width: 9.429%; height: 29px;">65-100</td>
            <td style="width: 9.92215%; height: 29px;">65-100</td>
            <td style="width: 14.1132%; height: 29px;">65-100</td>
            <td style="width: 29.384%; height: 29px;">51-57</td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>7</strong></td>
            <td style="width: 7.96997%; height: 29px;"><strong></strong>38-43</td>
            <td style="width: 9.2145%; height: 29px;">65-100</td>
            <td style="width: 9.89163%; height: 29px;">10</td>
            <td style="width: 8.96954%; height: 29px;">65-100</td>
            <td style="width: 4.52167%; height: 29px;">26</td>
            <td style="width: 9.0312%; height: 29px;">65-100</td>
            <td style="width: 9.429%; height: 29px;">19</td>
            <td style="width: 9.92215%; height: 29px;">65-100</td>
            <td style="width: 14.1132%; height: 29px;">65-100</td>
            <td style="width: 29.384%; height: 29px;">51-57</td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>8</strong></td>
            <td style="width: 7.96997%; height: 29px;"><strong></strong>38-43</td>
            <td style="width: 9.2145%; height: 29px;">11</td>
            <td style="width: 9.89163%; height: 29px;">65-100</td>
            <td style="width: 8.96954%; height: 29px;">65-100</td>
            <td style="width: 4.52167%; height: 29px;">27</td>
            <td style="width: 9.0312%; height: 29px;">65-100</td>
            <td style="width: 9.429%; height: 29px;">65-100</td>
            <td style="width: 9.92215%; height: 29px;">20</td>
            <td style="width: 14.1132%; height: 29px;">65-100</td>
            <td style="width: 29.384%; height: 29px;">51-57</td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>9</strong></td>
            <td style="width: 7.96997%; height: 29px;">12</td>
            <td style="width: 9.2145%; height: 29px;">65-100</td>
            <td style="width: 9.89163%; height: 29px;">65-100</td>
            <td style="width: 8.96954%; height: 29px;">65-100</td>
            <td style="width: 4.52167%; height: 29px;">28</td>
            <td style="width: 9.0312%; height: 29px;">65-100</td>
            <td style="width: 9.429%; height: 29px;">65-100</td>
            <td style="width: 9.92215%; height: 29px;">65-100</td>
            <td style="width: 14.1132%; height: 29px;">21</td>
            <td style="width: 29.384%; height: 29px;">51-57</td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>10</strong></td>
            <td style="width: 7.96997%; height: 29px;">6</td>
            <td style="width: 9.2145%; height: 29px;">58-64</td>
            <td style="width: 9.89163%; height: 29px;">58-64</td>
            <td style="width: 8.96954%; height: 29px;">58-64</td>
            <td style="width: 4.52167%; height: 29px;">29</td>
            <td style="width: 9.0312%; height: 29px;">58-64</td>
            <td style="width: 9.429%; height: 29px;">58-64</td>
            <td style="width: 9.92215%; height: 29px;">58-64</td>
            <td style="width: 14.1132%; height: 29px;">58-64</td>
            <td style="width: 29.384%; height: 29px;">8</td>
        </tr>
    </tbody>
</table>
<p>We fire space-by-space in the order assigned to each square.&nbsp; For example, we start with shooting at E5, followed by shooting at E6.&nbsp; For squares that feature a range of numbers, we <em>randomly</em> choose an ordering of those square so that the order we fire into them is random but occurs after lower numbered squares.&nbsp; Whenever a hit occurs, follow up by sinking the ship (and any other ships incidentally identified in the process), and then go back to the algorithm described above.</p>
<h4 style="text-align: center;"><strong>Quadrants Search</strong></h4>
<p>We call this the quadrants search because it divides up the board into four quadrants where the action takes place.</p>
<table style="border-collapse: collapse; width: 79.848%; height: 319px; margin-left: auto; margin-right: auto;" border="1">
    <tbody>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"></td>
            <td style="width: 7.96997%; height: 29px;"><strong>A</strong></td>
            <td style="width: 9.2145%; height: 29px;"><strong>B</strong></td>
            <td style="width: 9.89163%; height: 29px;"><strong>C</strong></td>
            <td style="width: 8.0335%; height: 29px;"><strong>D</strong></td>
            <td style="width: 8.73384%; height: 29px;"><strong>E</strong></td>
            <td style="width: 7.93917%; height: 29px;"><strong>F</strong></td>
            <td style="width: 8.80501%; height: 29px;"><strong>G</strong></td>
            <td style="width: 11.3262%; height: 29px;"><strong>H</strong></td>
            <td style="width: 11.1491%; height: 29px;"><strong>I</strong></td>
            <td style="width: 29.384%; height: 29px;"><strong>J</strong></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>1</strong></td>
            <td style="width: 7.96997%; height: 29px;"><span style="background-color: #bfedd2;">38</span></td>
            <td style="width: 9.2145%; height: 29px;"></td>
            <td style="width: 9.89163%; height: 29px;"><span style="background-color: #bfedd2;">23</span></td>
            <td style="width: 8.0335%; height: 29px;"></td>
            <td style="width: 8.73384%; height: 29px;"><span style="background-color: #bfedd2;">45</span></td>
            <td style="width: 7.93917%; height: 29px;"></td>
            <td style="width: 8.80501%; height: 29px;"></td>
            <td style="width: 11.3262%; height: 29px;"><span style="background-color: #fbeeb8;">27</span></td>
            <td style="width: 11.1491%; height: 29px;"></td>
            <td style="width: 29.384%; height: 29px; text-align: center;"><span style="background-color: #fbeeb8;">40</span></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>2</strong></td>
            <td style="width: 7.96997%; height: 29px;"></td>
            <td style="width: 9.2145%; height: 29px;"><span style="background-color: #bfedd2;">3</span></td>
            <td style="width: 9.89163%; height: 29px;"></td>
            <td style="width: 8.0335%; height: 29px;"><span style="background-color: #bfedd2;">4</span></td>
            <td style="width: 8.73384%; height: 29px;"></td>
            <td style="width: 7.93917%; height: 29px;"><span style="background-color: #fbeeb8;">51</span></td>
            <td style="width: 8.80501%; height: 29px;"><span style="background-color: #fbeeb8;">6</span></td>
            <td style="width: 11.3262%; height: 29px;"></td>
            <td style="width: 11.1491%; height: 29px;"><span style="background-color: #fbeeb8;">7</span></td>
            <td style="width: 29.384%; height: 29px;"></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>3</strong></td>
            <td style="width: 7.96997%; height: 29px;"><span style="background-color: #bfedd2;">24</span></td>
            <td style="width: 9.2145%; height: 29px;"></td>
            <td style="width: 9.89163%; height: 29px;"><span style="background-color: #bfedd2;">17</span></td>
            <td style="width: 8.0335%; height: 29px;"></td>
            <td style="width: 8.73384%; height: 29px;"><span style="background-color: #bfedd2;">22</span></td>
            <td style="width: 7.93917%; height: 29px;"><span style="background-color: #fbeeb8;">26</span></td>
            <td style="width: 8.80501%; height: 29px;"></td>
            <td style="width: 11.3262%; height: 29px;"><span style="background-color: #fbeeb8;">18</span></td>
            <td style="width: 11.1491%; height: 29px;"></td>
            <td style="width: 29.384%; height: 29px;"><span style="background-color: #fbeeb8;">28</span></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>4</strong></td>
            <td style="width: 7.96997%; height: 29px;"></td>
            <td style="width: 9.2145%; height: 29px;"><span style="background-color: #bfedd2;">2</span></td>
            <td style="width: 9.89163%; height: 29px;"></td>
            <td style="width: 8.0335%; height: 29px;"><span style="background-color: #bfedd2;">1</span></td>
            <td style="width: 8.73384%; height: 29px;"></td>
            <td style="width: 7.93917%; height: 29px;"></td>
            <td style="width: 8.80501%; height: 29px;"><span style="background-color: #fbeeb8;">5</span></td>
            <td style="width: 11.3262%; height: 29px;"></td>
            <td style="width: 11.1491%; height: 29px;"><span style="background-color: #fbeeb8;">8</span></td>
            <td style="width: 29.384%; height: 29px;"></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>5</strong></td>
            <td style="width: 7.96997%; height: 29px;"></td>
            <td style="width: 9.2145%; height: 29px;"><span style="background-color: #bfedd2;">49</span></td>
            <td style="width: 9.89163%; height: 29px;"><span style="background-color: #bfedd2;">21</span></td>
            <td style="width: 8.0335%; height: 29px;"></td>
            <td style="width: 8.73384%; height: 29px;"><span style="background-color: #bfedd2;">37</span></td>
            <td style="width: 7.93917%; height: 29px;"><span style="background-color: #fbeeb8;">39</span></td>
            <td style="width: 8.80501%; height: 29px;"></td>
            <td style="width: 11.3262%; height: 29px;"><span style="background-color: #fbeeb8;">25</span></td>
            <td style="width: 11.1491%; height: 29px;"></td>
            <td style="width: 29.384%; height: 29px;"><span style="background-color: #fbeeb8;">46</span></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>6</strong></td>
            <td style="width: 7.96997%; height: 29px;"><span style="background-color: #eccafa;">48</span></td>
            <td style="width: 9.2145%; height: 29px;"></td>
            <td style="width: 9.89163%; height: 29px;"><span style="background-color: #eccafa;">33</span></td>
            <td style="width: 8.0335%; height: 29px;"></td>
            <td style="width: 8.73384%; height: 29px;"><span style="background-color: #eccafa;">43</span></td>
            <td style="width: 7.93917%; height: 29px;"><span style="background-color: #c2e0f4;">41</span></td>
            <td style="width: 8.80501%; height: 29px;"></td>
            <td style="width: 11.3262%; height: 29px;"><span style="background-color: #c2e0f4;">29</span></td>
            <td style="width: 11.1491%; height: 29px;"><span style="background-color: #c2e0f4;">50</span></td>
            <td style="width: 29.384%; height: 29px;"></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>7</strong></td>
            <td style="width: 7.96997%; height: 29px;"></td>
            <td style="width: 9.2145%; height: 29px;"><span style="background-color: #eccafa;">16</span></td>
            <td style="width: 9.89163%; height: 29px;"></td>
            <td style="width: 8.0335%; height: 29px;"><span style="background-color: #eccafa;">13</span></td>
            <td style="width: 8.73384%; height: 29px;"></td>
            <td style="width: 7.93917%; height: 29px;"></td>
            <td style="width: 8.80501%; height: 29px;"><span style="background-color: #c2e0f4;">9</span></td>
            <td style="width: 11.3262%; height: 29px;"></td>
            <td style="width: 11.1491%; height: 29px;"><span style="background-color: #c2e0f4;">10</span></td>
            <td style="width: 29.384%; height: 29px;"></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>8</strong></td>
            <td style="width: 7.96997%; height: 29px;"><span style="background-color: #eccafa;">36</span></td>
            <td style="width: 9.2145%; height: 29px;"></td>
            <td style="width: 9.89163%; height: 29px;"><span style="background-color: #eccafa;">20</span></td>
            <td style="width: 8.0335%; height: 29px;"></td>
            <td style="width: 8.73384%; height: 29px;"><span style="background-color: #eccafa;">34</span></td>
            <td style="width: 7.93917%; height: 29px;"><span style="background-color: #c2e0f4;">30</span></td>
            <td style="width: 8.80501%; height: 29px;"></td>
            <td style="width: 11.3262%; height: 29px;"><span style="background-color: #c2e0f4;">19</span></td>
            <td style="width: 11.1491%; height: 29px;"></td>
            <td style="width: 29.384%; height: 29px;"><span style="background-color: #c2e0f4;">32</span></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>9</strong></td>
            <td style="width: 7.96997%; height: 29px;"></td>
            <td style="width: 9.2145%; height: 29px;"><span style="background-color: #eccafa;">15</span></td>
            <td style="width: 9.89163%; height: 29px;"></td>
            <td style="width: 8.0335%; height: 29px;"><span style="background-color: #eccafa;">14</span></td>
            <td style="width: 8.73384%; height: 29px;"><span style="background-color: #eccafa;">52</span></td>
            <td style="width: 7.93917%; height: 29px;"></td>
            <td style="width: 8.80501%; height: 29px;"><span style="background-color: #c2e0f4;">12</span></td>
            <td style="width: 11.3262%; height: 29px;"></td>
            <td style="width: 11.1491%; height: 29px;"><span style="background-color: #c2e0f4;">11</span></td>
            <td style="width: 29.384%; height: 29px;"></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>10</strong></td>
            <td style="width: 7.96997%; height: 29px;"><span style="background-color: #eccafa;">44</span></td>
            <td style="width: 9.2145%; height: 29px;"></td>
            <td style="width: 9.89163%; height: 29px;"><span style="background-color: #eccafa;">35</span></td>
            <td style="width: 8.0335%; height: 29px;"></td>
            <td style="width: 8.73384%; height: 29px;"></td>
            <td style="width: 7.93917%; height: 29px;"><span style="background-color: #c2e0f4;">47</span></td>
            <td style="width: 8.80501%; height: 29px;"></td>
            <td style="width: 11.3262%; height: 29px;"><span style="background-color: #c2e0f4;">31</span></td>
            <td style="width: 11.1491%; height: 29px;"></td>
            <td style="width: 29.384%; height: 29px;"><span style="background-color: #c2e0f4;">42</span></td>
        </tr>
    </tbody>
</table>
<p>stuff After we've finished the above, if the fleet has not been completely sunk we have only missed the 2x1.&nbsp; Randomly shoot at spaces with an adjacent empty cells where the remaining ship might be hiding until the fleet is sunk.&nbsp; Whenever a hit occurs, follow up by sinking the ship (and any other ships incidentally identified in the process), and then go back to the algorithm described above.</p>
<h4 style="text-align: center;"><strong>Diagonal Search + Random Checkerboard</strong></h4>
<p>This algorithm combines aspects of the random checkerboard strategy above with the less random search-type strategies focused on identifying the placement of large ships.&nbsp; The first part of the algorithm consists of diagonal searches in the order described here:</p>
<table style="border-collapse: collapse; width: 79.848%; height: 319px; margin-left: auto; margin-right: auto;" border="1">
    <tbody>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"></td>
            <td style="width: 7.96997%; height: 29px;"><strong>A</strong></td>
            <td style="width: 9.2145%; height: 29px;"><strong>B</strong></td>
            <td style="width: 9.89163%; height: 29px;"><strong>C</strong></td>
            <td style="width: 8.96954%; height: 29px;"><strong>D</strong></td>
            <td style="width: 7.64179%; height: 29px;"><strong>E</strong></td>
            <td style="width: 8.71918%; height: 29px;"><strong>F</strong></td>
            <td style="width: 10.209%; height: 29px;"><strong>G</strong></td>
            <td style="width: 10.8582%; height: 29px;"><strong>H</strong></td>
            <td style="width: 10.057%; height: 29px;"><strong>I</strong></td>
            <td style="width: 28.916%; height: 29px;"><strong>J</strong></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>1</strong></td>
            <td style="width: 7.96997%; height: 29px;"></td>
            <td style="width: 9.2145%; height: 29px;"><span style="background-color: #f8cac6;">23</span></td>
            <td style="width: 9.89163%; height: 29px;"></td>
            <td style="width: 8.96954%; height: 29px;"></td>
            <td style="width: 7.64179%; height: 29px;"></td>
            <td style="width: 8.71918%; height: 29px;"><span style="background-color: #f8cac6;">21</span></td>
            <td style="width: 10.209%; height: 29px;"></td>
            <td style="width: 10.8582%; height: 29px;"></td>
            <td style="width: 10.057%; height: 29px;"></td>
            <td style="width: 28.916%; height: 29px; text-align: center;"><span style="background-color: #f8cac6;">9</span></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>2</strong></td>
            <td style="width: 7.96997%; height: 29px;"><span style="background-color: #f8cac6;">24</span></td>
            <td style="width: 9.2145%; height: 29px;"></td>
            <td style="width: 9.89163%; height: 29px;"></td>
            <td style="width: 8.96954%; height: 29px;"></td>
            <td style="width: 7.64179%; height: 29px;"><span style="background-color: #f8cac6;">19</span></td>
            <td style="width: 8.71918%; height: 29px;"></td>
            <td style="width: 10.209%; height: 29px;"></td>
            <td style="width: 10.8582%; height: 29px;"></td>
            <td style="width: 10.057%; height: 29px;"><span style="background-color: #f8cac6;">7</span></td>
            <td style="width: 28.916%; height: 29px;"></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>3</strong></td>
            <td style="width: 7.96997%; height: 29px;"></td>
            <td style="width: 9.2145%; height: 29px;"></td>
            <td style="width: 9.89163%; height: 29px;"></td>
            <td style="width: 8.96954%; height: 29px;"><span style="background-color: #f8cac6;">17</span></td>
            <td style="width: 7.64179%; height: 29px;"></td>
            <td style="width: 8.71918%; height: 29px;"></td>
            <td style="width: 10.209%; height: 29px;"></td>
            <td style="width: 10.8582%; height: 29px;"><span style="background-color: #f8cac6;">5</span></td>
            <td style="width: 10.057%; height: 29px;"></td>
            <td style="width: 28.916%; height: 29px;"></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>4</strong></td>
            <td style="width: 7.96997%; height: 29px;"></td>
            <td style="width: 9.2145%; height: 29px;"></td>
            <td style="width: 9.89163%; height: 29px;"><span style="background-color: #f8cac6;">18</span></td>
            <td style="width: 8.96954%; height: 29px;"></td>
            <td style="width: 7.64179%; height: 29px;"></td>
            <td style="width: 8.71918%; height: 29px;"></td>
            <td style="width: 10.209%; height: 29px;"><span style="background-color: #f8cac6;">3</span></td>
            <td style="width: 10.8582%; height: 29px;"></td>
            <td style="width: 10.057%; height: 29px;"></td>
            <td style="width: 28.916%; height: 29px;"></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>5</strong></td>
            <td style="width: 7.96997%; height: 29px;"></td>
            <td style="width: 9.2145%; height: 29px;"><span style="background-color: #f8cac6;">20</span></td>
            <td style="width: 9.89163%; height: 29px;"></td>
            <td style="width: 8.96954%; height: 29px;"></td>
            <td style="width: 7.64179%; height: 29px;"></td>
            <td style="width: 8.71918%; height: 29px;"><span style="background-color: #f8cac6;">1</span></td>
            <td style="width: 10.209%; height: 29px;"></td>
            <td style="width: 10.8582%; height: 29px;"></td>
            <td style="width: 10.057%; height: 29px;"></td>
            <td style="width: 28.916%; height: 29px;"><span style="background-color: #f8cac6;">15</span></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>6</strong></td>
            <td style="width: 7.96997%; height: 29px;"><span style="background-color: #f8cac6;">22</span></td>
            <td style="width: 9.2145%; height: 29px;"></td>
            <td style="width: 9.89163%; height: 29px;"></td>
            <td style="width: 8.96954%; height: 29px;"></td>
            <td style="width: 7.64179%; height: 29px;"><span style="background-color: #f8cac6;">2</span></td>
            <td style="width: 8.71918%; height: 29px;"></td>
            <td style="width: 10.209%; height: 29px;"></td>
            <td style="width: 10.8582%; height: 29px;"></td>
            <td style="width: 10.057%; height: 29px;"><span style="background-color: #f8cac6;">13</span></td>
            <td style="width: 28.916%; height: 29px;"></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>7</strong></td>
            <td style="width: 7.96997%; height: 29px;"></td>
            <td style="width: 9.2145%; height: 29px;"></td>
            <td style="width: 9.89163%; height: 29px;"></td>
            <td style="width: 8.96954%; height: 29px;"><span style="background-color: #f8cac6;">4</span></td>
            <td style="width: 7.64179%; height: 29px;"></td>
            <td style="width: 8.71918%; height: 29px;"></td>
            <td style="width: 10.209%; height: 29px;"></td>
            <td style="width: 10.8582%; height: 29px;"><span style="background-color: #f8cac6;">11</span></td>
            <td style="width: 10.057%; height: 29px;"></td>
            <td style="width: 28.916%; height: 29px;"></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>8</strong></td>
            <td style="width: 7.96997%; height: 29px;"></td>
            <td style="width: 9.2145%; height: 29px;"></td>
            <td style="width: 9.89163%; height: 29px;"><span style="background-color: #f8cac6;">6</span></td>
            <td style="width: 8.96954%; height: 29px;"></td>
            <td style="width: 7.64179%; height: 29px;"></td>
            <td style="width: 8.71918%; height: 29px;"></td>
            <td style="width: 10.209%; height: 29px;"><span style="background-color: #f8cac6;">12</span></td>
            <td style="width: 10.8582%; height: 29px;"></td>
            <td style="width: 10.057%; height: 29px;"></td>
            <td style="width: 28.916%; height: 29px;"></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>9</strong></td>
            <td style="width: 7.96997%; height: 29px;"></td>
            <td style="width: 9.2145%; height: 29px;"><span style="background-color: #f8cac6;">8</span></td>
            <td style="width: 9.89163%; height: 29px;"></td>
            <td style="width: 8.96954%; height: 29px;"></td>
            <td style="width: 7.64179%; height: 29px;"></td>
            <td style="width: 8.71918%; height: 29px;"><span style="background-color: #f8cac6;">14</span></td>
            <td style="width: 10.209%; height: 29px;"></td>
            <td style="width: 10.8582%; height: 29px;"></td>
            <td style="width: 10.057%; height: 29px;"></td>
            <td style="width: 28.916%; height: 29px;"><span style="background-color: #f8cac6;">25</span></td>
        </tr>
        <tr style="height: 29px;">
            <td style="width: 5%; height: 29px;"><strong>10</strong></td>
            <td style="width: 7.96997%; height: 29px;"><span style="background-color: #f8cac6;">10</span></td>
            <td style="width: 9.2145%; height: 29px;"></td>
            <td style="width: 9.89163%; height: 29px;"></td>
            <td style="width: 8.96954%; height: 29px;"></td>
            <td style="width: 7.64179%; height: 29px;"><span style="background-color: #f8cac6;">16</span></td>
            <td style="width: 8.71918%; height: 29px;"></td>
            <td style="width: 10.209%; height: 29px;"></td>
            <td style="width: 10.8582%; height: 29px;"></td>
            <td style="width: 10.057%; height: 29px;"><span style="background-color: #f8cac6;">26</span></td>
            <td style="width: 28.916%; height: 29px;"></td>
        </tr>
    </tbody>
</table>
<p>Now imagine that we color the whole board with red and black squares in a checkerboard style.&nbsp; Notice that all of the planned shots above occur on <span style="color: #e03e2d;"><strong>red</strong></span> squares.&nbsp; If the enemy fleet is not yet sunk, continue randomly choosing <span style="color: #e03e2d;"><strong>red</strong></span> squares until the fleet is sunk.&nbsp; Whenever a hit occurs, follow up by sinking the ship (and any other ships incidentally identified in the process), and then go back to the algorithm described above.</p>
<p>&nbsp;</p>


