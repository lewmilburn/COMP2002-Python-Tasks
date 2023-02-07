# ---------------------------------- #
#     COMP20O2 PROGRAMMING TASKS     #
#                                    #
#  WEEK 1, TASK 3 - NUMBY & MATPLOT  #
#                                    #
#        STARTED 7TH FEB 2023        #
#       COMPLETED 7TH FEB 2023       #
# ---------------------------------- #

# Get required libraries
import numpy as np
import matplotlib.pyplot as plt

# Generate values
x = np.linspace(-np.pi, np.pi, 256, True)

# Plot the values
plt.plot(x, np.sin(x))

plt.show()