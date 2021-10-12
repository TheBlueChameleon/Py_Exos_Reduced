print("Interpreter up and running.")

print("Loading numpy...", end="")
import numpy as np
print("okay.")

print("Loading matplotlib...", end="")
import matplotlib.pyplot as plt
print("okay.")

print("Creating a plot of sin(x)...", end="")

X = np.array([(x-500)/100 for x in range(1000)])
Y = np.sin(X)

plt.figure()
plt.plot(X, Y)
plt.show()

print("okay.")
