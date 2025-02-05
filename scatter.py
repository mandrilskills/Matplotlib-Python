#Scatter plots
import matplotlib.pyplot as plt
hours = [2,3,5,1,4,6,7,8]
score = [70, 80, 85, 50, 90, 92, 95, 98]
plt.scatter(hours, score)
plt.title("Scatter Plot of Hours Studied v/s Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.grid(True)
plt.show()