#!/usr/bin/python
import os

global m1
global m2
global L1
global L2
global theta1
global theta2
global g
global t
def input():
    
    filepath = "input.txt"
    if os.path.exists(filepath):
        f = open(filepath,"r")
        line = f.readline()
        inputData = {}
        while line:
            inputs = line.split(",")
            inputData[inputs[0]]=float(inputs[1])
            line = f.readline()
        f.close()

        m1 = float(inputData.get('m1'))
        if (m1<=0.0):
            raise ValueError('Mass should not be negative')  
            print("Mass1 should not be negative")

        m2 = float(inputData.get('m2'))
        if (m2<=0.0):
            raise ValueError('Mass should not be negative') 
            print("Mass2 should not be negative")

        L1 = float(inputData.get('L1'))
        if (L1<=0.0):
            raise ValueError('Length should not be negative') 
            print("Length1 should not be negative")
        

        L2 = float(inputData.get('L2'))
        if (L1<=0.0):
            raise ValueError('Length should not be negative') 
            print("Length2 should not be negative")
        
        theta1 = float(inputData.get('theta1'))
        theta2 = float(inputData.get('theta2'))
        if (theta1==0.0) and (theta2==0):
            raise ValueError('Starting angles cannot both be zero.') 
            print("Starting angles cannot both be zero.")
        
        g = float(inputData.get('g'))
        if (g<=0.0):
            raise ValueError('Gravity should not be negative') 
            print("Gravity should not be negative")
        
        t = float(inputData.get('t'))
        if (t<=0.0):
            raise ValueError('Time should not be negative') 
            print("Time should not be negative")
        return inputData 
    else:
        print("Input file not found.")
 
input()
 
