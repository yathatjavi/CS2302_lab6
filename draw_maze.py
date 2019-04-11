# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:56:23 2019

@author: yatha
"""

# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joiniung any two cells
# Programmed by Olac Fuentes
# Last modified March 28, 2019

import matplotlib.pyplot as plt
import numpy as np
import random
import dsf
from datetime import datetime as dt
def remove_walls_c(W, sets):
    numSets= dsf.num_of_sets(sets)
    start = dt.now()
    while  numSets > 1 and W is not None:
            d = random.randint(0,len(walls)-1)
            #print(numSets)
            if (dsf.in_same_set(sets,walls[d][0],walls[d][1])) == False:
                
                dsf.union_c(sets,walls[d][0],walls[d][1])
                numSets -= 1
                walls.pop(d)
    stop = dt.now() -start
    #draw_maze(walls,maze_rows,maze_cols) 
    print('With compression, wall removal took ', stop,' to complete.')
    
    
def remove_walls(W, sets):
    numSets= dsf.num_of_sets(sets)
    start = dt.now()
    while  numSets > 1 and W is not None:
            d = random.randint(0,len(walls)-1)
            #print(numSets)
            if (dsf.in_same_set(sets,walls[d][0],walls[d][1])) == False:
                dsf.union(sets,walls[d][0],walls[d][1])
                numSets -= 1
                walls.pop(d)
    stop = dt.now() -start
    #draw_maze(walls,maze_rows,maze_cols) 
    print('Without compression, wall removal took ', stop,' to complete.')
    
            
def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

plt.close("all") 
maze_rows = 250
maze_cols = 250

walls = wall_list(maze_rows,maze_cols)
sets = dsf.DisjointSetForest(maze_rows*maze_cols)
#draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
try:
    choice = int(input("Enter (1)for union without compression or (2) for union with compression."))
    if choice ==1:
        remove_walls(walls,sets)
    elif choice == 2:
        remove_walls_c(walls,sets)
    else:
        print('invalid input')
except ValueError:
    print("exception reached")
    print()
print("Maze size: " , maze_rows, "X", maze_cols)




    
    


