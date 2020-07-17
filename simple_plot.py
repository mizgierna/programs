import numpy as np
import matplotlib.pyplot as plt

filename = "inflammation.csv"
data = np.loadtxt(filename, delimiter=',')
print(data)
print('data dimensions', data.shape)

fig = plt.figure(figsize=(8.,2.),facecolor="blue")

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('avg')
axes1.plot(data.mean(axis=0))

axes2.set_ylabel('maximum')
axes2.plot(data.max(axis=0))

axes3.plot(data.min(axis=0))
axes3.set_ylabel('minimum')

plt.show()
print("You just modified an R script!")