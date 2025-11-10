import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(1000) * 50
y_data = np.random.random(1000) * 50



# plt.scatter(x_data, y_data, c="#0f0", marker="*", s=150, alpha=0.3)
# years = [2006 + x for x in range(16)]
# print(years)
# weights = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80, 82, 82, 83, 89, 90, 90]

x = ["Python", "Java", "Go"]
y = [20, 30, 29]

# plt.plot(years, weights, color="red", lw=2, linestyle="--")
plt.bar(x,y, color="purple", align="edge", width=0.1, edgecolor = "green", linewidth=7)
plt.show()