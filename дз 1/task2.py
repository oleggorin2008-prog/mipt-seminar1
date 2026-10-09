import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random as rnd
import tkinter as tk

x = 0
A = [0]*1000

for i in range(1000):
    if rnd.random() > 0.5:
        x += 1
    else:
        x -= 1
    A[i] = x

plt.figure()
plt.plot(A, ms = 1)
plt.xlabel('номер шага, N')
plt.ylabel("координата x")
plt.title("график отдельной точки")

F = [0]*1000
for i in range(1000):
    x = 0
    for j in range(1000):
        if rnd.random() > 0.5:
            x += 1
        else:
            x -= 1
    F[i] = x

plt.figure()
plt.hist(F, bins=100, color="skyblue", edgecolor="black", alpha=0.7)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.xlabel("координата x в конце")
plt.title("гистограма количество точек, дошедших до опр. x")

F2 = [abs(F[i]) for i in range(1000)]

plt.figure()
plt.hist(F2, bins=50, color="red", edgecolor="black", alpha=0.7)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.xlabel("модуль координаты x в конце")
plt.title("гистограма модуля x")

#теперь иследуем зависимость корня N от ср.квад. отклонение x

sqrN = np.array([i for i in range(1000, 10000, 100)])
std = [0]*90
Polk = np.array([0 for i in range(250)])

for i in range(90):
    for gi in range(250):
        x = 0
        for j in range(sqrN[i]):
            if rnd.random() > 0.5:
                x += 1
            else:
                x -= 1
        Polk[gi] = x
    std[i] = np.std(Polk)

plt.figure()
ssqrN = np.sqrt(sqrN)
k, b = np.polyfit(ssqrN, std, 1)
r = np.corrcoef(ssqrN, std)[0, 1]
plt.plot([40, 100], [40*k + b, 100*k + b], color="blue")
plt.plot(ssqrN, std, "o", ms = 2, color = "blue")
plt.xlabel('корень из количество шагов (sqrt(N))')
plt.ylabel("средне квадратичное x из 100 прогонов")
plt.title("график для множества точек")

print( "Для иследование зависимости я постороил график станд.откл. от корня(N). Апроксимируя график получил k=",k," кореляция =",r)

plt.show()

