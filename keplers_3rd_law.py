# Project: Kepler's 3rd Law (Law of Harmonies)
# Name: Meesam Raza
# Degree: BS Math (Final Year Project MTH600)

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
print("Running Kepler's 3rd Law (Law of Harmonies)...")
print("Calculating T^2 vs R^3 for planets...")

# Data for 4 inner planets
# R = Distance from sun in AU (Astronomical Units)
# T = Orbital period in Earth years
planets = ['Mercury', 'Venus', 'Earth', 'Mars']
R = [0.387, 0.723, 1.000, 1.524]
T = [0.241, 0.615, 1.000, 1.881]

# Calculate R^3 and T^2
R_cubed = [r**3 for r in R]
T_squared = [t**2 for t in T]

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.plot(R_cubed, T_squared, marker='o', color='purple', linestyle='-', linewidth=2, markersize=8)

# Labeling each planet on the graph
for i, planet in enumerate(planets):
    plt.annotate(planet, (R_cubed[i], T_squared[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Final formatting of the graph
plt.title("Kepler 3rd Law - MTH600 Project\nBy Meesam Raza\n(T² is proportional to R³)")
plt.xlabel("Distance Cubed (R³) in AU³")
plt.ylabel("Time Squared (T²) in Years²")
plt.grid(True)

# save picture
plt.savefig(r"C:\Users\meesa\Desktop\python\keplers_3rd_law_plot.png")
print("Done! The graph has been saved as 'keplers_3rd_law_plot.png' on your Desktop folder.")
print("--------------------------------------------------")