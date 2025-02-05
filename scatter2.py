#Scatter Plots - Plotting Temperature
import matplotlib.pyplot as plt
temp = [25,30,35,40,20,15,28,33]
icecreamsale = [100,120,150,180,90,85,95,145]
plt.scatter(temp, icecreamsale, color='red', marker='o')
plt.title("Temperature v/s Ice Cream Sale Plot")
plt.xlabel("Temperature")
plt.ylabel("Ice Cream Sale")
plt.grid(True)
plt.show()