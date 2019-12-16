#!/usr/bin/python
from ODE import *

def output(theta1List, theta2List,time): 
	filepath = "output.txt"
	f = open("output.txt", "w")
	i = 0
	result = [time,theta1List,theta2List]
	display = []
	while i < len(result[0]):
		display.append([result[0][i],result[1][i],result[2][i]])
		i = i+1

	f.write("%s \n" % "[t,theta1(t),theta2(t)]")

	for item in display: 
		f.write("%s \n" % item)
	f.write('\n')

	f.close()
