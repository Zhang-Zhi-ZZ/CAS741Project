#!/usr/bin/python

import unittest
from main import * 
from ODE import *
from input import *
from output import *
from plot import*
from acceleration import *

class TestInput(unittest.TestCase)
	def test_input(self):
		data = {"m1":"2", "m2":"2", "L1":"1", "L2":"1", "theta1":"-0.1667", 
		"theta2":"0.0","g":"9.8", "t":"20"}
		result = input()
		self.assertEqual(data,result)


if __name__== '__main__':
	unittest.main()