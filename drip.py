import numpy as np
import scipy.misc as smp
import sys
from random import randint

MAX_X = 1024
MAX_Y = 1920
data = np.zeros((MAX_X,MAX_Y,3))
seen = set()

def mutate(x):
    return x + randint(-25,25)

def maybe_mutate(p):
    if randint(0,10) == 1:
        new_p = (min(mutate(p[0]), 255),min(mutate(p[1]), 255),min(mutate(p[2]), 255))
        return new_p
    else:
        return p

def validate(x, y):
    flatten = (y * MAX_X + x)
    if x in range(0, MAX_X) and y in range(0, MAX_Y) and flatten not in seen:
        seen.add(flatten)
        return True
    else:
        return False
        
def spread_right(p, x, y):
    if validate(x,y):
        p = maybe_mutate(p)
        data[x,y] = list(p)
        spread_right(p, x, y+1)
        maybe_down(p, x + 1, y)

def maybe_down(p, x, y):
    if validate(x,y) and randint(0, 1024) < 1023:
        p = maybe_mutate(p)
        data[x,y] = list(p)
        maybe_down(p, x + 1, y)

sys.setrecursionlimit(100000)
spread_right((0,50,50), 0, 0)
img = smp.toimage(data)
img.save('out.bmp')
img.show()
