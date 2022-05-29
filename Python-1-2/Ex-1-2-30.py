import sys
import stdio
import math

# accepting the latitude and longtitude in two points of the earth
x1 = int(sys.argv[1])
y1 = int(sys.argv[2])
x2 = int(sys.argv[3])
y2 = int(sys.argv[4])

# calculating the distance
d = 60 * math.arccos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1 - y2)))

stdio.write("The Great Circle Distance: ")
stdio.writeln(d)


