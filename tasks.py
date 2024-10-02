# Problem : 1
# Calculate Distance Using Speed and Time
Speed = 13
Time = 10

Distance = Speed * Time
print(str(Distance) + " metres")

# Problem:2
# Calculate Force Using Newton’s Second Law

Mass = 13
Acceleration = 4

Force = Mass * Acceleration
print(str(Force) + " N")

# Problem:3
# Calculate the gravitational potential energy

m = 5      
g = 9.8    
h = 7

Gravitational_PE = m * g * h
print(str(Gravitational_PE) + " joules")

# Problem:4
# Calculate the kinetic energy of an object in motion.

Mass = float(input("Write mass in Kg "))
Velocity = float(input("Write Velocity in metre/sec "))

Kinetic_Energy = 1/2 * (Mass * Velocity**2)
print(str(Kinetic_Energy) + " joules")

# Problem:5
# Calculates the voltage across a resistor given current and resistance using Ohm’s Law

Current = int(input("Write current in ampers: "))
Resistance = int(input("Write Resistance in ohms: "))

Voltage = Current * Resistance
print(str(Voltage) + " volts")

# Problem:6
# calculate the maximum height reached by a projectile, given its initial velocity and launch angle

import numpy as np
Velocity = 20 
Angle = 45
Gravity = 9.8
Angle_rad = np.radians(Angle)
h_max = (Velocity**2 * (np.sin(Angle_rad)**2)) / (2*Gravity)
print(str(h_max) + " meters")

# Problem:7
# calculate the period of a spring-mass system

Mass = 1
Spring_constant = 50
Time_period = (2*np.pi)*np.sqrt(Mass / Spring_constant)
print(str(Time_period) + " sec")

# Problem:8
# calculate the time it takes for an object to hit the ground when dropped from a certain height

Height = 20
Gravity = 9.8 
Time = np.sqrt(2*Height / Gravity)
print(str(Time) + " sec")

# Problem:9
# calculate the work done by a constant force acting on an object.

Force = 100
Displacement = 10
Angle = 30
angle = np.radians(Angle)
Work_done = Force * Displacement * np.cos(angle)
print(str(Work_done) + " joules")

# Problem:10
# calculate the power consumed by an electrical device.

Work = 500
Time = 50

Power = Work / Time
print(str(Power) + " W")