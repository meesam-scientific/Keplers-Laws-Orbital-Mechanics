"""
===============================================================================
Project : Kepler's 1st Law (Law of Ellipses)
Author  : Meesam Raza
Degree  : BS Mathematics (Final Year Project MTH600)

Idea    : Kepler's 1st law says a planet moves on an ellipse with the Sun at
          one focus. Here Newton's law of gravity is integrated numerically
          for one full orbit of Mercury, and the result is checked against
          the exact ellipse r(theta) = p / (1 + e*cos(theta)).

Method  : Velocity Verlet (a second-order method, time step = 1 hour).
Start   : Mercury at perihelion, moving perpendicular to the Sun-planet line.
===============================================================================
"""

import math

import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# Step 1: constants and starting values (SI units)
# =============================================================================
G = 6.67430e-11           # gravitational constant (m^3 kg^-1 s^-2)
M_sun = 1.989e30          # mass of the Sun (kg)
mu = G * M_sun

dt = 3600.0               # time step: 1 hour (seconds)

# Mercury at perihelion
x, y = 4.6001e10, 0.0     # distance from the Sun (m)
vx, vy = 0.0, 58980.0     # perihelion speed (m/s), perpendicular to the radius

# =============================================================================
# Step 2: orbit shape that follows from the starting values (exact theory)
# =============================================================================
r_start = math.hypot(x, y)
h = x * vy - y * vx                    # angular momentum per unit mass
p = h**2 / mu                          # semi-latus rectum
e = p / r_start - 1                    # eccentricity (perihelion start)
a = p / (1 - e**2)                     # semi-major axis
period = 2 * math.pi * math.sqrt(a**3 / mu)
n_steps = int(round(period / dt))      # simulate exactly one orbit

print("Kepler's 1st law - Mercury, one orbit")
print(f"Theory : a = {a:.4e} m, e = {e:.4f}, period = {period / 86400:.2f} days")

# =============================================================================
# Step 3: integrate the motion (velocity Verlet)
# =============================================================================
def acceleration(px, py):
    """Gravitational acceleration towards the Sun at the origin."""
    r = math.sqrt(px**2 + py**2)
    return -mu * px / r**3, -mu * py / r**3


x_path = [x]
y_path = [y]
ax, ay = acceleration(x, y)

for i in range(n_steps):
    x = x + vx * dt + 0.5 * ax * dt**2
    y = y + vy * dt + 0.5 * ay * dt**2
    ax_new, ay_new = acceleration(x, y)
    vx = vx + 0.5 * (ax + ax_new) * dt
    vy = vy + 0.5 * (ay + ay_new) * dt
    ax, ay = ax_new, ay_new
    x_path.append(x)
    y_path.append(y)

x_path = np.array(x_path)
y_path = np.array(y_path)

# =============================================================================
# Step 4: compare the simulated path with the exact ellipse
# =============================================================================
r_sim = np.hypot(x_path, y_path)
theta_sim = np.arctan2(y_path, x_path)
r_exact = p / (1 + e * np.cos(theta_sim))
max_deviation = np.max(np.abs(r_sim - r_exact) / r_exact)

r_min, r_max = r_sim.min(), r_sim.max()
print(f"Simulation : r_min = {r_min:.4e} m, r_max = {r_max:.4e} m")
print(f"             e (from r_min, r_max) = {(r_max - r_min) / (r_max + r_min):.4f}")
print(f"Maximum difference between simulated path and exact ellipse: "
      f"{max_deviation * 100:.4f} %")

# =============================================================================
# Step 5: draw the graph (distances in million km)
# =============================================================================
scale = 1e9   # 1 million km = 1e9 m

theta = np.linspace(0, 2 * np.pi, 400)
r_theory = p / (1 + e * np.cos(theta))

plt.figure(figsize=(8, 7))
plt.plot(x_path / scale, y_path / scale, color='blue', linewidth=2,
         label='Simulated path')
plt.plot(r_theory * np.cos(theta) / scale, r_theory * np.sin(theta) / scale,
         color='red', linestyle='--', linewidth=1, label='Exact ellipse')
plt.scatter(0, 0, color='orange', s=200, label='Sun (focus 1)')
plt.scatter(-2 * a * e / scale, 0, color='black', marker='x', s=60,
            label='Empty focus (focus 2)')
plt.scatter([r_min / scale], [0], color='green', s=40, zorder=5,
            label='Perihelion')
plt.scatter([-r_max / scale], [0], color='purple', s=40, zorder=5,
            label='Aphelion')
plt.title("Kepler's 1st Law: Mercury's orbit is an ellipse\n"
          "MTH600 Project - Meesam Raza")
plt.xlabel("x (million km)")
plt.ylabel("y (million km)")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, fontsize=8)
plt.grid(True)
plt.axis('equal')

plt.savefig("keplers_1st_law_plot.png", dpi=150, bbox_inches='tight')
print("Done! Picture saved as keplers_1st_law_plot.png")
plt.show()
