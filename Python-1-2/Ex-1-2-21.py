from asyncio import constants
from cmath import e
import sys
import stdio
import math


stdio.write("The number of Years: " )
t = int(sys.argv[1])
stdio.writeln(t)

#t = 2
stdio.write("The Principal: ")
P = float(sys.argv[2])
stdio.writeln(P)

#P = 2.5
stdio.write("The annual interest rate: ")
r = float(sys.argv[3])
stdio.writeln(r)

#r = 3.1

cmpInterest = P*math.e ** r*t
stdio.write("The compound Interest Rate: ")
stdio.write(cmpInterest)

