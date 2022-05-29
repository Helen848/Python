import sys
import stdio

# accepting the color in rgb format to convert to CMYK
r = int(sys.argv[1])
g = int(sys.argv[1])
b = int(sys.argv[1])

if(r == 0 and g == 0):
    if(b == 0):  
        c = 0
        m = 0
        y = 0
        k = 1        
else:
    w = max(r/255, g/255, b/255)
    c = (w - (r/255)) / w
    m = (w - (g/255)) / w
    y = (w - (b/255)) / w
    k = 1 - w
    
stdio.write("The covnersion color of r g b: ")
stdio.write(c)
stdio.write(" ")
stdio.write(m)
stdio.write(" ")
stdio.write(y)
stdio.write(" ")
stdio.write(k)
            

