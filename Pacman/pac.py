import os
import pygame
import time
from random import randint
import math

map = 1
fps=60
showDistGrid = 0
Ghost1 = 1
Ghost2 = 0
blocker = 0
showPath =0
moved=0
total=999
follow = 1
global caught
caught=[0,0]
time_clk=0
if map!=0:
    xGrid =19
    yGrid = 25
else:
    xGrid = 39  # 19
    yGrid = 25  # 25
height = yGrid * 40
width = xGrid * 40
valPlayer = 9000
pygame.init()
widthBlock = width // xGrid
Grid = [[9999 for i in range(xGrid)] for j in range(yGrid)]
pGrid = [[0 for i in range(xGrid)] for j in range(yGrid)]

def InitMap():
    global Grid,map
    map=randint(0,5)+1
    if map == 1:
        print("in 1")
        Grid = [[-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2], 
    [-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2], 
    [-2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2],
    [-2, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, -2],
    [-2, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, -2, -2], 
    [-2, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, -2],
    [-2, 9999, -2, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, -2, 9999, -2], 
    [-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2], 
    [-2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2], 
    [9998, 9998, 9998, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2, 9998, 9998, 9998], 
    [-2, -2, -2, -2, 9999, -2, 9999, -2, -2, 9998, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2], 
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9998, 9998, 9998, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999], 
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9998, 0, 9998, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999], 
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9998, 9998, 9998, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999], 
    [-2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2], 
    [9998, 9998, 9998, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2, 9998, 9998, 9998], 
    [-2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2], 
    [-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2],
    [-2, 9999, -2, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, -2, 9999, -2],
    [-2, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, -2],
    [-2, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, -2, -2],
    [-2, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, -2], 
    [-2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, -2, 9999, -2], 
    [-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2],
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]]
    elif map == 2:
        print("in 2")
        Grid = [[-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2], [-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2], [-2, 9999, 9999, -2, 9999, 9999, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, 9999, 9999, 9999, -2], [-2, 9999, -2, -2, -2, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, -2, 9999, 9999, -2], [9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999], [9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999], [-2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, -2], [-2, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2, 9999, -2, -2], [9999, 9999, 9999, -2, 9999, -2, -2, -2, 9999, 9999, -2, -2, -2, -2, -2, -2, 9999, 9999, -2], [9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999], [-2, 9999, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2], [-2, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 1, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, -2], [-2, -2, -2, -2, -2, 9999, 9999, 9999, 9999, 0, 9999, 9999, 9999, -2, 9999, -2, -2, 9999, -2], [-2, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 1, 9999, -2, 9999, -2, 9999, -2, 9999, 9999, -2], [-2, 9999, 9999, 9999, -2, 9999, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, 9999, -2, -2], [9999, 9999, -2, -2, -2, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999], [-2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, -2], [-2, 9999, 9999, 9999, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, 9999, 9999, -2, 9999, 9999, -2], [-2, -2, -2, 9999, 9999, -2, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, -2], [9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999], [9999, 9999, 9999, 9999, -2, -2, 9999, -2, -2, 9999, -2, -2, 9999, -2, -2, -2, 9999, 9999, 9999], [-2, 9999, 9999, -2, -2, -2, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, -2, -2, -2], [9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, -2, 9999], [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999], [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]]
    elif map==3:
        print("in 3")
        Grid=[ 
        [ -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
        [ -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, -2],
        [ -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2],
        [ -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2],
        [ -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2],
        [ 9998, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, 9998],
        [ -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2],
        [ 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999],
        [ -2, -2, 9999, -2, -2, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, -2, -2, 9999, -2, -2],
        [ 9998, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9998, -2, 9998],
        [ 9998, -2, 9999, -2, -2, -2, 9999, -2, -2, 9998, -2, -2, 9999, -2, -2, -2, 9999, -2, 9998],
        [ 9998, -2, 9999, -2, 9999, 9999, 9999, -2, 9998, 9998, 9998, -2, 9999, 9999, 9999, -2, 9999, -2, 9998],
        [ 9998, -2, 9999, -2, 9999, -2, 9999, -2, 9998, 0, 9998, -2, 9999, -2, 9999, -2, 9999, -2, 9998],
        [ 9998, -2, 9999, -2, 9999, -2, 9999, -2, 9998, 9998, 9998, -2, 9999, -2, 9999, -2, 9999, -2, 9998],
        [ -2, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, -2, -2],
        [ 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999],
        [ -2, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, -2],
        [ 9998, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9998],
        [ -2, -2, 9999, -2, -2, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, -2, -2, 9999, -2, -2],
        [ -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2],
        [ -2, 9999, -2, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, -2, 9999, -2],
        [ -2, 9999, -2, -2, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, -2, -2, 9999, -2],
        [ -2, 9999, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, 9999, -2],
        [ -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2],
        [ -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]]
    elif map==4:
        Grid=[ [ -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
        [ 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999],
        [ -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2],
        [ -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2],
        [ -2, 9999, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, 9999, -2],
        [ -2, 9999, -2, 9999, 9999, 9999, 9999, -2, 9999, -2, 9999, -2, 9999, 9999, 9999, 9999, -2, 9999, -2],
        [ -2, 9999, -2, 9999, -2, -2, 9999, -2, 9999, 9999, 9999, -2, 9999, -2, -2, 9999, -2, 9999, -2],
        [ -2, 9999, 9999, 9999, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, 9999, 9999, 9999, -2],
        [ -2, -2, -2, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2, -2, -2, -2],
        [ -2, 9999, 9999, 9999, 9999, -2, 9999, -2, -2, 9998, -2, -2, 9999, -2, 9999, 9999, 9999, 9999, -2],
        [ -2, 9999, -2, -2, 9999, -2, 9999, -2, 9998, 9998, 9998, -2, 9999, -2, 9999, -2, -2, 9999, -2],
        [ -2, 9999, 9999, -2, 9999, -2, 9999, -2, 9998, 0, 9998, -2, 9999, -2, 9999, -2, 9999, 9999, -2],
        [ -2, -2, 9999, -2, 9999, 9999, 9999, -2, 9998, 9998, 9998, -2, 9999, 9999, 9999, -2, 9999, -2, -2],
        [ 9998, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, -2, 9998],
        [ 9998, -2, 9999, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2, 9999, -2, 9998],
        [ 9998, -2, 9999, 9999, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, 9999, 9999, -2, 9998],
        [ 9998, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9998],
        [ -2, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, -2],
        [ 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999],
        [ -2, -2, 9999, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2, 9999, -2, -2],
        [ -2, 9999, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, 9999, -2],
        [ -2, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, -2],
        [ -2, 9999, -2, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, -2, 9999, -2],
        [ -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2],
        [ -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]]
    else:
        Grid=[ [ -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
        [ -2, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, -2],
        [ -2, 9999, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, 9999, -2],
        [ -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2],
        [ -2, 9999, -2, 9999, -2, 9999, -2, -2, 9999, -2, 9999, -2, -2, 9999, -2, 9999, -2, 9999, -2],
        [ -2, 9999, 9999, 9999, -2, 9999, -2, -2, 9999, -2, 9999, -2, -2, 9999, -2, 9999, 9999, 9999, -2],
        [ -2, -2, -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2, -2, -2],
        [ 9999, 9999, 9999, 9999, -2, -2, -2, 9999, -2, -2, -2, 9999, -2, -2, -2, 9999, 9999, 9999, 9999],
        [ -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2],
        [ -2, 9999, -2, -2, 9999, -2, 9999, -2, -2, 9998, -2, -2, 9999, -2, 9999, -2, -2, 9999, -2],
        [ -2, 9999, -2, 9999, 9999, -2, 9999, -2, 9998, 9998, 9998, -2, 9999, -2, 9999, 9999, -2, 9999, -2],
        [ -2, 9999, -2, 9999, -2, -2, 9999, -2, 9998, 0, 9998, -2, 9999, -2, -2, 9999, -2, 9999, -2],
        [ -2, 9999, 9999, 9999, 9999, -2, 9999, -2, 9998, 9998, 9998, -2, 9999, -2, 9999, 9999, 9999, 9999, -2],
        [ -2, 9999, -2, 9999, -2, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, -2, 9999, -2, 9999, -2],
        [ -2, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, -2],
        [ -2, 9999, -2, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, -2, 9999, -2],
        [ -2, 9999, 9999, 9999, 9999, -2, -2, 9999, 9999, -2, 9999, 9999, -2, -2, 9999, 9999, 9999, 9999, -2],
        [ -2, -2, 9999, -2, 9999, -2, 9999, 9999, -2, -2, -2, 9999, 9999, -2, 9999, -2, 9999, -2, -2],
        [ -2, 9999, 9999, -2, 9999, -2, 9999, -2, -2, -2, -2, -2, 9999, -2, 9999, -2, 9999, 9999, -2],
        [ -2, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, -2],
        [ -2, 9999, -2, -2, 9999, 9999, -2, -2, 9999, -2, 9999, -2, -2, 9999, 9999, -2, -2, 9999, -2],
        [ -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, -2, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, -2],
        [ -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2, 9999, -2, -2, -2, 9999, -2],
        [ -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, -2, 9999, 9999, 9999, 9999, 9999, -2],
        [ -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]]
InitMap()
def playerInit():
    p=[randint(0,yGrid-1),randint(0,xGrid-1)]    
    if(Grid[p[0]][p[1]]==9999 and (p[0]<9 or p[1]<6 or (p[1]>12)or p[0]>14)):
        Grid[p[0]][p[1]]=valPlayer
    else:
        p=playerInit()
    return(p)
playerInit()
def pointsinit():
    global total,pGrid
    total=0
    for i in range (yGrid):
        for j in range(xGrid):
            pGrid[i][j]=Grid[i][j]
            if(pGrid[i][j]==9999):
                total+=1
pointsinit()
    
    
follow2 = 0
if follow == 0:
    follow2 = 1
print("Test 2")
w = pygame.display.set_mode((width,height))


def main():
    print("Test 3")
    counter = 0
    while counter < (xGrid * yGrid):
        x = counter // xGrid
        y = counter % xGrid
        if Grid[x][y] == valPlayer:
            break
        counter += 1
    yPlayer = x
    xPlayer = y

    counter = 0
    while counter < (xGrid * yGrid):
        y = counter // xGrid
        x = counter % xGrid
        if Grid[y][x] == 0:
            break
        counter += 1
    yGhost = y
    xGhost = x

    run = True

    def grn(dist,yGhost,xGhost,moveGh0st,valGhost):
        global caught
        if caught[valGhost*-1]==-127:
            caught[valGhost*-1]=-127
        elif caught[valGhost*-1]<30 and dist==0:
            caught[valGhost*-1]+=1
        elif dist>0:
            caught[valGhost*-1]=0



        if showDistGrid == 1:
            font = pygame.font.Font(None,20)

        counter = 0

        while counter < (xGrid * yGrid):
            y = counter // xGrid
            x = counter % xGrid
            if Grid[y][x] == valPlayer:
                break
            counter += 1

        while dist > 0:
            if x > 0 and Grid[y][x - 1] == dist:
                x -= 1

            elif x == 0 and Grid[y][xGrid - 1] == dist:
                x = xGrid - 1

            elif y > 0 and Grid[y - 1][x] == dist:
                y -= 1

            elif y == 0 and Grid[yGrid - 1][x] == dist:
                y = yGrid - 1

            elif x < xGrid and Grid[y][(x + 1) % xGrid] == dist:
                x = (x + 1) % xGrid

            elif y < yGrid - 1 and Grid[(y + 1) % yGrid][x] == dist:
                y = (y + 1) % yGrid

            if showPath == 1:
                pygame.draw.rect(w,(70,170-(valGhost*-1*30),60),(x * widthBlock,y * widthBlock,widthBlock,widthBlock))

            if showDistGrid == 1 and showPath == 1:
                text = font.render(str(dist),True,(90,90,170))
                trex = text.get_rect()
                trex.topleft = (x * widthBlock,y * widthBlock)
                w.blit(text,trex)

            if dist == 1 and moveGh0st == 1 and (
                    (abs(yGhost - y) + 1) % xGrid < 3 and (abs(xGhost - x) + 1) % xGrid < 3):
                Grid[yGhost][xGhost] = 9999
                yGhost = y
                xGhost = x
                Grid[yGhost][xGhost] = valGhost

            else:
                Grid[y][x] = 9999

            dist -= 1

    def path(moveGhost):
        run = True
        font = pygame.font.Font(None,20)
        dist = 0
        found = 0

        counter = 0
        while counter < (xGrid * yGrid):
            y = counter // xGrid
            x = counter % xGrid
            if Grid[y][x] == valPlayer:
                break
            counter += 1

        while run and Ghost1 == 1:
            counter = 0

            while counter < (xGrid * yGrid):
                y2 = (counter // xGrid)
                x2 = counter % xGrid
                counter += 1
                if dist > 51:
                    col = 255
                else:
                    col = 5 * dist

                if Grid[y2][x2] == dist:
                    if Grid[y2][x2 - 1] > dist:
                        if Grid[y2][x2 - 1] == valPlayer:
                            run = False
                            found = 1

                        else:
                            Grid[y2][x2 - 1] = dist + 1

                            if showDistGrid == 1:
                                pygame.draw.rect(w,(255 - col,255 - col,col),(
                                    x2 * widthBlock - widthBlock,y2 * widthBlock,widthBlock,widthBlock))
                                text = font.render(str(dist),True,(50,50,50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock - widthBlock,y2 * widthBlock)
                                w.blit(text,trex)

                    if y2 > 0 and Grid[y2 - 1][x2] > dist:
                        if Grid[y2 - 1][x2] == valPlayer:
                            run = False
                            found = 1

                        else:
                            Grid[y2 - 1][x2] = dist + 1

                            if showDistGrid == 1:
                                pygame.draw.rect(w,(255 - col,255 - col,col),(
                                    x2 * widthBlock,y2 * widthBlock - widthBlock,widthBlock,widthBlock))
                                text = font.render(str(dist),True,(50,50,50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock,y2 * widthBlock - widthBlock)
                                w.blit(text,trex)

                    if Grid[y2][(x2 + 1) % xGrid] > dist:
                        if Grid[y2][(x2 + 1) % xGrid] == valPlayer:
                            run = False
                            found = 1

                        else:
                            Grid[y2][(x2 + 1) % xGrid] = dist + 1

                            if showDistGrid == 1:
                                pygame.draw.rect(w,(255 - col,255 - col,col),(
                                    x2 * widthBlock + widthBlock,y2 * widthBlock,widthBlock,widthBlock))
                                text = font.render(str(dist),True,(50,50,50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock + widthBlock,y2 * widthBlock)
                                w.blit(text,trex)

                    if y2 < yGrid - 1 and Grid[y2 + 1][x2] > dist:
                        if Grid[y2 + 1][x2] == valPlayer:
                            run = False
                            found = 1

                        else:
                            Grid[y2 + 1][x2] = dist + 1

                            if showDistGrid == 1:
                                pygame.draw.rect(w,(255 - col,255 - col,col),(
                                    x2 * widthBlock,y2 * widthBlock + widthBlock,widthBlock,widthBlock))
                                text = font.render(str(dist),True,(50,50,50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock,y2 * widthBlock + widthBlock)
                                w.blit(text,trex)

            dist += 1
            if dist > 999:
                break

        if Ghost1 == 1:
            if found == 1:
                grn(dist -1,yGhost,xGhost,moveGhost,0)
            pygame.draw.rect(w,(200,90,50),(xGhost * widthBlock,yGhost * widthBlock,widthBlock,widthBlock))

        if Ghost2 == 1:
            res()
            dist = 0
            run = True
            found = 0
            distMani = 1

            counter = 0
            while counter < (xGrid * yGrid):
                y = counter // xGrid
                x = counter % xGrid
                if Grid[y][x] == -1:
                    break
                counter += 1
            yGhost2 = y
            xGhost2 = x

        while run and Ghost2 == 1:
            counter = 0
            while counter < (xGrid * yGrid):
                y2 = (counter // xGrid)

                x2 = counter % xGrid
                counter += 1
                if dist > 51:
                    col = 255
                else:
                    col = 5 * dist

                if Grid[y2][x2] == dist - distMani:
                    if Grid[y2][x2 - 1] > dist:
                        if Grid[y2][x2 - 1] == valPlayer:
                            run = False
                            found = 1
                        else:
                            Grid[y2][x2 - 1] = dist + 1
                            if showDistGrid == 1:
                                pygame.draw.rect(w,(255 - col,255 - col,col),(
                                    x2 * widthBlock - widthBlock,y2 * widthBlock,widthBlock,widthBlock))

                                text = font.render(str(dist),True,(50,50,50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock - widthBlock,y2 * widthBlock)
                                w.blit(text,trex)
                    if y2 > 0 and Grid[y2 - 1][x2] > dist:
                        if Grid[y2 - 1][x2] == valPlayer:
                            run = False
                            found = 1
                        else:
                            Grid[y2 - 1][x2] = dist + 1
                            if showDistGrid == 1:
                                pygame.draw.rect(w,(255 - col,255 - col,col),(
                                    x2 * widthBlock,y2 * widthBlock - widthBlock,widthBlock,widthBlock))
                                text = font.render(str(dist),True,(50,50,50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock,y2 * widthBlock - widthBlock)
                                w.blit(text,trex)
                    if Grid[y2][(x2 + 1) % xGrid] > dist:
                        if Grid[y2][(x2 + 1) % xGrid] == valPlayer:
                            run = False
                            found = 1
                        else:
                            Grid[y2][(x2 + 1) % xGrid] = dist + 1
                            if showDistGrid == 1:
                                pygame.draw.rect(w,(255 - col,255 - col,col),(
                                    x2 * widthBlock + widthBlock,y2 * widthBlock,widthBlock,widthBlock))
                                text = font.render(str(dist),True,(50,50,50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock + widthBlock,y2 * widthBlock)
                                w.blit(text,trex)
                    if y2 < yGrid - 1 and Grid[y2 + 1][x2] > dist:
                        if Grid[y2 + 1][x2] == valPlayer:
                            run = False
                            found = 1
                        else:
                            Grid[y2 + 1][x2] = dist + 1
                            if showDistGrid == 1:
                                pygame.draw.rect(w,(255 - col,255 - col,col),(
                                    x2 * widthBlock,y2 * widthBlock + widthBlock,widthBlock,widthBlock))
                                text = font.render(str(dist),True,(50,50,50))
                                trex = text.get_rect()
                                trex.topleft = (x2 * widthBlock,y2 * widthBlock + widthBlock)
                                w.blit(text,trex)

            dist += 1
            distMani = 0

            if dist > 999:
                break

        if found == 1 and Ghost2 == 1:
            grn(dist - 1,yGhost2,xGhost2,moveGhost,-1)
        if Ghost2 == 1:
            pygame.draw.rect(w,(200,90,50),(xGhost2 * widthBlock,yGhost2 * widthBlock,widthBlock,widthBlock))
        #pygame.draw.rect(w,(170,60,80),(,,widthBlock,widthBlock))
        global moved
        if(moved%4>1):
            pygame.draw.arc(w, (255, 255, 0), (x * widthBlock, y * widthBlock, widthBlock, widthBlock),0.7853981634, 5.4977871438, 30)
        else:
            pygame.draw.circle(w, (255, 255, 0), (x * widthBlock+widthBlock//2, y * widthBlock+widthBlock//2), widthBlock//2)

    def res():
        counter = 0
        while counter < (xGrid * yGrid):
            y = counter // xGrid
            x = counter % xGrid
            if Grid[y][x] > 0 and Grid[y][x] < valPlayer:
                Grid[y][x] = 9999
            counter += 1
        #print(Grid)

    click = 0
    pr = 0
    ticker = 0
    clock = pygame.time.Clock()
    pv = 1
    movePlayer = 0
    tic = 0

    time_clk=0
    global Ghost2,total,moved
    gh2 = Ghost2
    Ghost2=0

    while run:

        if time_clk<180:
            time_clk += 1
            ticker = (ticker + 1) % 40 * follow + follow2
        elif gh2==1:
            Ghost2=1
        res()

        ticker = (ticker + 1) % 40 * follow + follow2
        clock.tick(fps)
        if tic > 0:
            tic -= 1
        counter = 0
        while counter < (xGrid * yGrid):
            x = counter // xGrid
            y = counter % xGrid
            if Grid[x][y] == 0:
                break
            counter += 1
        yGhost = x
        xGhost = y
        counter = 0
        yy = 0
        Mouse_Loc = pygame.mouse.get_pos()
        if total==0:
            break  
        while counter < (xGrid * yGrid):
            x = counter // xGrid
            y = counter % xGrid
            if Grid[x][y] == -2:
                pygame.draw.rect(w,(20,35,80),(y * widthBlock,x * widthBlock,widthBlock,widthBlock))
            elif (counter % 2 == 0 and yy % 2 == 0) or (counter % 2 != 0 and yy % 2 != 0):
                pygame.draw.rect(w,(12,15,40),(y * widthBlock,x * widthBlock,widthBlock,widthBlock))
            else:
                pygame.draw.rect(w,(5,8,15),(y * widthBlock,x * widthBlock,widthBlock,widthBlock))
            if pGrid[x][y] == 9999:
                pygame.draw.circle(w,(200,35,80),(y * widthBlock +widthBlock//2,x * widthBlock+widthBlock//2),widthBlock//8)
            counter += 1

        keypress = pygame.key.get_pressed()
        if click == 1:
            yy = Mouse_Loc[1] // widthBlock
            counter = Mouse_Loc[0] // widthBlock % xGrid
            if counter >= xGrid or yy >= yGrid:
                pr = 5
            if pr == 0:
                if counter != yGhost or yy != xGhost:
                    Grid[yy][counter] = -2
            elif pr == 1 and Grid[yy][counter] == -2:
                Grid[yy][counter] = 9999
        if pr == 2:
            yy = Mouse_Loc[1] // widthBlock
            counter = Mouse_Loc[0] // widthBlock % xGrid
            if Grid[yy][counter] != -2 and Grid[yy][counter] != 0:
                Grid[yPlayer][xPlayer] = 9999
                yPlayer = yy
                xPlayer = counter
                Grid[yPlayer][xPlayer] = valPlayer
        if pr == 3:
            yy = Mouse_Loc[1] // widthBlock * pv
            counter = Mouse_Loc[0] // widthBlock % xGrid * pv
            if Grid[yy][counter] != -2 and Grid[yy][counter] != valPlayer:
                Grid[yGhost][xGhost] = 9999
                yGhost = yy
                xGhost = counter
                Grid[yGhost][xGhost] = 0
        if ticker == 0:
            mov3Ghost = 1
        else:
            mov3Ghost = 0
        moved=0
        if movePlayer == 1 and tic == 0 and Grid[yPlayer + 1][xPlayer] != -2 and Grid[yPlayer + 1][
            xPlayer] != 0 and Grid[yPlayer + 1][xPlayer] != -1:
            tic = 15
            Grid[yPlayer][xPlayer] = 9999
            yPlayer += 1
            Grid[yPlayer][xPlayer] = valPlayer
            moved=1+moved%4
        elif movePlayer == 2 and tic == 0 and Grid[yPlayer - 1][xPlayer] != -2 and Grid[yPlayer - 1][
            xPlayer] != 0 and Grid[yPlayer - 1][xPlayer] != -1:
            Grid[yPlayer][xPlayer] = 9999
            yPlayer -= 1
            tic = 15
            Grid[yPlayer][xPlayer] = valPlayer
            moved=5+moved%4
        elif movePlayer == 3 and tic == 0 and Grid[yPlayer][(xPlayer + 1) % xGrid] != -2 and\
                Grid[yPlayer][(xPlayer + 1) % xGrid] != 0 and Grid[yPlayer][
            (xPlayer + 1) % xGrid] != -1:
            Grid[yPlayer][xPlayer] = 9999
            xPlayer = (xPlayer + 1) % xGrid
            tic = 15
            Grid[yPlayer][xPlayer % xGrid] = valPlayer
            moved=9+moved%4
        elif movePlayer == 4 and tic == 0 and xPlayer != 0 and Grid[yPlayer][xPlayer - 1] != -2 and\
                Grid[yPlayer][xPlayer - 1] != 0 and Grid[yPlayer][xPlayer - 1] != -1:
            Grid[yPlayer][xPlayer] = 9999
            xPlayer -= 1
            tic = 15
            Grid[yPlayer][xPlayer] = valPlayer
            moved=13+moved%4
        elif movePlayer == 4 and tic == 0 and xPlayer == 0 and Grid[yPlayer][xGrid - 1] != -2 and\
                Grid[yPlayer][xGrid - 1] != 0 and Grid[yPlayer][xGrid - 1] != -1:
            Grid[yPlayer][xPlayer] = 9999
            xPlayer = xGrid - 1
            tic = 15
            Grid[yPlayer][xPlayer] = valPlayer
            moved=13+moved%4
        if(moved>0):
            if pGrid[yPlayer][xPlayer]==9999:
                pGrid[yPlayer][xPlayer]=0
                total-=1
        if caught[0] > 20 or caught[1] > 20:
            run = False

        for event in pygame.event.get():
            if keypress[pygame.K_q]:
                pr = 1
                click = 1

            elif keypress[pygame.K_e]:
                pr = 0
                click = 1

            elif keypress[pygame.K_t]:
                pr = 2
                ticker = 1

            elif keypress[pygame.K_r]:
                pr = 3

            elif keypress[pygame.K_SPACE]:
                mov3Ghost = 1

            else:
                click = 0
                pr = 0
                mov3Ghost = 0

            if keypress[pygame.K_s] and Grid[yPlayer + 1][xPlayer] != -2 and Grid[yPlayer + 1][
                xPlayer] != 0 and Grid[yPlayer + 1][xPlayer] != -1:
                movePlayer = 1
            elif keypress[pygame.K_w] and Grid[yPlayer - 1][xPlayer] != -2 and Grid[yPlayer - 1][
                xPlayer] != 0 and Grid[yPlayer - 1][xPlayer] != -1:
                movePlayer = 2
            elif keypress[pygame.K_d] and Grid[yPlayer][(xPlayer + 1) % xGrid] != -2 and Grid[yPlayer][
                (xPlayer + 1) % xGrid] != 0 and Grid[yPlayer][(xPlayer + 1) % xGrid] != -1:
                movePlayer = 3
            elif keypress[pygame.K_a] and Grid[yPlayer][xPlayer - 1] != -2 and Grid[yPlayer][
                xPlayer - 1] != 0 and Grid[yPlayer][xPlayer - 1] != -1:
                movePlayer = 4
            else:
                movePlayer = 0

            if keypress[pygame.K_ESCAPE] or event.type == pygame.QUIT or caught[0]>29 or caught[1]>29:
                
                run = False

        path(mov3Ghost)
        
        pygame.display.update()
	
print("Test 4")
main()

#print(Grid)
pygame.quit()
