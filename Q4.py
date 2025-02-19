import numpy as np
import matplotlib.pyplot as plt

# Exercise 4a

# Given function to sample (X, Y)
rng = np.random.default_rng()
def sampleXY(n):
    u1 = rng.random(n)
    xs = u1**0.25
    u2 = rng.random(n)
    ys = np.sqrt(u2) * xs / 2
    return xs, ys

# Generate samples
n_samples = 100000
X_samples, Y_samples = sampleXY(n_samples)

# Plot 2D Histogram
plt.figure()
plt.hist2d(X_samples, Y_samples, bins=200, density=True, cmap='Blues')
plt.colorbar(label="Density")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Density of Sampled (X, Y) Pairs")
plt.show()

# Exercise 4b

# Marginal density of X
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(X_samples, bins=50, density=True, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel("X")
plt.ylabel("Density")
plt.title("Marginal Density of X")

# Marginal density of Y
plt.subplot(1, 2, 2)
plt.hist(Y_samples, bins=50, density=True, alpha=0.7, color='green', edgecolor='black')
plt.xlabel("Y")
plt.ylabel("Density")
plt.title("Marginal Density of Y")

plt.tight_layout()
plt.show()
