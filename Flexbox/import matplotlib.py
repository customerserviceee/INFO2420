import matplotlib.pyplot as plt
import numpy as np

# Original function (approximate points from the graph)
x = np.linspace(1, 4.5, 400)
y = x**2 - 1  # This is a guess based on the shape; replace with actual if known

# Inverse function (reflection of y = f(x))
x_inv = y
y_inv = x

# Plotting
plt.figure(figsize=(6,6))
plt.plot(x, y, 'r', label='Original function')
plt.plot(x_inv, y_inv, 'b', label='Inverse function')
plt.plot([0, 5], [0, 5], 'k--', label='y = x')

plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function and Its Inverse')
plt.legend()
plt.grid(True)
plt.show()
