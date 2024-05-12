#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

plt.plot(y, color='red')  # Plotting y as a solid red line
plt.xlim(0, 10)  # Setting x-axis range from 0 to 10
plt.show()
