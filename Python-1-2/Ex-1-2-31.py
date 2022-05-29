import sys
import stdio
import math

# accepting three integers to order in ascending order
numOne = int(sys.argv[1])
numTwo = int(sys.argv[2])
numThree =  int(sys.argv[3])

maxVal = max(numOne, numTwo, numThree)
minVal= min(numOne, numTwo, numThree)

if(numOne > minVal and numOne < maxVal):
    midVal = numOne
elif(numTwo > minVal and numTwo < maxVal):
    midVal = numTwo
else:
    midVal = numThree
    
stdio.write("In Ascending order: ")
stdio.write(minVal)
stdio.write(" ")
stdio.write(midVal)
stdio.write(" ")
stdio.write(maxVal)            


