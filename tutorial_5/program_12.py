import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

plt.figure(figsize=(10, 6))

plt.plot(x, y1, label='Sine Wave (sin(x))', color='blue', linestyle='-')

plt.plot(x, y2, label='Cosine Wave (cos(x))', color='red', linestyle='--')

plt.plot(x, y3, label='Product (sin(x)*cos(x))', color='green', linestyle=':')

plt.xlabel('X-axis Label (e.g., Time)')
plt.ylabel('Y-axis Label (e.g., Amplitude)')

plt.title('Plotting Multiple Lines on the Same Graph')

plt.legend()

plt.grid(True)

print("Displaying plot with multiple lines, labels, title, and legend...")
plt.show()