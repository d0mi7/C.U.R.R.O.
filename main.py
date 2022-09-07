import matplotlib.pyplot as plt
import numpy as np
# x = np.arange(0.0, 2.0 , 0.01)
# y = 1 + np.sin(2 * np.pi * t)

theta = np.linspace(0, 2 * np.pi, 100)

x = 16 * ( np.sin(theta) ** 3 )
y = 13 * np.cos(theta) - 5* np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)

ax = plt.subplot()

ax.plot(x, y)

# ax.set(xlabel="X -->", ylabel="Y -->", title="C.U.R.R.O.")
ax.set(xlabel="X -->", ylabel="Y -->", title="Python❤")
ax.grid()
plt.show()