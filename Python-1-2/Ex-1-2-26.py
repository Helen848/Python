import sys
import stdio

#accepting month, day and year 
month = sys.argv[1]
day = int(sys.argv[2])
year = int(sys.argv[3])

if(month == "Jnuary"): month = 1
elif(month == "February"): month = 2
elif(month == "March"): month = 3
elif(month == "April"): month = 4
elif(month == "May"): month = 5
elif(month == "JUne"): month = 6
elif(month == "July"): month = 7
elif(month == "August"): month = 8
elif(month == "September"): month = 9
elif(month == "October"): month = 10
elif(month == "November"): month = 11
elif(month == "December"): month = 12
else:
    stdio.write("Unknown Month")
    
Yo = year - (14 - month)/12
x = int(Yo + Yo/4 - Yo/100 + Yo/400)
Mo = int(month + 12 * ((14 - month)/12) - 2)
Do = (day + x + (31 * Mo)/12) % 7

if(Do == 0): Do = 'Sunday'  
elif(Do == 1): Do = 'Monday' 
elif(Do == 2): Do = 'Tuesday'
elif(Do == 3): Do = 'Wedensday'
elif(Do == 4): Do = 'Thursday'
elif(Do == 5): Do = 'Friday'
elif(Do == 6): Do = 'Saturday'
else:
    stdio.writeln('Unknown Day') 
    
stdio.write('On ')
stdio.write(Do)
stdio.write(" of the week was ")
stdio.write(month)
stdio.write(day)
stdio.writeln(year)
    

