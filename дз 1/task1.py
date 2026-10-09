import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from fontTools.diff import color

def per(s):
    s = s.split(".")
    return int(s[0]) + int(s[1])/10

f = open('iris_data.txt')
print(f.readline())

iris0 = ["" for i in range(150)]
for i in range(150):
    iris0[i] = f.readline()[:-2].split(",")

f.close()

Rasm = [["Iris-setos","50"],["Iris-versicolor","50"],["Iris-virginica","50"]]

A1 = [[per(iris0[i][1]) for i in range(49)], [per(iris0[i][1]) for i in range(50, 99)], [per(iris0[i][1]) for i in range(100, 149)]]
A2 = [[per(iris0[i][2]) for i in range(49)], [per(iris0[i][2]) for i in range(50, 99)], [per(iris0[i][2]) for i in range(100, 149)]]
A3 = [[per(iris0[i][3]) for i in range(49)], [per(iris0[i][3]) for i in range(50, 99)], [per(iris0[i][3]) for i in range(100, 149)]]
A4 = [[per(iris0[i][4]) for i in range(49)], [per(iris0[i][4]) for i in range(50, 99)], [per(iris0[i][4]) for i in range(100, 149)]]


plt.figure()
plt.plot(A1[0], A2[0], "o", color="red", label = "iris_setos")
plt.plot(A1[1], A2[1], "o", color="blue", label = "iris_versicolor")
plt.plot(A1[2], A2[2], "o", color="green", label = "iris_virginica")

k, m = np.polyfit(A1[0], A2[0], 1)
r = np.corrcoef(A1[0], A2[0],)[0, 1]
plt.plot([min(A1[0]), max(A1[0])], [min(A1[0])*k + m, max(A1[0])*k + m], color="red", label = f"setos: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

k, m = np.polyfit(A1[1], A2[1], 1)
r = np.corrcoef(A1[1], A2[1],)[0, 1]
plt.plot([min(A1[1]), max(A1[1])], [min(A1[1])*k + m, max(A1[1])*k + m], color="blue", label = f"versicolor: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

k, m = np.polyfit(A1[2], A2[2], 1)
r = np.corrcoef(A1[2], A2[2],)[0, 1]
plt.plot([min(A1[2]), max(A1[2])], [min(A1[2])*k + m, max(A1[2])*k + m], color="green", label = f"virginica: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

plt.legend()
plt.title("sepal-x/leght-y")


plt.figure()
plt.plot(A2[0], A3[0], "o", color="red", label = "iris_setos")
plt.plot(A2[1], A3[1], "o", color="blue", label = "iris_versicolor")
plt.plot(A2[2], A3[2], "o", color="green", label = "iris_virginica")

k, m = np.polyfit(A2[0], A3[0], 1)
r = np.corrcoef(A2[0], A3[0],)[0, 1]
plt.plot([min(A2[0]), max(A2[0])], [min(A2[0])*k + m, max(A2[0])*k + m], color="red", label = f"setos: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

k, m = np.polyfit(A2[1], A3[1], 1)
r = np.corrcoef(A2[1], A3[1],)[0, 1]
plt.plot([min(A2[1]), max(A2[1])], [min(A2[1])*k + m, max(A2[1])*k + m], color="blue", label = f"versicolor: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

k, m = np.polyfit(A2[2], A3[2], 1)
r = np.corrcoef(A2[2], A3[2],)[0, 1]
plt.plot([min(A2[2]), max(A2[2])], [min(A2[2])*k + m, max(A2[2])*k + m], color="green", label = f"virginica: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

plt.legend()
plt.title("leght-x/widght-y")


plt.figure()
plt.plot(A3[0], A4[0], "o", color="red", label = "iris_setos")
plt.plot(A3[1], A4[1], "o", color="blue", label = "iris_versicolor")
plt.plot(A3[2], A4[2], "o", color="green", label = "iris_virginica")

k, m = np.polyfit(A3[0] + A3[1] + A3[2], A4[0] + A4[1] + A4[2], 1)
r = np.corrcoef(A3[0] + A3[1] + A3[2], A4[0] + A4[1] + A4[2])[0, 1]
plt.plot([1, 7], [1*k + m, 7*k + m], color="black", label = f"general k = {k:.2f} m = {m:.2f} r = {r:.2f}")

k, m = np.polyfit(A3[0], A4[0], 1)
r = np.corrcoef(A3[0], A4[0],)[0, 1]
plt.plot([min(A3[0]), max(A3[0])], [min(A3[0])*k + m, max(A3[0])*k + m], color="red", label = f"setos: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

k, m = np.polyfit(A3[1], A4[1], 1)
r = np.corrcoef(A3[1], A4[1],)[0, 1]
plt.plot([min(A3[1]), max(A3[1])], [min(A3[1])*k + m, max(A3[1])*k + m], color="blue", label = f"versicolor: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

k, m = np.polyfit(A3[2], A4[2], 1)
r = np.corrcoef(A3[2], A4[2],)[0, 1]
plt.plot([min(A3[2]), max(A3[2])], [min(A3[2])*k + m, max(A3[2])*k + m], color="green", label = f"virginica: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

plt.legend()
plt.title("widght-x/PetalLength-y")


plt.figure()
plt.plot(A1[0], A4[0], "o", color="red", label = "iris_setos")
plt.plot(A1[1], A4[1], "o", color="blue", label = "iris_versicolor")
plt.plot(A1[2], A4[2], "o", color="green", label = "iris_virginica")

k, m = np.polyfit(A1[0], A4[0], 1)
r = np.corrcoef(A1[0], A4[0],)[0, 1]
plt.plot([min(A1[0]), max(A1[0])], [min(A1[0])*k + m, max(A1[0])*k + m], color="red", label = f"setos: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

k, m = np.polyfit(A1[1], A4[1], 1)
r = np.corrcoef(A1[1], A4[1],)[0, 1]
plt.plot([min(A1[1]), max(A1[1])], [min(A1[1])*k + m, max(A1[1])*k + m], color="blue", label = f"versicolor: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

k, m = np.polyfit(A1[2], A4[2], 1)
r = np.corrcoef(A1[2], A4[2],)[0, 1]
plt.plot([min(A1[2]), max(A1[2])], [min(A1[2])*k + m, max(A1[2])*k + m], color="green", label = f"virginica: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

plt.legend()
plt.title("sepal-x/PetalLength-y")


plt.figure()
plt.plot(A2[0], A4[0], "o", color="red", label = "iris_setos")
plt.plot(A2[1], A4[1], "o", color="blue", label = "iris_versicolor")
plt.plot(A2[2], A4[2], "o", color="green", label = "iris_virginica")

k, m = np.polyfit(A2[0], A4[0], 1)
r = np.corrcoef(A2[0], A4[0],)[0, 1]
plt.plot([min(A2[0]), max(A2[0])], [min(A2[0])*k + m, max(A2[0])*k + m], color="red", label = f"setos: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

k, m = np.polyfit(A2[1], A4[1], 1)
r = np.corrcoef(A2[1], A4[1],)[0, 1]
plt.plot([min(A2[1]), max(A2[1])], [min(A2[1])*k + m, max(A2[1])*k + m], color="blue", label = f"versicolor: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

k, m = np.polyfit(A2[2], A4[2], 1)
r = np.corrcoef(A2[2], A4[2],)[0, 1]
plt.plot([min(A2[2]), max(A2[2])], [min(A2[2])*k + m, max(A2[2])*k + m], color="green", label = f"virginica: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

plt.legend()
plt.title("leght-x/PetalLength-y")


plt.figure()
plt.plot(A1[0], A3[0], "o", color="red", label = "iris_setos")
plt.plot(A1[1], A3[1], "o", color="blue", label = "iris_versicolor")
plt.plot(A1[2], A3[2], "o", color="green", label = "iris_virginica")

k, m = np.polyfit(A1[0], A3[0], 1)
r = np.corrcoef(A1[0], A3[0],)[0, 1]
plt.plot([min(A1[0]), max(A1[0])], [min(A1[0])*k + m, max(A1[0])*k + m], color="red", label = f"setos: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

k, m = np.polyfit(A1[1], A3[1], 1)
r = np.corrcoef(A1[1], A3[1],)[0, 1]
plt.plot([min(A1[1]), max(A1[1])], [min(A1[1])*k + m, max(A1[1])*k + m], color="blue", label = f"versicolor: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

k, m = np.polyfit(A1[2], A3[2], 1)
r = np.corrcoef(A1[2], A3[2],)[0, 1]
plt.plot([min(A1[2]), max(A1[2])], [min(A1[2])*k + m, max(A1[2])*k + m], color="green", label = f"virginica: k = {k:.2f} m = {m:.2f} r = {r:.2f}")

plt.legend()
plt.title("sepal-x/widght-y")

plt.show()