"""
===============================================================================
Project : Kepler's 2nd Law (Law of Equal Areas)
Author  : Meesam Raza
Degree  : BS Mathematics (Final Year Project MTH600)

Idea    : Kepler's 2nd law says the line from the Sun to the planet sweeps out
          equal areas in equal times. Here the orbit is integrated numerically
          for one full period, and the area swept in two equal time windows
          (one near the far point, one near the close point) is calculated
          and compared.

Method  : Velocity Verlet (a second-order method, time step = 1 hour).
Start   : Planet at its far point (aphelion), moving slowly.
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
window_days = 20          # length of each "equal time" window (days)

x, y = 2.0e11, 0.0        # start far from the Sun (m)
vx, vy = 0.0, 15000.0     # slow starting speed (m/s)

# Orbit period from the starting values (used to simulate exactly one orbit)
energy = 0.5 * (vx**2 + vy**2) - mu / math.hypot(x, y)
a = -mu / (2 * energy)
period = 2 * math.pi * math.sqrt(a**3 / mu)
n_steps = int(round(period / dt))

print("Kepler's 2nd law - equal areas in equal times")
print(f"Orbit period = {period / 86400:.1f} days ({n_steps} steps of 1 hour)")

# =============================================================================
# Step 2: integrate the motion (velocity Verlet)
# =============================================================================
def acceleration(px, py):
    """Gravitational acceleration towards the Sun at the origin."""
    r = math.sqrt(px**2 + py**2)
    return -mu * px / r**3, -mu * py / r**3


x_path = [x]
y_path = [y]
speed = [math.hypot(vx, vy)]
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
    speed.append(math.hypot(vx, vy))

x_path = np.array(x_path)
y_path = np.array(y_path)
speed = np.array(speed)

# =============================================================================
# Step 3: area swept by the Sun-planet line in a time window
# =============================================================================
def swept_area(i_start, i_end):
    """Area of the sector Sun -> path[i_start..i_end] (shoelace formula).
    The Sun is at the origin, so only the path points are needed."""
    xs = x_path[i_start:i_end + 1]
    ys = y_path[i_start:i_end + 1]
    return 0.5 * abs(np.sum(xs[:-1] * ys[1:] - xs[1:] * ys[:-1]))


steps_per_window = int(window_days * 86400 / dt)

# Window 1: starts at the far point (start of the orbit)
start1 = 0
end1 = start1 + steps_per_window

# Window 2: centred on the close point (perihelion, half-way through the orbit)
i_peri = int(np.argmin(np.hypot(x_path, y_path)))
start2 = i_peri - steps_per_window // 2
end2 = start2 + steps_per_window

area1 = swept_area(start1, end1)
area2 = swept_area(start2, end2)

r_far = np.hypot(x_path, y_path).max()
r_close = np.hypot(x_path, y_path).min()

print(f"Window length          : {window_days} days each")
print(f"Area 1 (far, slow)     : {area1:.4e} m^2")
print(f"Area 2 (close, fast)   : {area2:.4e} m^2")
print(f"Difference             : {abs(area1 - area2) / area1 * 100:.3f} %")
print(f"Speed at far point     : {speed.min():.0f} m/s")
print(f"Speed at close point   : {speed.max():.0f} m/s "
      f"({speed.max() / speed.min():.2f} times faster)")
print(f"Distance far / close   : {r_far / r_close:.2f}")

# =============================================================================
# Step 4: draw the graph (distances in million km)
# =============================================================================
scale = 1e9   # 1 million km = 1e9 m

plt.figure(figsize=(8, 7))
plt.plot(x_path / scale, y_path / scale, color='blue', label='Planet path')
plt.scatter(0, 0, color='orange', s=200, label='Sun')

xa = np.concatenate(([0], x_path[start1:end1 + 1], [0])) / scale
ya = np.concatenate(([0], y_path[start1:end1 + 1], [0])) / scale
plt.fill(xa, ya, color='green', alpha=0.5,
         label=f'Area 1: {window_days} days, far and slow')

xb = np.concatenate(([0], x_path[start2:end2 + 1], [0])) / scale
yb = np.concatenate(([0], y_path[start2:end2 + 1], [0])) / scale
plt.fill(xb, yb, color='red', alpha=0.5,
         label=f'Area 2: {window_days} days, close and fast')

plt.title("Kepler's 2nd Law: equal areas in equal times\n"
          f"Area 1 = {area1:.3e} m$^2$, Area 2 = {area2:.3e} m$^2$\n"
          "MTH600 Project - Meesam Raza")
plt.xlabel("x (million km)")
plt.ylabel("y (million km)")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, fontsize=8)
plt.grid(True)
plt.axis('equal')

plt.savefig("keplers_2nd_law_plot.png", dpi=150, bbox_inches='tight')
print("Done! Picture saved as keplers_2nd_law_plot.png")
plt.show()
