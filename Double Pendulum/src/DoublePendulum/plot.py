#!/usr/bin/python

# importing the required module 
import matplotlib.pyplot as plt 
from ODE import *
import numpy as np
from scipy.interpolate import UnivariateSpline
# line 1 points  

def plot(theta1List, theta2List,t):

    plt.plot(t, theta1List, label="theta1")

    # line 2 points

    # plotting the line 2 points
    plt.plot(t, theta2List, label="theta2")

    # naming the x axis
    plt.xlabel('time(second)')
    # naming the y axis
    plt.ylabel('angle(degree)')
    # giving a title to my graph
    plt.title('Output Graph')

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()
