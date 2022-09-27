import numpy as np
import matplotlib.pyplot as plt
x1=np.loadtxt('x1.txt')
y1=np.loadtxt('y1.txt')
y2=np.loadtxt('y2.txt')
y3=np.loadtxt('y3.txt')

plt.plot(x1,y1,label="Numerica")
plt.plot(x1,y2,label="Analitica")
plt.plot(x1,y3,label="Runge Kutta")
plt.legend()
plt.savefig('EULER.PNG')
plt.show()