import matplotlib.pyplot as plt
import numpy as np

# Create a heart shape
t = np.linspace(0, 2 * np.pi, 100)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Plot  with  symbols
plt.figure(figsize=(8,8))
plt.plot(x, y, color='pink')  # Plot the outline with white color to match background

# Fill the heart with ❤ symbols
for i in range(100):
    plt.text(x[i], y[i], '❤', fontsize=10, ha='center', va='center',color='red')

# Add text in the center
plt.text(0, 0, "You are so Beautiful", fontsize=30, color='pink', ha='center', va='center')

# Set limits and background
plt.xlim(-20, 20)
plt.ylim(-20, 20)
plt.gca().set_facecolor('red')
plt.axis('off')  # Hide axes

# Show the plot
plt.show()