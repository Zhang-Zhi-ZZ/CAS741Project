#!/usr/bin/python

import unittest
from main import * 
from ODE import *
from input import *
from output import *
from plot import*
from acceleration import *

class TestInput(unittest.TestCase):
	def test_input(self):
		data1 = {"m1":2.0, "m2":2.0, "L1":1.0, "L2":1.0, "theta1":-0.1667, 
		"theta2":0.0,"g":9.8, "t":20.0}
		result1 = input()
		self.assertEqual(data1,result1)

	def test_acceleration(self):
		data2 = [3.768147788796435, -4.0733428589067255]
		result2 = acceleration(-0.5, 0, 0.3, 0,1,1,9.8,2, 2,20)
		self.assertEqual(data2,result2)

	def test_output(self):
		data3 = "expectedoutput.txt"
		result3 = output([1,2,3], [2,3,4],[0.5, 1.0, 1.5])
		self.assertListEqual(list(io,open(data3)),list(io.open(result3)))

if __name__== '__main__':
	unittest.main()
