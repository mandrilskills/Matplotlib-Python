import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,100)
y = np.sin(x)   #take sin value of all the points plotted on x-axis
z= np.cos(x)
#Plotting the data
plt.plot(x,y)
plt.title("Sinusoidal Graph")
plt.xlabel("Angle")
plt.ylabel("Sin values")
plt.show()
