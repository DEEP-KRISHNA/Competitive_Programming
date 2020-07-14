# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

import math

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	d1 = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
	d2 = math.sqrt(math.pow(x2 - x3, 2) + math.pow(y2 - y3, 2))
	d3 = math.sqrt(math.pow(x3 - x1, 2) + math.pow(y3 - y1, 2))
	her = ((d1 + d2 + d3) / 2)
	return math.sqrt(her*(her-d1)*(her-d2)*(her-d3))
	# pass
