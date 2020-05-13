# coding=utf-8

"""
The idea comes from "Ninty-Nine Haskell Problems": 

https://wiki.haskell.org/H-99:_Ninety-Nine_Haskell_Problems

So we try to solve the same set of those small problems in Python. Here are
the problems related to List.
"""

from itertools import count, takewhile, dropwhile, chain
from functools import reduce



def head(it):
	"""
	[Iterable] it 
		=> [Object] first element of it, or raise ValueError if it is empty
	"""
	try:
		return next(iter(it))
	except StopIteration:
		raise ValueError



def tail(it):
	"""
	[Iterable] it
		=> [Object] The last element of it, or raise ValueError if it is empty
	"""
	iterator = iter(it)
	try:
		while(True):
			el = next(iterator)
	except StopIteration:
		try:
			return el
		except UnboundLocalError:	# el not assigned, meaning it is empty
			raise ValueError



"""
# This version also works
# 
def tail(it):
	n = 0
	iterator = iter(it)
	try:
		while(True):
			el = next(iterator)
			n = n + 1
	except StopIteration:
		if n > 0:
			return el
		else:
			raise ValueError
"""


"""
# This version doesn't work. It's because when we nest next() and iter() calls, it
# causes an infinite loop.
# 
def tail(it):
	try:
		while(True):
			el = next(iter(it))
	except StopIteration:
		try:
			return el
		except UnboundLocalError:
			raise ValueError
"""



def lastButOne(it):
	"""
	[Iterable] it 
		=> [Object] the next to the last element of it or raise ValueError
			if it has less than 2 elements
	"""
	def pairs(first, it):
		for el in it:
			yield (first, el)
			first = el


	iterator = iter(it)
	return tail(pairs(head(iterator), iterator))[0]



def firstNelements(it, n):
	"""
	[Iterable] it
		=> [Iterable] it, an iterable object on the first N elements of it (if
			it has at least N elements), or all elemtns in it.
	"""
	return map(lambda x: x[1], zip(range(n), it))



def elementAt(it, n):
	"""
	[Iterable] it, [Int] n
		=> [Object] the nth element of it, if it has at least n elements
					or raise a ValueError

			n starting from 1, 1 means the first element

	Take out the first (n-1) elements, then take the head of the remaining
	(potentially infinite) list.
	"""
	return head(dropwhile( lambda t: t[0] < n
					  	 , zip(count(1), it)
					  	 )
			   )[1]



"""
# Similar idea, also works
def elementAt(it, n):
	return head(filter( lambda t: t[0] >= n
					  , zip(count(1), it)
					  )
			   )[1]
"""


"""
# Also works: take the first n elements, take the tail of it
# Note that tail(firstNelements(it, n)) does not work, because firstNelements()
# may not contain N elements.
# 
def elementAt(it, n):
	el = tail(zip(range(1, n+1), it))
	if el[0] == n:
		return el[1]
	else:
		raise ValueError
"""



def reverse(it):
	"""
	[Iterable] it => [Iterable] it

	return the reversed list

	Note that if the input is a string, then we need to return a string rather
	than a map object.
	"""
	def build(acc, el):
		return [el] + acc

	result = reduce(build, it, [])
	return ''.join(result) if isinstance(it, str) else result





"""
	[Iterable] it
		=> [int] number of elements in the iterator, 0 if empty
"""
numElements = lambda it: sum(map(lambda _: 1, it))



"""
# This also works
# 
def numElements(it):

	try:
		return tail(zip(count(1), it))[0]
	except ValueError:	# empty list
		return 0
"""


"""
# Also works
def numElements(it):

	try:
		return tail(enumerate(it))[0] + 1
	except ValueError:	# empty list
		return 0
"""




if __name__ == '__main__':
	print(head(filter(lambda x: x > 5, count())))

