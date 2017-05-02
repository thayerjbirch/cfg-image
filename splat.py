import numpy as np
import scipy.misc as smp
import sys
from random import randint
from random import shuffle

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

def adjacent(x, y):
    a = [(x-1,y-1), (x-1, y), (x-1, y+1), (x,y-1), (x,y + 1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    shuffle(a)
    return a

sys.setrecursionlimit(100000)

stack = [((0,50,50), randint(0,MAX_X-1), randint(0,MAX_Y-1))]

while stack:
    p,x,y = stack.pop()
    if validate(x,y) and randint(0,10) < 8:
        p = maybe_mutate(p)
        data[x,y] = list(p)
        for t in adjacent(x,y):
            stack.append((p, t[0], t[1]))

img = smp.toimage(data)
img.save('out.bmp')
img.show()
