"""
===============================================================================
Project : Kepler's 3rd Law (Law of Harmonies)
Author  : Meesam Raza
Degree  : BS Mathematics (Final Year Project MTH600)

Idea    : Kepler's 3rd law says T^2 is proportional to R^3. With R in
          astronomical units (AU) and T in years, the constant is 1.
          This script tests the law with orbital data of four planets:
            1. the ratio T^2 / R^3 for every planet,
            2. a straight-line fit of T^2 against R^3 (slope and R^2),
            3. a log-log fit, where T ~ R^p should give p = 1.5.
===============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# Step 1: orbital data of the four inner planets
# =============================================================================
# R = mean distance from the Sun in AU, T = orbital period in Earth years
planets = ['Mercury', 'Venus', 'Earth', 'Mars']
R = np.array([0.387, 0.723, 1.000, 1.524])
T = np.array([0.241, 0.615, 1.000, 1.881])

R_cubed = R**3
T_squared = T**2

print("Kepler's 3rd law - T^2 / R^3 for each planet")
for name, r3, t2 in zip(planets, R_cubed, T_squared):
    print(f"  {name:8s} R^3 = {r3:7.4f}   T^2 = {t2:7.4f}   T^2/R^3 = {t2 / r3:.4f}")

# =============================================================================
# Step 2: straight-line fit  T^2 = slope * R^3 + intercept
# =============================================================================
slope, intercept = np.polyfit(R_cubed, T_squared, 1)
fitted = slope * R_cubed + intercept
ss_res = np.sum((T_squared - fitted) ** 2)
ss_tot = np.sum((T_squared - T_squared.mean()) ** 2)
r_squared = 1 - ss_res / ss_tot

print(f"Linear fit : T^2 = {slope:.4f} * R^3 + {intercept:.4f}   (R^2 = {r_squared:.6f})")

# =============================================================================
# Step 3: log-log fit  log T = p * log R + c   (expected p = 1.5)
# =============================================================================
p, c = np.polyfit(np.log(R), np.log(T), 1)
print(f"Log-log fit: T ~ R^p with p = {p:.4f}   (Kepler: p = 1.5)")

# =============================================================================
# Step 4: draw the graphs
# =============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left: T^2 against R^3 with the fitted line
x_line = np.linspace(0, R_cubed.max() * 1.05, 100)
ax1.plot(x_line, slope * x_line + intercept, color='gray', linestyle='--',
         label=f'Fit: slope = {slope:.4f}, $R^2$ = {r_squared:.5f}')
ax1.scatter(R_cubed, T_squared, color='purple', s=60, zorder=5, label='Planet data')
for i, name in enumerate(planets):
    ax1.annotate(name, (R_cubed[i], T_squared[i]), textcoords="offset points",
                 xytext=(0, 10), ha='center')
ax1.set_title("$T^2$ against $R^3$")
ax1.set_xlabel("Distance cubed, $R^3$ (AU$^3$)")
ax1.set_ylabel("Period squared, $T^2$ (years$^2$)")
ax1.grid(True)
ax1.legend(loc='upper left', fontsize=8)

# Right: log-log plot, the slope should be 1.5
x_log = np.linspace(R.min() * 0.9, R.max() * 1.1, 100)
ax2.loglog(x_log, np.exp(c) * x_log**p, color='gray', linestyle='--',
           label=f'Fit: slope = {p:.3f}')
ax2.loglog(R, T, 'o', color='purple', markersize=8, label='Planet data')
for i, name in enumerate(planets):
    ax2.annotate(name, (R[i], T[i]), textcoords="offset points",
                 xytext=(0, 10), ha='center')
ax2.set_title("Log-log plot: $T \\propto R^{p}$, expected $p = 1.5$")
ax2.set_xlabel("Distance, $R$ (AU)")
ax2.set_ylabel("Period, $T$ (years)")
ax2.grid(True, which='both')
ax2.legend(loc='upper left', fontsize=8)

fig.suptitle("Kepler's 3rd Law - MTH600 Project - Meesam Raza")

plt.savefig("keplers_3rd_law_plot.png", dpi=150, bbox_inches='tight')
print("Done! Picture saved as keplers_3rd_law_plot.png")
plt.show()
