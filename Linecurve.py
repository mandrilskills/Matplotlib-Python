import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [1,4,9,16,25]
# Create plot
plt.plot(x, y, label="Line", color='red', linestyle='--')
# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
# Show plot
plt.show()
