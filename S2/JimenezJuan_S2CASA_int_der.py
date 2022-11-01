import numpy as np
import matplotlib.pylab as plt
def f(x):
  return np.cos(x)
def fordiff(x0,xf,n):
  x=np.linspace(x0,xf,n)
  y=f(x)
  h=(xf-x0)/n
  yd=[]
  for t in range(n-1):
    if t!=n-1:
      yd.append((y[t+1]-y[t])/h)
  return x,y,yd
def centdiff(x0,xf,n):
  x=np.linspace(x0,xf,n)
  y=f(x)
  h=(xf-x0)/n
  yd=[]
  for t in range(n-1):
    if t==0:
      pass
    elif t!=n-1:
      yd.append(((
          ((y[t+1]+y[t])/2)-
           (y[t-1]+y[t])/2))/
           h)
    else:
      pass
  return x,y,yd
x,y,yd=fordiff(0,2*np.pi,100)
x1,y1,yd1=centdiff(0,2*np.pi,100)
plt.plot(x,y,label='Funcion')
plt.plot(x,-np.sin(x),label='Analitica')
plt.plot(x[:-1],yd,label='Forward Difference')
plt.plot(x1[1:-1],yd1,label='Central Difference')
plt.legend()
plt.savefig('DerivadaFun.png')
plt.close()
#Errores |(valor numérico - valor analitico)/valor analitico|
efordiff=(np.array(yd)-np.array(-np.sin(x)[:-1]))/np.array(-np.sin(x)[:-1])
ecentdiff=(np.array(yd1)-np.array(-np.sin(x)[1:-1]))/np.array(-np.sin(x)[1:-1])
fig, axs = plt.subplots(2)
fig.suptitle('Errores')
axs[0].plot(x[:-1],efordiff)
axs[1].plot(x[1:-1],ecentdiff)
plt.savefig('ErrorDerivada.png')
plt.close()
#Segunda derivada
def der2esc(x0,xf,n):
  x=np.linspace(x0,xf,n)
  y=f(x)
  h=(xf-x0)/n
  yd=[]
  for t in range(n-1):
    if t==0:
      pass
    elif t!=n-1:
      yd.append((
          y[t+1]+
          y[t-1]-
          (2*y[t]))/
           h**2)
    else:
      pass
  return x,y,yd
x2,y2,yd2=der2esc(0,2*np.pi,100)
x1,y1,yd1=centdiff(0,2*np.pi,100)
plt.plot(x,y)
plt.plot(x2[1:-1],yd2)
plt.savefig('2DerivadaFun.pdf')
plt.close()
#Rhampson
# Funcion polinomica
def poli(x):
  return (x**5)-(2.0*x**4)-(10.0*x**3)+(20.0*x*x)+ (9.0*x)-18.0

# Derivada de la funcion
def poli_dev(x):
    return (5*x**4)-(8*x**3)-(30*x**2)+(40*x)+ (9.0)

x=np.linspace(-5,5,1000)
y=poli(x)
plt.plot(x[4:-4],y[4:-4])
plt.savefig('JimenezJuan_NRpoli.pdf')
plt.close()
def newtonRaphson(x,e,N):
    for i in range(N):
        x1 = x - (poli(x)/poli_dev(x))
        if abs(x1-x)<e:
          print(f'Iteración N°{i} - x={x1} - f(x)={poli(x1)}')
          break
        else:
          print(f'Iteración N°{i} - x={x1} - f(x)={poli(x1)}')
          x=x+1
newtonRaphson(-3,0.0001,200)