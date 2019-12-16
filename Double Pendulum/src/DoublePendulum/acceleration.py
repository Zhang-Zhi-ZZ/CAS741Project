#!/usr/bin/python
from math import *
from input import *
def acceleration(theta1, theta1dot, theta2, theta2dot,m1,m2,g,L1, L2,time):
	global theta1dotdot
	global theta2dotdot
	
	# calculate frequently used stuff	
	cos1 = cos(theta1)
	cos2 = cos(theta2)
	sin1 = sin(theta1)
	sin2 = sin(theta2)
	sin12 = sin(theta1-theta2)
	cos12 = cos(theta1-theta2)
	mtot = m1+m2


	# define the acceleration equation
	'''
	A = -g*(2*m1+m2)*sin1 - m2*g*sin(theta1-2*theta2)
	B = -2*sin12*m2*(theta2dot**2*L2+theta1dot**2*L1*cos12)
	C = L1*(2*m1+m2-m2*cos(2*theta1-2*theta2))
	theta1dotdot = (A+B)/C

	D = 2*sin12*(theta1dot**2*L1*mtot)
	E = g*mtot*cos1+theta2dot**2*L2*m2*cos12
	theta2dotdot = (D+E)/C
	'''

	A = mtot*L1
	B = m2*L2*cos12
	C = -m2*L2*theta2dot**2*sin12-mtot*g*sin1
	D = L1/L2*cos12
	E = (L1*theta1dot**2*sin12-g*sin2)/L2

	theta1dotdot = (C-B*E)/(A-B*D)
	theta2dotdot = E-D*theta1dotdot

	#energy = -m1*g*L1*cos1-m2*g*(L1*cos1+L2*cos2)
	#energy += 0.5*m1*theta1dot**2*L1**2+0.5*m2*(theta1dot**2*L1**2+theta2dot**2*L2**2+2*L1*L2*theta1dot*theta2dot*cos12)
	 
	secondDerivs = [theta1dotdot, theta2dotdot]
	

	#secondDerivs = [theta1dotdot, theta2dotdot, energy]
	return secondDerivs
	