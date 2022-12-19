import project
import matplotlib.pyplot as plt

time_max = 15
precision = 0.01
s, i, r = project.get_results(200, 2, time_max, precision, f=project.runge_kutta_method)
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
