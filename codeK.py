import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Accceleration(g) = GM/R^2
# Where G is gravitational constant,M is mass of Earth amd R is radius of earth

R = 6378    # Radius is in kilometers
g = 9.8     # Acceleration due to gravity is in m/s^2

dist = np.array([0, R/4, R/2, 3*R/4, R, 5*R/4, 3*R/2, 7*R /
                4, 2*R, 5*R/2, 3*R, 7*R/2, 4*R, 9*R/2, 5*R])
acc = np.array([0, g/4, g/2, 3*g/4, g, 16*g/25, 4*g/9, 16*g/49,
               g/4, 4*g/25, g/9, 4*g/49, g/16, 4*g/81, g/25])

plt.plot(dist, acc, 'g-')
plt.xlabel("Radius(km)")
plt.ylabel("Gravity(m/s^2)")
plt.title("Earth's Gravity", fontdict={
          'fontname': 'Comic Sans MS', 'fontweight': 'bold', 'fontsize': 15})
plt.legend(['Gravity'])
plt.show()


# Data analysis on Planets

planetdata = pd.read_csv("dataK.csv")
print(planetdata)
plt.figure(figsize=(20, 10))

plt.subplot(2, 2, 1)
plt.plot(planetdata.Body, planetdata.Mass, 'g-o')
plt.ylabel("Mass of planets in 10^24kg")
plt.legend(['Mass'])

plt.subplot(2, 2, 2)
plt.plot(planetdata.Body, planetdata.Radius, 'r-x')
plt.ylabel("Radius of planets in km")
plt.legend(['Radius'])

plt.subplot(2, 2, 3)
plt.plot(planetdata.Body, planetdata.Acceleration_due_to_Gravity, 'b-*')
plt.ylabel("Gravity of planets in m/s^2")
plt.legend(['Gravity'])

plt.subplot(2, 2, 4)
plt.plot(planetdata.Body, planetdata.Density, 'm-+')
plt.ylabel("Density of planets in kg/m^3")
plt.legend(['Density'])

plt.suptitle("Planetary Data")

plt.show()


# Elements classification

elements = pd.read_csv("elementsK.csv")
print(elements)
color = ["green", "blue", "hotpink", "red", "orange", "yellow"]

plt.pie(elements.Number_of_elements,
        labels=elements.Types_of_Elements, startangle=0, colors=color)
plt.legend()
plt.title("Elements", fontdict={
          'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 16})

plt.show()
