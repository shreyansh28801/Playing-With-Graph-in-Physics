import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

var = pd.read_csv('dataS.csv')
print(var)
plt.figure(figsize=(50, 100))


x = np.array([26, 71, 2, 1])
mylabels = ["Uranium", "Thorium", "Radium", "Polonium"]
plt.subplot(2, 3, 1)
plt.pie(x, labels=mylabels)
plt.title("Occurrance of Radioactive Elements in Earth")


sqrt_freq = np.array([0.5, 2])
atomic_no = np.array([1, 40])
plt.subplot(2, 3, 2)
plt.plot(atomic_no, sqrt_freq, marker='.')
plt.title("Moseley Law")
plt.xlabel("Atomic Number 'Z' ")
plt.ylabel("Sqrt_Frequency 'v' ")


x = np.linspace(0, 10, 256, endpoint=True)
y = (np.exp(-x))
plt.subplot(2, 3, 3)
plt.plot(x, y, '-g', label=r'$y = e^{-x}')
axes = plt.gca()
axes.set_xlim([x.min(), x.max()])
axes.set_ylim([y.min(), y.max()])
plt.xlabel("Time (seconds)")
plt.ylabel("No. of Particles")
plt.title("Radioactive Decay Law")


plt.subplot(2, 3, 4)
plt.bar(var.Element, var.Energy)
plt.title("Energy of Elements")


plt.subplot(2, 3, 5)
plt.scatter(var.Element, var.HalfLife)
plt.title("HalfLife of Radioactive Elements")


plt.subplot(2, 3, 6)
plt.plot(var.Element, var.NaturalConcentration, '*-.r')
plt.title("NaturalConcentration")

plt.show()