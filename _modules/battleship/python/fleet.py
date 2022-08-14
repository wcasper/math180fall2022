#!/usr/bin/python

import random
import numpy as np

class battleship_ship:
  _type = ""    # battleship name
  _len  = 0     # ship length
  _pos  = ""    # ship starting position
  _ori  = ""    # ship orientation
  _sunk = False # whether the ship is sunk

  def __init__(self,n,type_str):
    self._type = type_str
    self._len = n
    self._sunk = False
 
  def ori2diff(self):
    dx = 0
    dy = 0
    if(self._ori == "N"):
        dx = 0
        dy = 1
    elif(self._ori == "E"):
        dx = 1
        dy = 0
    elif(self._ori == "S"):
        dx = 0
        dy = -1
    elif(self._ori == "W"):
        dx = -1
        dy = 0
    return [dx,dy]

class battleship_fleet:
  _ships = []
  _index = {}
  _sunk = False

  def __init__(self):
    self._ships.append(battleship_ship(5,"Carrier"))
    self._ships.append(battleship_ship(4,"battleship"))
    self._ships.append(battleship_ship(3,"cruiser"))
    self._ships.append(battleship_ship(3,"submarine"))
    self._ships.append(battleship_ship(2,"destroyer"))
    self._index = {'C':0,'b':1,'c':2,'s':3,'d':4}
    self._sunk = False

  def fleet2matrix(self):
    fleetmatrix = np.array([['.']*10]*10)
    for ship in self._ships:
      x = int(ord(ship._pos[0])-ord('a')+1)   # convert a->1, b->2, etc.
      y = int(ship._pos[1:])                  # convert remaining string to integer
      [dx,dy] = ship.ori2diff()
      for n in range(ship._len):
        fleetmatrix[x-1][10-y] = ship._type[0]  # first letter of ship type
        x += dx
        y += dy

    return fleetmatrix

  def smallest_ship(self):
    lmin = 10
    for ship in self._ships:
      if (not ship._sunk and ship._len < lmin):
        lmin = ship._len
    return lmin

  def pretty_print(self):
    fleetmatrix = self.fleet2matrix()
    for line in fleetmatrix:
      print(line)

  def scatter(self):
    self._sunk = False
    for ship in self._ships:
      ship._sunk = False
      
    fleetmatrix = np.array([['.']*10]*10)
    for ship in self._ships:
      illegal_position = True
      while(illegal_position):
        dx = 0
        dy = 0
        x = random.randint(1,10)
        y = random.randint(1,10)
        z = random.randint(1,4)
        if(z == 1):
          ship._ori = "N"
        elif(z == 2):
          ship._ori = "E"
        elif(z == 3):
          ship._ori = "S"
        elif(z == 4):
          ship._ori = "W"
        dx,dy = ship.ori2diff()
        x0 = x
        y0 = y
        ship._pos = str(chr(x-1+ord('a'))) + str(y)
        # check if the position is legal
        illegal_position = False
        for n in range(ship._len):
          if (x < 1 or x > 10 or y < 1 or y > 10):
            illegal_position = True
            break
          elif (fleetmatrix[x-1,10-y] != '.'):
            illegal_position = True
            break
          x += dx
          y += dy

      x = x0
      y = y0
      for n in range(ship._len):
        fleetmatrix[x-1,10-y] = ship._type[0]
        x += dx
        y += dy

  def update_status(self, board_state):
    fleet_is_sunk = True
    for idx in range(len(self._ships)):
      ship = self._ships[idx]
      x = int(ord(ship._pos[0])-ord('a')+1) 
      y = int(ship._pos[1:])
      [dx,dy] = ship.ori2diff()
      ship_is_sunk = True
      for n in range(ship._len):
        if(board_state[x-1][10-y] != 'H'):
          ship_is_sunk = False
          fleet_is_sunk = False
          break
        x += dx
        y += dy
      self._ships[idx]._sunk = ship_is_sunk
    self._sunk = fleet_is_sunk
        
