import sys
import stdio
import random

numOne = random.random()
numTwo = random.random()
numThree = random.random()
numFour = random.random()
numFive = random.random()

#finding the max and min value of the five random numbers
minVal = min(numOne, numTwo, numThree, numFour, numFive)
maxVal = max(numOne, numTwo, numThree, numFour, numFive)
avgVal = float((numOne + numTwo + numThree + numFour + numFive)/5)

stdio.write("The minmum value from random numbers: ")
stdio.writeln(minVal)
stdio.write("The maximum value from random numbers: ")
stdio.writeln(maxVal)
stdio.write("The average value from random numbers: ")
stdio.writeln(avgVal)


