#!/usr/bin/python
import math
import os
import matplotlib.pyplot as plt 
from ODE import *
from input import *
from output import *
from plot import*
from acceleration import *
  
def main_functions():
	inputData = input()
	m1 = inputData.get('m1')
	m2 = inputData.get('m2')
	L1 = inputData.get('L1')
	L2 = inputData.get('L2')
	theta1 = inputData.get('theta1')
	theta2 = inputData.get('theta2')
	g = inputData.get('g')
	t = inputData.get('t')
	temp = ODE(theta1, theta2, m1, m2, L1,L2,g,t)
	output(temp[0], temp[1],temp[2])
	plot(temp[0],temp[1],temp[2]) 
 
        

main_functions()


