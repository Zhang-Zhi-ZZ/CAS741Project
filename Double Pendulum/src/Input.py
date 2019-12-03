#!/usr/bin/python

import yaml

m1=float()
m2=float()
L1=float()
L2=float()
theta1=float()
theta2=float()
g=float()
t=float()

def verify_params():
    if ((m1<=0.0) or (m2<=0.0)):
        raise NEGATIVE_MASS
    if ((L1<=0.0) or (L2<=0.0)):
        raise NEGATIVE_LENGTH
    if (g<=0.0):
        raise NEGATIVE_GARVITY
    if (t<=0.0):
        raise NEGATIVE_TIME

def load_params(s):
    global m1
    global m2
    global L1
    global L2
    global theta1
    global theta2
    global g
    global t
    try:
        input_file = open(s)
        input_data = yaml.load(input_file)
        m1 = float(input_data["m1"])
        m2 = float(input_data["m2"])
        L1 = float(input_data["L1"])
        L2 = float(input_data["L2"])
        theta1 = float(input_data["theta1"])
        theta2 = float(input_data["theta2"])
        g = float(input_data["g"])
        verify_params()
