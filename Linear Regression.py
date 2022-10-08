import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import math
h=[159,180,186,180,156,165,177.8,150,179,182,177,157,170,154,189,168,177,164,183,164,165,176.74,167,155.75,178,163,167,185,180,170,154,162,157,162.56,185,160,180,173,180,170,172.72,180,179,164,185,172,176,180,163,175,170,163,146,168,162,155,161,155.4,152.4,164,154,164,168,152,160,152.4,174,165,173.73,150,180,]
w=[46,85,95,58,65,60,71,36,52,70,78,47,70,40,72,74,66,48,82,65,67,80,44,64.3,55,59,65,70,60,45,67,48,47,60,82,58,68,76,52,58,60,67,68,54,65,68,60,58,45,79,78,75,43,48,50,56,55,46,44,63,45,57,62,39,54,50,55,55,60,44,80]
x=int(input("Enter Your Height:"))
ax = plt.axes()
ax.scatter(h,w,color='blue',s=10)
pf=np.polyfit(h,w,1)
m=pf[0]
c=pf[1]
y=[m*i+c for i in h]
h.append(x)
y.append(m*x+c)
ax.plot(h,y,color='red')
ax.scatter(x,m*x+c,color='green')
plt.title("Linear Regression")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.legend(handles=[mpatches.Patch(color='blue', label='Points'),mpatches.Patch(color='red', label='Best Fit Line'),mpatches.Patch(color='green', label='Input Height')])
print("Your Predicted Weight based on the Sample Data is "+str(m*x+c)+" Kgs")
plt.show()

