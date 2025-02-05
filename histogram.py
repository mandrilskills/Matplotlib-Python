#Histogram plotting
import matplotlib.pyplot as plt
import numpy as np
exam = np.random.normal(70, 10, 200)
plt.hist(exam, bins=20, edgecolor ='black')
plt.title("Exam Histogram Graph")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()
