import sys
import stdio

#accepting numbers from the command line to check whether they are in ascending or descending order
numOne = int(sys.argv[1])
numTwo = int(sys.argv[2])
numThree = int(sys.argv[3])

if(numOne < numTwo and numOne < numThree):
    if(numTwo < numThree):
        stdio.write(True)          
elif(numOne > numTwo and numOne > numThree):
    if(numTwo > numThree):
        stdio.write(True)
else:
    stdio.write(False)
            
    
              
          
