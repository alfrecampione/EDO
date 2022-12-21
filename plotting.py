import project
import matplotlib.pyplot as plt
import numpy as np

time_max = 15
precision = 0.01
N = 200
S = 195
I = 5
a = 1.69
s, i, r = project.get_results(
    S / N, I / N, time_max, precision, f=project.runge_kutta_method
)
t = [0.0]
n = int(time_max / precision)
t0 = 0
for j in range(n):
    t1 = t0 + precision
    t.append(t1)
    t0 = t1
plt.plot(t, s)
plt.plot(t, i)
plt.plot(t, r)
# plt.savefig("photo.jpg")
plt.show()
