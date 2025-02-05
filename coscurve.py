import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,100)
y = np.sin(x)   #take sin value of all the points plotted on x-axis
z= np.cos(x)
#Plotting the data
plt.plot(x,z)
plt.title("Cosine Graph")
plt.show()
