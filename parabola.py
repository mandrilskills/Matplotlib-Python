import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,20)        #numbers between particular range
y=x**2                          #Parabola curve
plt.plot(x,y,'g+')
plt.title("Parabola curve")
plt.show()

