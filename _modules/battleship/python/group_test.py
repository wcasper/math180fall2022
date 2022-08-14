#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random
import sys

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

def group1_algorithm(_fleet):
  fleet_matrix = _fleet.fleet2matrix()

  board_state = np.array([['.']*10]*10)
  while(not _fleet._sunk):
    x0 = random.randint(0,4)
    y0 = random.randint(5,9)

    if(True):
      xarr = [x0, x0, x0+5,x0+5]
      yarr = [y0, y0-5,y0-5,y0]
      for quad in range(4):
        x = xarr[quad]
        y = yarr[quad]
        if(board_state[x,y] == '.'):
          if fleet_matrix[x,y] == '.':
            board_state[x,y] = 'M'
          else:
            board_state[x,y] = 'H'
            board_state = sink_algorithm(board_state, _fleet, x, y)
            _fleet.update_status(board_state)
  return board_state

def group2_algorithm(_fleet):
  fleet_matrix = _fleet.fleet2matrix()

  board_state = np.array([['.']*10]*10)

  # choose random center entry
  x = random.choice([4,5])
  y = random.choice([4,5])

  # define knight moves
  knight = [[-1,-2],[-1,2],[1,-2],[1,2],[-2,-1],[-2,1],[2,-1],[2,1]]

  while(not _fleet._sunk):
    if(board_state[x,y] == '.'):
      if fleet_matrix[x,y] == '.':
        board_state[x,y] = 'M'
      else:
        board_state[x,y] = 'H'
        board_state = sink_algorithm(board_state, _fleet, x, y)
        _fleet.update_status(board_state)
    # get next x,y point
    if (not _fleet._sunk):
      moveorder = list(range(8))
      random.shuffle(moveorder)
      for k in range(8):
        x1 = x + knight[moveorder[k]][0]
        y1 = y + knight[moveorder[k]][1]
        if(x1>=0 and x1 < 10 and y1 >=0 and y1 < 10):
          if(board_state[x1,y1] == '.'):
            x = x1
            y = y1
            break
      # if we couldn't find a free knight move, just pick a random open spot
      while(board_state[x,y] != '.'):
        x = random.randint(0,9)
        y = random.randint(0,9)
      
  return board_state


def group3_algorithm(_fleet):
  fleet_matrix = _fleet.fleet2matrix()

  sequence = [[5,5],[5,4],[4,4],[4,5],[9,0],[0,0],[0,9],[9,9],[3,4],[2,3],[3,2],[4,3],[5,2],[6,3],[7,2],[7,4],[6,5],[7,6],[6,7],[5,6],[4,7],[3,6],[2,7],[2,5],[1,3],[1,6],[8,3],[8,6],[3,1],[6,1],[3,8],[6,8]]
  nseq = len(sequence)

  board_state = np.array([['.']*10]*10)
  cycle = 0
  while(not _fleet._sunk):
    if(cycle < nseq):
      [x,y] = sequence[cycle]
    else:
      while(board_state[x,y] != '.' or (x+y)%2 == 0):
        x = random.randint(0,9)
        y = random.randint(0,9)
    if(board_state[x,y] == '.'):
      if fleet_matrix[x,y] == '.':
        board_state[x,y] = 'M'
      else:
        board_state[x,y] = 'H'
        board_state = sink_algorithm(board_state, _fleet, x, y)
        _fleet.update_status(board_state)
    cycle += 1
  return board_state

def group4_algorithm(_fleet):
  fleet_matrix = _fleet.fleet2matrix()

  collection1 = [[5,5],[5,4],[4,4],[4,5]]
  collection2 = [[0,0],[1,1],[2,2],[3,3],[6,6],[7,7],[8,8],[9,9],[0,9],[1,8],[2,7],[3,6],[6,3],[7,2],[8,1],[9,0]]
  collection3 = [[2,4],[2,5],[4,2],[5,2],[4,7],[5,7],[7,4],[7,5]]
  collection4 = [[0,4],[0,5],[4,0],[4,5],[4,9],[5,9],[9,4],[9,5],[2,0],[0,2],[0,7],[7,0],[2,9],[9,2],[9,7],[7,9]]

  collections = [collection1,collection2,collection3,collection4]
  ncollections = len(collections)

  board_state = np.array([['.']*10]*10)
  for k in range(ncollections):
    collection = collections[k]
    ncollection = len(collection)
    random.shuffle(collection)

    for j in range(ncollection):
      [x,y] = collection[j]
      if(board_state[x,y] == '.'):
        if fleet_matrix[x,y] == '.':
          board_state[x,y] = 'M'
        else:
          board_state[x,y] = 'H'
          board_state = sink_algorithm(board_state, _fleet, x, y)
          _fleet.update_status(board_state)
      if(_fleet._sunk):
        break
    if(_fleet._sunk):
      break
  while(not _fleet._sunk):
    x = random.randint(0,9)
    y = random.randint(0,9)
    if(board_state[x,y] == '.'):
      if fleet_matrix[x,y] == '.':
        board_state[x,y] = 'M'
      else:
        board_state[x,y] = 'H'
        board_state = sink_algorithm(board_state, _fleet, x, y)
        _fleet.update_status(board_state)

  return board_state

def group5_algorithm(_fleet):
  fleet_matrix = _fleet.fleet2matrix()

  misses = []
  hits = []
  smallest_ship = 2

  # initial shot
  x = 4
  y = 4

  board_state = np.array([['.']*10]*10)
  while(not _fleet._sunk):
    if(board_state[x,y] == '.'):
      if fleet_matrix[x,y] == '.':
        board_state[x,y] = 'M'
        misses.append([x,y])
      else:
        board_state[x,y] = 'H'
        board_state = sink_algorithm(board_state, _fleet, x, y)
        _fleet.update_status(board_state)
        hits.append([x,y])
        smallest_ship = _fleet.smallest_ship()

    mtargets = []
    htargets = []
    mhtargets = [mtargets,htargets]
    mstarts = misses.copy()
    random.shuffle(mstarts)
    hstarts = hits.copy()
    random.shuffle(hstarts)
    mhstarts = [mstarts,hstarts]
    if(not _fleet._sunk):
      # choose next space
      for it in range(2):
        targets = mhtargets[it]
        starts = mhstarts[it]
        for [x,y] in starts:
          if len(targets) > 0:
            break
          for dx in [-1,1]:
            for dy in [-1,1]:
              for j in range(0,smallest_ship+1):
                k = smallest_ship+1-j
                x1 = x + dx*j
                y1 = y + dy*k
                if(0<=x1 and x1 < 10 and 0<= y1 and y1 < 10):
                  if(board_state[x1,y1] == '.'):
                    # check directions
                    dmax = 1
                    directions = [[1,0],[0,1]]
                    for jj in range(2):
                      [dx1,dy1] = directions[jj]
                      dist = 0
                      for kk in range(1-smallest_ship,smallest_ship):
                        if(0<=x1+dx1*kk and x1+dx1*kk < 10 and 0<= y1+dy1*kk and y1+dy1*kk < 10):
                          if(board_state[x1+dx1*kk,y1+dy1*kk] == '.'):
                            dist += 1
                      if (dmax < dist):
                        dmax = dist
                    if(dmax >= smallest_ship):
                      targets.append([x1,y1])
        if(len(targets)>0):  # there's a good target already
          break
                     
      if(len(mtargets)==0 and len(htargets)==0):
        _fleet.pretty_print()
        print("ERROR !!!, %i\n" % smallest_ship)
        print(board_state)
        sys.exit(0)
      elif (len(mtargets)>0):
        [x,y] = random.choice(mtargets)
      else:
        [x,y] = random.choice(htargets)

  return board_state

def group6_algorithm(_fleet):
  fleet_matrix = _fleet.fleet2matrix()

  collection1 = [[3,3],[3,4],[3,5],[3,6],[6,3],[6,4],[6,5],[6,6],[4,2],[5,2],[4,7],[5,7]]
  collection2 = [[0,3],[0,4],[0,5],[0,6],[9,3],[9,4],[9,5],[9,6],[3,0],[4,0],[5,0],[6,0],[3,9],[4,9],[5,9],[6,9],[2,1],[1,2],[8,7],[7,8],[1,7],[2,8],[7,1],[8,2]]

  collections = [collection1,collection2]
  ncollections = len(collections)

  board_state = np.array([['.']*10]*10)
  for k in range(ncollections):
    collection = collections[k]
    ncollection = len(collection)
    random.shuffle(collection)

    for j in range(ncollection):
      [x,y] = collection[j]
      if(board_state[x,y] == '.'):
        if fleet_matrix[x,y] == '.':
          board_state[x,y] = 'M'
        else:
          board_state[x,y] = 'H'
          board_state = sink_algorithm(board_state, _fleet, x, y)
          _fleet.update_status(board_state)
      if(_fleet._sunk):
        break
    if(_fleet._sunk):
      break
  while(not _fleet._sunk):
    x = random.randint(0,9)
    y = random.randint(0,9)
    if(board_state[x,y] == '.'):
      if fleet_matrix[x,y] == '.':
        board_state[x,y] = 'M'
      else:
        board_state[x,y] = 'H'
        board_state = sink_algorithm(board_state, _fleet, x, y)
        _fleet.update_status(board_state)

  return board_state

def group8_algorithm(_fleet):
  fleet_matrix = _fleet.fleet2matrix()

  board_state = np.array([['.']*10]*10)

  directions1 = [[-2,0],[0,2],[2,0],[0,-2]]
  directions2 = [[-2,0],[0,-2],[2,0],[0,2]]

  x = 4
  y = 4

  count = 0
  dcount = 0
  idir = 0
  inner_spiral = False
  while(not _fleet._sunk):
    if (x < 0 or y < 0):
      x = 5
      y = 5
      inner_spiral = True
      count = 0
      dcount = 0
      idir = 0

    if(board_state[x,y] == '.'):
      if fleet_matrix[x,y] == '.':
        board_state[x,y] = 'M'
      else:
        board_state[x,y] = 'H'
        board_state = sink_algorithm(board_state, _fleet, x, y)
        _fleet.update_status(board_state)

    if(inner_spiral):
      [dx,dy] = directions2[idir]
    else:
      [dx,dy] = directions1[idir]
    x = x + dx
    y = y + dy

    dcount += 1
    if int(count/2) + 1 <= dcount:
      # change direction
      idir = (idir+1)%4
      dcount = 0
      count += 1

  return board_state

def group7_algorithm(_fleet):
  fleet_matrix = _fleet.fleet2matrix()

  collection1 = [[4,4],[3,3],[2,2],[1,1],[0,0]]
  collection2 = [[4,5],[3,6],[2,7],[1,8],[0,9]]
  collection3 = [[5,5],[6,6],[7,7],[8,8],[9,9]]
  collection4 = [[5,4],[6,3],[7,2],[8,1],[9,0]]

  collections = [collection1,collection2,collection3,collection4]
  ncollections = len(collections)

  board_state = np.array([['.']*10]*10)
  for k in range(ncollections):
    collection = collections[k]
    ncollection = len(collection)
    random.shuffle(collection)

    for j in range(ncollection):
      [x,y] = collection[j]
      if(board_state[x,y] == '.'):
        if fleet_matrix[x,y] == '.':
          board_state[x,y] = 'M'
        else:
          board_state[x,y] = 'H'
          board_state = sink_algorithm(board_state, _fleet, x, y)
          _fleet.update_status(board_state)
      if(_fleet._sunk):
        break
    if(_fleet._sunk):
      break

  while(not _fleet._sunk):
    smallest_ship = _fleet.smallest_ship()
    max_mod = 0
    max_cnt = 0
    cnt = 0
    for k in range(0,10):
      for j in range(k,10+k,smallest_ship):
        if(board_state[j%10,k] != '.'):
          cnt += 1
    max_cnt = cnt
    for mod in range(1,smallest_ship):
      cnt = 0
      for k in range(0,10):
        for j in range(k+mod,10+k+mod,smallest_ship):
          if(board_state[j%10,k] != '.'):
            cnt += 1
    if max_cnt < cnt:
      max_cnt = cnt
      max_mod = mod

    x = random.randint(0,9)
    y = random.randint(0,9)
    if(board_state[x,y] == '.' and (x-y)%smallest_ship == mod):
      if fleet_matrix[x,y] == '.':
        board_state[x,y] = 'M'
      else:
        board_state[x,y] = 'H'
        board_state = sink_algorithm(board_state, _fleet, x, y)
        _fleet.update_status(board_state)

  return board_state

def random_algorithm(_fleet):
  fleet_matrix = _fleet.fleet2matrix()

  board_state = np.array([['.']*10]*10)
  while(not _fleet._sunk):
    x = random.randint(0,9)
    y = random.randint(0,9)
    if(board_state[x,y] == '.'):
      if fleet_matrix[x,y] == '.':
        board_state[x,y] = 'M'
      else:
        board_state[x,y] = 'H'
        board_state = sink_algorithm(board_state, _fleet, x, y)
        _fleet.update_status(board_state)
  return board_state


shot_avg = 0
ntrials = 10000

algorithms = [random_algorithm, group1_algorithm, group2_algorithm, group3_algorithm, group4_algorithm, group5_algorithm, group6_algorithm, group7_algorithm, group8_algorithm]
algorithm_names = ["Pure Random", "Counter-Clockwise Search", "Dark Knight", "Checkered Quadrants", "Spider Web", "Iterated Guess", "Pentagons", "X factor", "Swirl"]
for alg_idx in range(8,len(algorithms)):
  algorithm = algorithms[alg_idx]
  algorithm_name = algorithm_names[alg_idx]
  for k in range(ntrials):
    testfleet.scatter()
    fleet_matrix = testfleet.fleet2matrix()

    board_state = algorithm(testfleet)
    nshots = 0
    for i in range(10):
      for j in range(10):
        if(board_state[i,j] != '.'):
          nshots += 1
    shot_avg += nshots
    #print("nshots=",nshots)

  shot_avg /= ntrials
  print(algorithm_name, shot_avg)


