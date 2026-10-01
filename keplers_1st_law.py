# Project: Kepler's 1st Law
# Name: Meesam Raza
# Degree: BS Math (Final Year Project MTH600)

import numpy as np
import matplotlib.pyplot as plt
import math

# step 1: set basic values for sun and planet
G = 6.67430e-11        # gravity constant
M_sun = 1.989e30       # mass of sun
dt = 86400             # time in one day (seconds)
days = 365             # total days for one year

# starting position of planet (like earth)
x = 1.496e11           # distance from sun
y = 0.0
vx = 0.0               # starting speed x
vy = 29780.0           # starting speed y

# empty lists to save path
x_path = []
y_path = []

print("running 1st law code...")

# step 2: use loop to calculate path day by day
for i in range(days):
    # find distance between planet and sun
    r = math.sqrt(x**2 + y**2)
    
    # calculate gravity pull
    ax = -G * M_sun * x / r**3
    ay = -G * M_sun * y / r**3
    
    # update speed
    vx = vx + (ax * dt)
    vy = vy + (ay * dt)
    
    # update position
    x = x + (vx * dt)
    y = y + (vy * dt)
    
    # save the points
    x_path.append(x)
    y_path.append(y)

# step 3: draw the graph
plt.figure(figsize=(8, 8))
plt.plot(x_path, y_path, label='Planet Path', color='blue')
plt.scatter(0, 0, color='orange', s=200, label='Sun')

plt.title("Kepler 1st Law - MTH600 Project\nBy Meesam Raza")
plt.xlabel("x axis (meters)")
plt.ylabel("y axis (meters)")
plt.legend()
plt.grid(True)
plt.axis('equal')

# save picture to desktop folder
plt.savefig(r"C:\Users\meesa\Desktop\python\keplers_1st_law_plot.png")
print("done! picture is saved.")