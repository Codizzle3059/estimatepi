from random import uniform

#Square has xrange [-1,1] and yrange [-1,1].
#Circle's center point is at [0,0].
#Area of square is 4, area of circle is pi.
#Generate random floating point numbers between -1 and 1, figure out whether
#they are in the circle and the square, or just the square, then add them
#to the respective tallies. Finally, since pi/4 = num_in_circle/num_outside_circle,
#so simply divide them and multiply by 4 to estimate pi

NUM_OF_DARTS = 10000

num_in_circle = 0

def incircle(x, y):
    global num_in_circle
	rad = x*x + y*y
	if rad <= 1:
		num_in_circle += 1

def generatepoints():
	x = uniform(-1, 1)
	y = uniform(-1, 1)
	return x, y

def estimatepi():
	global NUM_OF_DARTS
	global num_in_circle
	for x in xrange(NUM_OF_DARTS):
		x, y = generatepoints()
		incircle(x, y)
	return (float(num_in_circle)/NUM_OF_DARTS) * 4

print estimatepi()
