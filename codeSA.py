
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline


# In[2]:


pressure=np.array([10,15,20,25,30,35,40,45,50],dtype="int32")
t=300
volume=[]   

for i in pressure:
   x= (8.314*t)/i
   y=round(x,0)
   volume.append(y)
   

    
plt.subplot(2,2,1)

plt.xlabel("pressure")
plt.ylabel("volume")
plt.title("Pressure Volume - Boyle's Law",fontsize=20)

for i,value in enumerate(pressure):
    plt.annotate((value,volume[i]),(pressure[i],volume[i]))
    
s=UnivariateSpline(pressure,volume,s=0)
xs=np.linspace(10,50,500)
ys=s(xs)

plt.plot(xs,ys,color="blue")

plt.scatter(pressure,volume)


# In[3]:


t1=[]
pres=400
for i in volume:
   x= (i*pres)/8.314
   y=round(x,0)
   t1.append(y)

plt.subplot(2,2,2)
plt.xlabel("temperature")
plt.ylabel("volume")
plt.title("Charle's Law",fontsize=20)



plt.plot(t1,volume,color="blue")


# In[4]:


vol1=150
temp1=[]
for i in pressure:
   x= (i*vol1)/8.314
   y=round(x,0)
   temp1.append(y)


plt.subplot(2,2,3)
plt.ylabel("pressure")
plt.xlabel("temperature")
plt.title("Gay-Lussac's Law",fontsize=20)



plt.plot(temp1,pressure,color="blue")


# In[5]:


pr=350
te=400
n=[]
for i in volume:
   x= (i*pr)/(8.314*te)
   y=round(x,4)
   n.append(y)

plt.subplot(2,2,4)
plt.ylabel("N")
plt.xlabel("volume")
plt.title("Avagadro's Law",fontsize=20)



plt.plot(n,volume,color="blue")

plt.show()

