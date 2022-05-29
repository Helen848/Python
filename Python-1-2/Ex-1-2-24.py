import sys
import stdio
import math
import random

#generate random number for u and v
u = random.random()
v = random.random()

#formula to generate guassian random numbers
w = math.sin(2 * math.pi * v) * (-2* math.log(u)) ** 0.5

stdio.writeln("The Guassian Random Number: ")
stdio.writeln(w)
