# coding=utf-8
# 

import unittest2
from itertools import takewhile, count
from py_functional_learning.list_problems import head, tail, numElements \
	, firstNelements, elementAt, reverse



class TestList(unittest2.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestList, self).__init__(*args, **kwargs)



	def testHead(self):
		self.assertEqual('a', head(['a']))
		self.assertEqual(1, head(range(1,100)))
		self.assertEqual('a', head(['a', 'b']))
		self.assertEqual(3, head(filter(lambda x: x > 2, range(8))))
		self.assertEqual(0, head(count()))	# infinite list



	def testHeadError(self):
		try:
			head([])
		except ValueError:
			pass	# expected
		else:
			self.fail('something goes wrong')



	def testTail(self):
		self.assertEqual('a', tail(['a']))
		self.assertEqual('b', tail(['a', 'b']))
		self.assertEqual(6, tail(filter(lambda x: x < 7, range(100))))



	def testTailError(self):
		try:
			tail([])
		except ValueError:
			pass	# expected
		else:
			self.fail('something goes wrong')



	def testNumElements(self):
		self.assertEqual(0, numElements([]))
		self.assertEqual(0, numElements(filter(lambda x: x > 5, range(4))))
		self.assertEqual(1, numElements(['a']))
		self.assertEqual(5, numElements('abcde'))



	def testFirstNelements(self):
		self.assertEqual([], list(firstNelements([], 2)))
		self.assertEqual([1], list(firstNelements([1], 2)))
		self.assertEqual([0, 1], list(firstNelements(range(5), 2)))
		self.assertEqual(['a'], list(firstNelements('abc', 1)))
		self.assertEqual([0, 1, 2], list(firstNelements(count(), 3)))



	def testElementAt(self):
		self.assertEqual('a', elementAt('abc', 1))
		self.assertEqual(2, elementAt(range(3), 3))
		self.assertEqual(5, elementAt(count(1), 5))	# infinite list



	def testElementAtError(self):
		try:
			elementAt([], 1)
		except ValueError:
			pass	# expected
		else:
			self.fail('something goes wrong')


		try:
			elementAt([1, 2], 3)
		except ValueError:
			pass	# expected
		else:
			self.fail('something goes wrong')



	def testReverse(self):
		self.assertEqual([], reverse([]))
		self.assertEqual('a', reverse('a'))
		self.assertEqual('ab c', reverse('c ba'))
		self.assertEqual( [3, 2, 1]
						, reverse(takewhile(lambda x: x < 4, count(1))))