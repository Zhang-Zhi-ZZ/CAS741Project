#!/usr/bin/python
from acceleration import *
from input import*
from math import *
def ODE(theta1, theta2, m1, m2, L1,L2,g,t):
 

	global thetaList
 
	# initialize data
 
	theta1List = [theta1]
	theta2List = [theta2]
	theta1dotdotList = []
	theta2dotdotList = []
	
	theta1dot = 0.0
	theta2dot = 0.0
	theta1dotList = [theta1dot]
	theta2dotList = [theta2dot]
	dt = 0.005
	time = 0.0
	timeList =[0.0]
	# solve ODE
	while time<t:
		#rate(100)
		thetadotdot = acceleration(theta1, theta1dot, theta2, theta2dot,m1,m2,g,L1, L2,time)
		theta1dot = theta1dot + thetadotdot[0]*dt
		theta1 = theta1 + theta1dot * dt 
		theta2dot = theta2dot + thetadotdot[1] * dt
		theta2 = theta2 + theta2dot * dt 
		time = time + dt
		timeList.append(time)
		theta1List.append(theta1)
		theta2List.append(theta2)
		theta1dotList.append(theta1dot)
		theta2dotList.append(theta2dot)
		theta1dotdotList.append(thetadotdot[0])
		theta2dotdotList.append(thetadotdot[1])
		#thetaList = [theta1List,theta2List]
	return [theta1List, theta2List,timeList]


