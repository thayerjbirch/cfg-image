import numpy as np
import scipy.misc as smp
import sys
from random import randint

MAX_X = 1024
MAX_Y = 1024
data = np.zeros((MAX_X,MAX_Y,3))

def mutate(x):
    return x + randint(-25,25)

def maybe_mutate(p):
    if randint(0,10) == 1:
        new_p = (min(mutate(p[0]), 255),min(mutate(p[1]), 255),min(mutate(p[2]), 255))
        return new_p
    else:
        return p

def top_left(p, x, y):
    p = maybe_mutate(p)
    if x in range(0, MAX_X) and y in range(0, MAX_Y):
        data[x,y] = list(p)
        left(p, x - 1, y)
        top(p, x, y - 1)
        top_left(p, x - 1, y - 1)
    

def left(p, x, y):
    p = maybe_mutate(p)
    if x in range(0, MAX_X) and y in range(0, MAX_Y):
        data[x,y] = list(p)
        left(p, x - 1, y)

def bot_left(p, x, y):
    p = maybe_mutate(p)
    if x in range(0, MAX_X) and y in range(0, MAX_Y):
        data[x,y] = list(p)
        left(p, x - 1, y)
        bot(p, x, y + 1)
        bot_left(p, x - 1, y + 1)

def bot(p, x, y):
    p = maybe_mutate(p)
    if x in range(0, MAX_X) and y in range(0, MAX_Y):
        data[x,y] = list(p)
        bot(p, x, y + 1)

def bot_right(p, x, y):
    p = maybe_mutate(p)
    if x in range(0, MAX_X) and y in range(0, MAX_Y):
        data[x,y] = list(p)
        bot(p, x, y + 1)
        right(p, x + 1, y)
        bot_right(p, x + 1, y + 1)

def right(p, x, y):
    p = maybe_mutate(p)
    if x in range(0, MAX_X) and y in range(0, MAX_Y):
        data[x,y] = list(p)
        right(p, x + 1, y)

def top_right(p, x, y):
    p = maybe_mutate(p)
    if x in range(0, MAX_X) and y in range(0, MAX_Y):
        data[x,y] = list(p)
        top(p, x, y - 1)
        right(p, x + 1, y)
        top_right(p, x + 1, y - 1)

def top(p, x, y):
    p = maybe_mutate(p)
    if x in range(0, MAX_X) and y in range(0, MAX_Y):
        data[x,y] = list(p)
        top(p, x, y - 1)

def center(p, x, y):
    p = maybe_mutate(p)
    data[x,y] = list(p)
    top(p, x, y - 1)
    top_right(p, x + 1, y - 1)
    right(p, x + 1, y)
    bot_right(p, x + 1, y + 1)
    bot(p, x, y + 1)
    bot_left(p, x - 1, y + 1)
    left(p, x - 1, y)
    top_left(p, x - 1, y - 1)

sys.setrecursionlimit(100000)
center((0,0,0), int(MAX_X / 2), int(MAX_Y / 2))
img = smp.toimage(data)
img.save('out.bmp')
img.show()
