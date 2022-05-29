import sys
import stdio
import math

#accepting center of the map, latitude, and longtitude points 
center = float(sys.argv[1])
lat = float(sys.argv[2])
longt = float(sys.argv[3])

#projection formula
x = longt - center
y = 1/2 * math.log((1 + math.sin(lat)))

stdio.writeln("The Mercator Projection: in the x y coordinate: ")
stdio.write(x)
stdio.write(" and ")
stdio.write(y)

