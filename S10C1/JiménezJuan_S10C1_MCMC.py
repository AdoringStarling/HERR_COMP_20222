# Ejercicio 1

import numpy as np
import matplotlib.pylab as plt
# Use esta funcion que recibe un valor x y retorna un valor f(x) donde f es la forma funcional que debe seguir su distribucion. 
def mifun(x):
  x_0 = 3.0
  a = 0.01
  return np.exp(-(x**2))/((x-x_0)**2 + a**2)

sigma=[5,0.2,0.01,0.1,0.1]
pasos=[100000,100000,100000,1000,100000]


# Al ejecutar el codigo, este debe generar 6 (o 5) graficas .pdf una para cada vez que se llama a la funcion.
x=np.linspace(4,-4,100)
y=mifun(x)
# x_old = np.random.randint(-4, 4, 1)[0]
alm=[]
alm.append(np.random.randint(-4, 4, 1)[0])
for sig,pas in zip(sigma,pasos):
  for i in range(pas):
    x_new = np.random.normal(0, sig, 1000)
    x_new= np.interp(x_new, (x_new.min(), x_new.max()), (-4, 4))[0]
    # np.random.normal(x_old,sigma,1)[0]
    a=mifun(alm[-1]+x_new)/mifun(alm[-1])

    if a>1:
      alm.append(x_new+alm[-1])
      # x_old=x_new
    else:
      b=np.random.uniform(0, 1, 100)[0]
      if b<=a:
        alm.append(x_new+alm[-1])
        # x_old=x_new
      else:
        alm.append(alm[-1])


  #plt.hist(np.array(alm))
  plt.hist(np.array(alm), bins=40, density=True)
  plt.plot(x,y)
  plt.title("histograma_"+str(sig)+"_"+str(pas))
  plt.savefig("histograma_"+str(sig)+"_"+str(pas)+".pdf")
  plt.close()