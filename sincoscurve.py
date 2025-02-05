import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,50)
plt.plot(x,np.sin(x),"g-")
plt.plot(x,np.cos(x),"r--")
plt.title("Sin and Cosine Curves")
plt.show()