# ---------------------------------- #
#     COMP20O2 PROGRAMMING TASKS     #
#                                    #
#  WEEK 1, TASK 3 - NUMBY & MATPLOT  #
#                                    #
#        STARTED 7TH FEB 2023        #
#       COMPLETED 7TH FEB 2023       #
# ---------------------------------- #

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 256, True)

plt.plot(x, np.sin(x))
