import matplotlib.pyplot as plt
import numpy as np

x_axis = np.arange(0,5,0.1)

x=0

e_x = [np.exp(x) for x in x_axis]
    

plt.plot(x_axis, e_x)