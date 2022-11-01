#Ejercicio 1:
# Los arrays `u` y `v` representan dos series en función del tiempo `t`.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

t = np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6, 0.8, 0.9])
u = np.array([-12.,-45.,-6.,-78.,-34.,-22.,10.,-31.,27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])
# 1) Grafique las dos series de datos en una misma imagen y guarde dicha gráfica sn mostrarla en'serie.pdf' 
plt.plot(t,u,label='u')
plt.plot(t,v,label='v')
plt.legend()
plt.xlabel('t')
plt.ylabel('Valor')
plt.savefig('serie.pdf')
plt.close()
# 2) Calcule la covarianza entre `u` y `v` e imprima su valor.
def cov(x,y):
  return np.sum((x-np.average(x))*(y-np.average(y)))/(np.size(x)-1) #Use la formula establecida para una muestra
print(f'La covarianza (muestral) entre u y v es {cov(u,v)}')
# 3) Calcule la varianza de `u` e imprima su valor.
def var(x):
  return np.sum((x-np.average(x))**2)/(np.size(x)-1)
print(f'La varianza (muestral) de u es {var(u)}')
# 4) Imprima un mensaje donde explique qué puede inferir del valor de covarianza obtenido.
print('Dada la covarianza muestral de -363.6375, se puede indicar que cuando u aumenta, \n v disminuye, lo que vendría siendo que son fuertemente inversamente proporcionales')
# 5) Construya un código para obtener la matriz de covarianza de los datos anteriores. (compare su resultado con el de numpy.cov)
def cov_matr(x):
  cm=np.zeros((len(x),len(x)))
  for file1,col in zip(x,range(np.size(x))):
    for file2,row in zip(x,range(np.size(x))):
      if col==row:
        cm[row,col]=var(file1)
      else:
        cm[row,col]=cov(file1,file2)
  return cm
print(f'Con mi codigo:\n {cov_matr(np.array([u,v]))}')
print(f'Con numpy:\n {np.cov(u,v)}')
# 6) Repita lo anterior para obtener la matriz de covarianza de los datos del archivo: room-temperature.csv
print('room-temperature')
df=pd.read_csv('room-temperature.csv')
x=df.iloc[:,1:].values
x1=cov_matr(x.T)
print(f'Con mi codigo:\n {x1}')
x2=np.cov(x.T)
print(f'Con numpy:\n {x2}')
# 6a) Grafique las 4 series de datos en una misma imagen y guarde dicha gráfica sin mostrarla en 'serieTemp.pdf'
plt.figure(figsize=(32,24)) 
plt.plot(df.iloc[:,0].values,df.iloc[:,1].values,label='FrontLeft')
plt.plot(df.iloc[:,0].values,df.iloc[:,2].values,label='FrontRight')
plt.plot(df.iloc[:,0].values,df.iloc[:,3].values,label='BackLeft')
plt.plot(df.iloc[:,0].values,df.iloc[:,4].values,label='BackRight')
plt.legend()
plt.xlabel('t')
plt.ylabel('Temperatura')
plt.xticks((df.iloc[:,0].values)[0:-1:10])
plt.savefig('serieTemp.pdf')
plt.close()
# 7) Calcule los autovalores y los autovectores de la matriz de covarianza de los datos de temperatura.
#(use el paquete: https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html)
eval,evec=np.linalg.eig(x1)
print(f'Los autovalores para la matriz de covarianza (sin estandarizar) es:\n {eval}')
print(f'Los autovectores para la matriz de covarianza (sin estandarizar) es:\n {evec}')
# 8) Lea: https://towardsdatascience.com/a-one-stop-shop-for-principal-component-analysis-5582fb7e0a9c
#Organice sus autovalores y autovectores e imprima cuales son sus componentes principales (puede usar
#paquetes de numpy para encontrar autovalores y autovectores. lea cuidadosamente la documentación.)
xs=x-np.mean(x,axis=0)
x3=np.cov(xs.T)
print(f'Con numpy estandarizados:\n {x2}') #Lo mismo!
sorted_index = np.argsort(eval)[::-1]#Fragmento de codigo extraido de ___
evals = eval[sorted_index]
evecs= evec[:,sorted_index]

# 9) Imprima cuantos componentes principales considera que son necesarios para explicar sus datos.
n=3
evecn = evecs[:,0:n]
xred=np.dot(xs,evecn)
# 10) Grafique sus datos en el nuevo sistema de referencia (PC1 PC2)
pca1 = pd.DataFrame(xred , columns = ['PC1','PC2','PC3'])
pca1 = pd.concat([pca1,df.iloc[:,0] ] , axis = 1)

fig = plt.figure()
plt.figure(figsize = (32,24))
ax0 = fig.add_subplot(221, projection='3d')
ax1 = fig.add_subplot(222)
ax2 = fig.add_subplot(223)
ax3 = fig.add_subplot(224)
print('De izquierda a derecha y de arriba a abajo (x,y,z): PC1,PC2,PC3;PC1,PC2;PC2,PC3;PC1,PC3')
ax0.scatter3D(xs=pca1['PC1'],ys=pca1['PC2'],zs=pca1['PC3'],c=(pd.to_datetime(df.iloc[:,0]).dt.hour),cmap= 'hsv')
ax1.scatter(pca1['PC1'], pca1['PC2'],c =pd.to_datetime(df.iloc[:,0]).dt.hour, s = 60 , cmap= 'hsv')
ax1.legend()
ax2.scatter(pca1['PC2'], pca1['PC3'],c =pd.to_datetime(df.iloc[:,0]).dt.hour, s = 60 , cmap= 'hsv')
ax3.scatter(pca1['PC1'], pca1['PC3'],c =pd.to_datetime(df.iloc[:,0]).dt.hour, s = 60 , cmap= 'hsv')
fig.set_figheight(15)
fig.set_figwidth(15)
#sb.scatter3D(data = pca1, x = 'PC1',y = 'PC2',z='PC3',hue =pd.to_datetime(df.iloc[:,0]).dt.hour, s = 60 , palette= 'hsv')
plt.show()
plt.close()
# 11) Comente cuales son las agrupaciones de sus variables originales que aparecen. Mire en su gráfica
# de los datos originales si el resultado tiene sentido.
#[COMENTARIO]
#Se pueden evidencair 2 agrupamientos principales basados en el estudio de 2 a 3 componentes principales.
#Estos principalemente se dividen con respecto a un rango horarios siendo el de mas densidad de puntos comprendido entre las
# 0 y 8 horas, ientras las demas estan mas dispersas. 