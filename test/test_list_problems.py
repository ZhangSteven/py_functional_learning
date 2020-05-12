# coding=utf-8
# 

import unittest2
from py_functional_learning.list_problems import head, tail, numElements



class TestList(unittest2.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestList, self).__init__(*args, **kwargs)



	def testHead(self):
		self.assertEqual('a', head(['a']))
		self.assertEqual(1, head(range(1,100)))
		self.assertEqual('a', head(['a', 'b']))
		self.assertEqual(3, head(filter(lambda x: x > 2, range(8))))



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