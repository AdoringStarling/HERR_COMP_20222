import matplotlib.pyplot as plt
import numpy as np

x1=np.loadtxt('xeu.txt')
yeuv=np.loadtxt('yeuv.txt')
yeux=np.loadtxt('yeux.txt')

plt.plot(x1,yeuv,label="Velocidad")
plt.plot(x1,yeux,label="Desplazamiento")
plt.title("EULER")
plt.legend()
plt.savefig('EULER_1.PNG')
plt.close()

yrkv=np.loadtxt('yeuv.txt')
yrkx=np.loadtxt('yeux.txt')
plt.plot(x1,yrkv,label="Velocidad")
plt.plot(x1,yrkx,label="Desplazamiento")
plt.title("Runge Kutta")
plt.legend()
plt.savefig('Runge Kutta_1.PNG')
plt.close()
