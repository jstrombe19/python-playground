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

total_rad = 0.64
total_mass = 6.0
worst_theta = 90

arm1_rad = 0.215
arm2_rad = 0.175
arm3_rad = 0.125
arm4_rad = 0.075
arm5_rad = 0.050

force = force(total_mass)
torque = torque(total_rad, force, worst_theta)
print("Torque:", torque, "Nm")
print("Torque:", convert_Nm_to_Kgcm(torque), "kg cm")



