from project import *
import matplotlib.pyplot as plt

s, i, r = get_results(100, 2, 10, 1)
plt.plot(s)
plt.plot(i)
plt.plot(r)
plt.show()
