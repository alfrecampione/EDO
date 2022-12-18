import project
import matplotlib.pyplot as plt

s, i, r = project.get_results(100, 2, 10, 0.01, f=project.runge_kutta_method)
plt.plot(s)
plt.plot(i)
plt.plot(r)
# plt.savefig("photo.jpg")
plt.show()
