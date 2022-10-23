#Ejercicio 1 Terminar lo que hizo en clase + dos preguntas adicionales (en mayusculas en el texto)

import numpy as np
import matplotlib.pylab as plt
import pandas as pd
# 1) lea los datos de resorte.dat y almacenelos.
# 
d=pd.read_csv('resorte.dat',delim_whitespace=True,header=None)
# Los datos corresponden a las posiciones en x de un oscilador (masa resorte) en funcion del tiempo. La ecuacion de movimiento esta dada por
d=d.rename(columns={0:'t',1:'x'})
# xt=a*np.exp(-gamma*t)*np.cos(omega*t)
# Donde a, gamma, y omega son parametros que se busca determinar.
# 2) Implemente un algoritmo que le permita, por medio de estimacion bayesiana de parametros, encontrar los parametros correspondientes 
# a los datos d. Para esto debe:

# 2a.) definir una funcion que reciba los parametros que se busca estimar y los datos de tiempo y retorne los datos modelados  
def mod(t,a, gamma, omega):
    return a*np.exp(-gamma*t)*np.cos(omega*t)

# 2b.) Definir una funcion que retorne la funcion de verosimilitud
def ver(x0,x1):
    return np.exp(-((0.5)*sum(((x0-x1)/np.std(x0))**2)))
#condiciones iniciales: tomen por ejemplo:
aini=7.5
gammaini=0.6
omegaini=18.2

#numero de pasos: empiecen con 10000 y aumenten el número si ven que el algoritmo necesita mas pasos para converger.
iteraciones=10000
lw=np.array([])
aw=np.array([])
aw=np.append(aw, aini)
gw=np.array([])
gw=np.append(gw,gammaini)
ow=np.array([])
ow=np.append(ow,omegaini)
alw=np.array([0])

x=d['x'].values
t=d['t'].values

for i in range(iteraciones):
    a     = np.random.normal(aw[i]) 
    gamma = np.random.normal(gw[i])
    omega = np.random.normal(ow[i])
    xo = mod(t, aw[i], gw[i],ow[i])
    xn = mod(t, a,gamma,omega)
    lo = ver(x, xo)
    ln = ver(x, xn)
    alpha = ln/lo
    # print(alpha)
    alw=np.append(alw,alpha)
    if alpha<=1.0:
        aw=np.append(aw, a)
        gw=np.append(gw, gamma)
        ow=np.append(ow, omega)
        lw=np.append(lw, ln)
    else:
        b=np.random.uniform(0, 1, 100)[0]
        if b<alpha:
            aw=np.append(aw, a)
            gw=np.append(gw, gamma)
            ow=np.append(ow, omega)
            lw=np.append(lw, ln)
        else:
            aw=np.append(aw, aw[i])
            gw=np.append(gw, gw[i])
            ow=np.append(ow, ow[i])
            lw=np.append(lw, lo)
arg=np.argmin(np.abs(alw[(alw>0.99)&(alw<1.01)]-np.ones(len(alw[(alw>0.99)&(alw<1.01)]))))
print(f"LOS MEJORES PARAMETROS SON a={aw[alw==alw[(alw>0.99)&(alw<1.01)][arg]]} gamma={gw[alw==alw[(alw>0.99)&(alw<1.01)][arg]]} Y omgega={ow[alw==alw[(alw>0.99)&(alw<1.01)][arg]]}")
plt.plot(t, x ,'b--',label='Original')
plt.plot(t, mod(t, aw[alw==alw[(alw>0.99)&(alw<1.01)][arg]], gw[alw==alw[(alw>0.99)&(alw<1.01)][arg]],ow[alw==alw[(alw>0.99)&(alw<1.01)][arg]]), 'r--',label='Modelo')
plt.legend()
plt.savefig('Resorte.png')
plt.close()
print('Considero que si se puede saber de manera individual cual es k ó m, ya que gracias a que los dos son inputs de la función modelo, solo se cambian estas 2 variables. Eso sí, tardaría mas tiempo y no es del todo seguro que de un valor razonable, ya que se guardan las escalas.')