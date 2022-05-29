import sys
import stdio
import math

temp = float(sys.argv[1])
speed = float(sys.argv[2])

stdio.write("The given Temperature in Fahrenheit: ")
stdio.writeln(temp)

stdio.write("The given Wind Speed in miles per hour: ")
stdio.writeln(speed)

if(abs(temp) > 50):
    stdio.writeln('Temperatue should be less than 50')
elif(speed < 3 or speed > 120):
    stdio.write('The Speed should be between 3 and 120')
else:
      wind = 35.74 + (0.6215*temp) + (0.4275 - 35.75) * (speed ** 0.16)
      stdio.write("The Wind Chill: ")
      stdio.write(wind)            
            
    
