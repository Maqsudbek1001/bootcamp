
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-125, 126, dtype=int)
y = x**2

plt.plot(x, y)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("Parabola (y = x^2)")

plt.show()