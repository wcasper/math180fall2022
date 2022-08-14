#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random

from fleet import *

testfleet = battleship_fleet()
testfleet.scatter()

def sink_algorithm(board_state, _fleet, x1, y1):
  new_targets = []

  fleet_matrix = _fleet.fleet2matrix()

  # iterate through the adjacent squares
  for [dx,dy] in [[1,0],[0,1],[0,-1],[-1,0]]:
    if _fleet._ships[_fleet._index[fleet_matrix[x1,y1]]]._sunk:
      break
    x = x1+dx
    y = y1+dy
    # continue in direction until miss or no more board or ship sunk
    go_immediately_to_opposite = False
    for n in range(10):
      if _fleet._ships[_fleet._index[fleet_matrix[x1,y1]]]._sunk:
        break
      elif(x > 9 or x < 0 or y > 9 or y < 0):
        break
      elif(board_state[x,y] == '.'):
        if(fleet_matrix[x,y] == '.'):
          board_state[x,y] = 'M'
          break
        elif(fleet_matrix[x,y] != fleet_matrix[x1,y1]):
        # accidently hit an additional target!
          board_state[x,y] = 'H'
          go_immediately_to_opposite = True
          _fleet.update_status(board_state)
          if(not _fleet._ships[_fleet._index[fleet_matrix[x,y]]]._sunk):
            new_targets.append([x,y])
        else:
        # hit the same boat, woot!
          board_state[x,y] = 'H'
          go_immediately_to_opposite = True
          _fleet.update_status(board_state)
      else:
        break

      x += dx
      y += dy

    # try other direction if we have to hits in a straight line
    if(go_immediately_to_opposite):
      x = x1-dx
      y = y1-dy
      # continue in direction until miss or no more board or ship sunk
      for n in range(10):
        go_immediately_to_opposite = False
        if _fleet._ships[_fleet._index[fleet_matrix[x1,y1]]]._sunk:
          break
        elif(x > 9 or x < 0 or y > 9 or y < 0):
          break
        elif(board_state[x,y] == '.'):
          if(fleet_matrix[x,y] == '.'):
            board_state[x,y] = 'M'
            break
          elif(fleet_matrix[x,y] != fleet_matrix[x1,y1]):
          # accidently hit an additional target!
            board_state[x,y] = 'H'
            go_immediately_to_opposite = True
            _fleet.update_status(board_state)
            if(not _fleet._ships[_fleet._index[fleet_matrix[x,y]]]._sunk):
              new_targets.append([x,y])
          else:
          # hit the same boat, woot!
            board_state[x,y] = 'H'
            go_immediately_to_opposite = True
            _fleet.update_status(board_state)
        else:
          break

        x -= dx
        y -= dy

  # sink any new targets we accidentally found
  for target in new_targets:
    [x,y] = target
    board_state = sink_algorithm(board_state, _fleet, x, y)
    _fleet.update_status(board_state)
  return board_state

def random_algorithm(_fleet):
  fleet_matrix = _fleet.fleet2matrix()

  board_state = np.array([['.']*10]*10)
  while(not _fleet._sunk):
    x = random.randint(0,9)
    y = random.randint(0,9)
    if fleet_matrix[x,y] == '.':
      board_state[x,y] = 'M'
    else:
      board_state[x,y] = 'H'
      board_state = sink_algorithm(board_state, _fleet, x, y)
      _fleet.update_status(board_state)
  return board_state


shot_avg = 0
ntrials = 10000
for k in range(ntrials):
  testfleet.scatter()
  fleet_matrix = testfleet.fleet2matrix()

  board_state = random_algorithm(testfleet)
  nshots = 0
  for i in range(10):
    for j in range(10):
      if(board_state[i,j] != '.'):
        nshots += 1
  print("shots taken:", nshots)
  shot_avg += nshots

shot_avg /= ntrials
print(shot_avg)


