# Project: Kepler's 2nd Law (Equal Areas)
# Name: Meesam Raza
# Degree: BS Math (Final Year Project MTH600)

import math
import matplotlib.pyplot as plt

# ==========================================
# terminal output details
# ==========================================
print("--------------------------------------------------")
print("Project: Kepler's Laws of Planetary Motion (MTH600)")
print("Author: Meesam Raza")
print("Degree: BS Mathematics")
print("University: Virtual University of Pakistan")
print("--------------------------------------------------")
print("Running Kepler's 2nd Law (Law of Equal Areas)...")
print("Calculating orbital path and areas...")

# step 1: basic settings
G = 6.67430e-11
M_sun = 1.989e30
dt = 86400 * 2         # checking position every 2 days
total_steps = 365      # total steps to complete the oval orbit

# starting position of planet (making it an oval/ellipse shape)
x = 2.0e11             # start far from sun
y = 0.0
vx = 0.0
vy = 15000.0           # slow starting speed

x_path = []
y_path = []

# step 2: calculate orbit path
for i in range(total_steps):
    r = math.sqrt(x**2 + y**2)
    
    # gravity formulas
    ax = -G * M_sun * x / r**3
    ay = -G * M_sun * y / r**3
    
    vx = vx + (ax * dt)
    vy = vy + (ay * dt)
    
    x = x + (vx * dt)
    y = y + (vy * dt)
    
    x_path.append(x)
    y_path.append(y)

# step 3: draw the graph and fill areas
plt.figure(figsize=(8, 8))
plt.plot(x_path, y_path, color='blue', label='Planet Path')
plt.scatter(0, 0, color='orange', s=200, label='Sun')

# fill area 1 (when planet is far and slow) - 30 steps
x_area1 = [0] + x_path[10:40] + [0]
y_area1 = [0] + y_path[10:40] + [0]
plt.fill(x_area1, y_area1, color='green', alpha=0.5, label='Area 1 (Same Time)')

# fill area 2 (when planet is close and fast) - 30 steps
x_area2 = [0] + x_path[180:210] + [0]
y_area2 = [0] + y_path[180:210] + [0]
plt.fill(x_area2, y_area2, color='red', alpha=0.5, label='Area 2 (Same Time)')

# final design
plt.title("Kepler 2nd Law - MTH600 Project\nBy Meesam Raza")
plt.xlabel("x axis (meters)")
plt.ylabel("y axis (meters)")
plt.legend()
plt.grid(True)
plt.axis('equal')

# save picture
plt.savefig(r"C:\Users\meesa\Desktop\python\keplers_2nd_law_plot.png")
print("Done! The graph has been saved as 'keplers_2nd_law_plot.png' on your Desktop folder.")
print("--------------------------------------------------")