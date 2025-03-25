import numpy as np
import math

GRAVITY = 9.81
NM_TO_KGCM = 10.197162129779

def torque(radius, force, theta):
    torque = radius * force * math.sin(np.deg2rad(theta))
    return torque

def force(mass):
    force = mass * GRAVITY
    return force

def convert_Nm_to_Kgcm(torque_Nm):
    return torque_Nm * NM_TO_KGCM

radius = float(input("Enter radius in meters: "))
mass = float(input("Enter mass in kilograms: "))
theta = float(input("Enter theta in degrees: "))

force = force(mass)
torque = torque(radius, force, theta)
print("Torque:", torque, "Nm")
print("Torque:", convert_Nm_to_Kgcm(torque), "kg cm")
