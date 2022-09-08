const btn1 = document.getElementById('undo');
const btn2 = document.getElementById('clear');
const btn3 = document.getElementById('simulate');
const btn4 = document.getElementById('simulate100');
const stat = document.getElementById('statistics');

const rainbow = ['red','orange','yellow','green','blue','rebeccapurple','violet'];

function change() {      
document.body.style.background = rainbow[Math.floor(7*Math.random())];
}
btn1.addEventListener('click', undoFiringOrder);
btn2.addEventListener('click', clearFiringOrder);
btn3.addEventListener('click', simulateBattle);
btn4.addEventListener('click', simulate100Battles);


//Sets important constants and variables

const firingOrder = document.getElementById("firing-order");
const battleshipFleet = document.getElementById("battleship-fleet");
let firingRows = document.getElementsByClassName("gridRow");
let simulRows = document.getElementsByClassName("simRow");
let cells = document.getElementsByClassName("cell");
let bells = document.getElementsByClassName("bell");

let nx = 10;
let ny = 10;
let waterColor = '#29a4c3';
let hitColor = '#993333';
let missColor = '#000066';
const ship_lengths = [5,4,3,3,2];
const ship_strings = ['C','b','c','s','d'];

main();
function main() {
  for (r = 0; r < nx; r++) {
    let row = document.createElement("div");
    firingOrder.appendChild(row).className = "gridRow";
  };

  for (i = 0; i < firingRows.length; i++) {
    for (j = 0; j < ny; j++) {
      let newCell = document.createElement("div");
      newCell.style.background = waterColor;
      newCell.innerHTML = '-';
      newCell.addEventListener('click',setFiringOrder);
      firingRows[i].appendChild(newCell).className = "cell";
    };
  };

  for (r = 0; r < nx; r++) {
    let row = document.createElement("div");
    battleshipFleet.appendChild(row).className = "simRow";
  };

  for (i = 0; i < simulRows.length; i++) {
    for (j = 0; j < ny; j++) {
      let newCell = document.createElement("div");
      newCell.style.background = waterColor;
      newCell.innerHTML = '-';
      simulRows[i].appendChild(newCell).className = "cell";
    };
  };
}


let _nshots = 1;
let stat_sum = 0;
let stat_num = 0;

function setFiringOrder() {
  if(this.innerHTML == '-') {
    this.innerHTML = _nshots;
    _nshots = _nshots + 1;
  };
}

function undoFiringOrder() {
  if(_nshots == 0) return;
  for(i = 0; i < cells.length; i++) {
    if(cells[i].innerHTML == _nshots-1) {
      cells[i].innerHTML = '-';
      _nshots = _nshots -1;
      break;
    };
  };
  stat_num = 0;
  stat_sum = 0;
}

function clearFiringOrder() {
  for(i = 0; i < cells.length; i++) {
    cells[i].innerHTML = '-';
    cells[i].style.background = waterColor;
  };
  _nshots = 1;
  stat_num = 0;
  stat_sum = 0;
}

function generateRandomFleet() {
  const dx = [1,0,-1,0];
  const dy = [0,1,0,-1];


  // clear any previous fleet
  for(i = nx*ny; i < cells.length; i++) {
    cells[i].innerHTML = '-';
    cells[i].style.background = waterColor;
  };

  for(i = 0; i < ship_lengths.length; i++) {
    //window.alert(ship_lengths.length)
    // place ith ship
    len = ship_lengths[i]
    let ship_placed = false;
    while(ship_placed == false) {
      // get random position and direction
      ship_placed = true;
      dir = Math.floor(Math.random() * 4);
      x = Math.floor(Math.random() * 10);
      y = Math.floor(Math.random() * 10);

      for(j = 0; j < len; j++) {
        x1 = x + dx[dir]*j;
        y1 = y + dy[dir]*j;
	if(x1 < 0 || x1 >= nx || y1 < 0 || y1 >= ny) {
	  ship_placed = false;
          break;
	};
	if(cells[nx*ny + nx*y1 + x1].innerHTML !== '-') {
          ship_placed = false;
          break;
	};
      };

      if(ship_placed) {
        for(j = 0; j < len; j++) {
          x1 = x + dx[dir]*j;
          y1 = y + dy[dir]*j;
          cells[nx*ny + nx*y1 + x1].innerHTML = ship_strings[i];
        };
      };

    };
  };
}

function shipIsSunk(ship_char) {
  for(i = nx*ny; i < cells.length; i++) {
    if(cells[i].innerHTML == ship_char && cells[i].style.background == cells[0].style.background) return false;
  };

  return true;
}

function sinkShip(x,y) {
  // do obvious search pattern to sink a ship we hit at (x,y)
  
  const dx = [1,0,-1,0];
  const dy = [0,1,0,-1];

  let shot_cnt = 0;
  let iter_max = 1000;
  let iter = 0;

  let flavor = cells[nx*ny + nx*y + x].innerHTML;

  let sunk = false
  while(sunk == false) {
  for(dir = 0; dir < 4; dir++) {
    for(i = 1; i < nx; i++) {
      let x1 = x + dx[dir]*i;
      let y1 = y + dy[dir]*i;
      let idx = nx*ny + nx*y1 + x1;
      if(x1 < 0 || x1 >= nx || y1 < 0 || y1 >= ny) {
        break;
      };
      if(cells[idx].style.background !== cells[0].style.background) {
        break;
      };
      if(cells[idx].style.background == cells[0].style.background) {
        shot_cnt = shot_cnt + 1;
        if(cells[idx].innerHTML == '-') {
          cells[idx].style.background = missColor;
	  break;
	};
        if(cells[idx].innerHTML !== '-') {
          cells[idx].style.background = hitColor;
          if(cells[idx].innerHTML !== flavor) {
	    let extra_shots = 0;
            extra_shots = sinkShip(x1,y1);
	    shot_cnt = shot_cnt + extra_shots;
	    break;
	  };
	};
      };
    };

    sunk = shipIsSunk(flavor);
    iter ++;
    if(sunk) break;
  };
    if(iter > iter_max) {
      alert("max iterations exceeded");
      break;
    };
  };

  return shot_cnt;
}

function sinkFleet() {

  let shot_cnt = 0;
  let fleet_sunk = false;
  while(fleet_sunk == false) {
    let idx = 0;

    // find the location of the next shot; if unspecified then
    // choose the next shot location randomly from available
    let minval = 100;
    var indices = [];
    for(i = nx*ny; i < cells.length; i++) {
      if(cells[i].style.background == cells[0].style.background) {
        indices.push(i);
        if(cells[i-nx*ny].innerHTML !== '-') {
          if(cells[i-nx*ny].innerHTML < minval) {
            minval = cells[i-nx*ny].innerHTML;
	    idx = i;
	  };
        };
      };
    };
    if(minval == 100) {
      k = Math.floor(Math.random()*indices.length)
      idx = indices[k];
    }

    x = idx % nx;
    y = Math.floor((idx-x)/nx - ny);


    let num_hits = 0;
    let extra_shots = 0;

    if(cells[idx].style.background == cells[0].style.background) {

      // update shot count
      shot_cnt = shot_cnt + 1;
      if(cells[idx].innerHTML == '-') {
        cells[idx].style.background = missColor;
      };
      if(cells[idx].innerHTML !== '-') {
        cells[idx].style.background = hitColor;
        extra_shots = sinkShip(x,y);
	for(i=nx*ny; i < cells.length; i++) {
          if(cells[idx].style.background == cells[i].style.background) {
            num_hits ++;
	  }
	};
      };
      shot_cnt = shot_cnt + extra_shots;
    };


    // check if fleet is sunk
    if(num_hits == 17) {
      fleet_sunk = true;
      break;
    };

  };

  return shot_cnt;
}

function updateStatistics(shot_cnt) {
  stat_sum = stat_sum + shot_cnt;
  stat_num ++;
  stat_avg = stat_sum/stat_num;
  stat.innerHTML  = 'Shots for this fleet = ' + shot_cnt.toString() + '<br/>';
  stat.innerHTML += 'Number of fleets sim = ' + stat_num.toString() + '<br/>';
  stat.innerHTML += 'Average shots per fleet = ' + stat_avg.toString();
}

function simulateBattle() {
  generateRandomFleet();
  shot_cnt = sinkFleet();
  updateStatistics(shot_cnt);
}

function simulate100Battles() {
  for(ii=0; ii < 100; ii++) {
    simulateBattle();
  };
}





