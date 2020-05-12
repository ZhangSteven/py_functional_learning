# coding=utf-8

"""
Calculate PI.

The idea is to generate points on a circle of radius 1, then sum up the distances
among them.

Support we have a circle of radius 1 on the XY plane, then generate N points on it,
we'll have

(x0, y0), (x1, y1), (x2, y2), ... (xN, yN)

Where x0 = 0, x1 = 1/N, x2 = 2/N, ... xN = 1, 

y coordinates are derived by:

y = sqrt(1 - x^2)

The distance between two neighbouring points (x1, y1) and (x2, y2) are:

d = sqrt(2 * (1 - x1*x2 - sqrt((1-x1^2)*(1-x2^2))))

Then there will be N distances for those points. The sum of those distances will
be approximately equal to a quarter of the perimeter of the circle of radius 1, 
which is PI/2.
"""

from itertools import islice, count
from math import sqrt


"""
	returns a sequence of (k, k+1), k = 0, 1, 2, ... n-1

	returns: (0, 1), (1, 2), (2, 3), ... (n-1, n)
"""
pairs = lambda n: zip(count(), range(1, n+1))


"""
# Also works

pairs = lambda n: enumerate(range(1, n+1))
"""


"""
# Also works, but a more general approach:

# 1) Generate the pairs according to the pattern (k, k+1)
# 2) Take the first n elements

def pairs(n):
	
	def unlimitedPairs():	# an infinite generator
		current = 0
		while(True):
			yield (current, current+1)
			current = current + 1


	return islice(unlimitedPairs(), n)
"""



distance = lambda t: \
	sqrt(2*(1 - t[0]*t[1] - sqrt((1-t[0]*t[0])*(1-t[1]*t[1]))))



distanceN = lambda N: \
	map( distance
	   , map(lambda t: (t[0]/N, t[1]/N), pairs(N)))



distance16 = lambda t: \
	sqrt(2*(256 - t[0]*t[1] - sqrt((256-t[0]*t[0])*(256-t[1]*t[1]))))



distanceN16 = lambda N: \
	map( distance16
	   , map(lambda t: (16*t[0]/N, 16*t[1]/N), pairs(N)))




if __name__ == '__main__':

	"""
		When N = 16, the precision of calcualted PI seems to reaches the hightest.
		Further increasing N lowers the precision.

		N 		Calculated PI
		16		3.1415926358798396
		17		3.1415926459452117
		18		3.1415926473385323
		19		3.1415926156872938
		20		3.1415924847027172

		Is it because when N > 16, the output of the distance() function becomes
		too small to be precisely represented in Python, therefore lowers the
		precision?

		But when we switch to use distance16(), which calculates the distance between
		two points on a circle of radius 16, but it yields exactly the same results
		as when we use distance().

		Is it because of the internal representation of a float number in Python,
		the precision is limited.

		Maybe we should switch to some high precision module to do the calculation. 
	"""
	N = 16
	print(sum(distanceN(2**N))*2)


	# Also works, with exactly the same results
	# print(sum(distanceN16(2**N))/8)

	
