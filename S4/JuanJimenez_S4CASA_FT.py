import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq

# Construcción de la señal
N = 128 # number of point in the whole interval
f = 200.0 # frequency in Hz
dt = 1 / (f * 32 ) #32 samples per unit frequency
t = np.linspace( 0, (N-1)*dt, N)
y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t )+ 0.17*np.sin(2 * np.pi * (15*f) * t )
# Construcción de la señal
N = 128 # number of point in the whole interval
f = 200.0 # frequency in Hz
dt = 1 / (f * 32 ) #32 samples per unit frequency
t = np.linspace( 0, (N-1)*dt, N)
y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t )+ 0.17*np.sin(2 * np.pi * (15*f) * t )
# 1) implemente de la transformada de fourier discreta
def fourier(N,y):
  n=np.arange(0,N)
  k=n.reshape((-1, 1))
  return (np.dot(y,np.exp((2j*np.pi*k*n)/N))[range(int(N/2))])/(N)#Quitar espejo
# 2) Genere el arreglo de las frecuencias (ver documentación de fftfreq):
def arr_freq(N,dt):
  n=np.arange(0,N)
  return (n/(N*dt))[range(int(N/2))] #Quitar espejo
fy=fourier(N,y) 
fx=arr_freq(N,dt)
#3) Haga una gráfica comparando método propio con implementación de scipy.fftpack.fft
fft_x = fft(y) / N # FFT Normalized
freq = fftfreq(N, dt) # Recuperamos las frecuencias
fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(16,8))
# plt.figure(figsize=(24,12))
fig.suptitle('Comparación Fourier')
ax1.plot(freq[range(int(N/2))],abs(fft_x[range(int(N/2))]))
ax1.set_title('scipy.fftpack.fft')
ax2.plot(fx,abs(fy))
ax2.set_title('Mi Función')
plt.show()
import pandas as pd
# 1) Almacene los datos de signal.dat. La columna 1 es el tiempo y la columna 2 es su señal f(t).
#Grafique su señal en función del tiempo y guarde dicha gráfica sin mostrarla en signal.png.
df=pd.read_csv('signal.dat',header=None)
plt.plot(df.iloc[:,0],df.iloc[:,1])
plt.savefig('signal.png')
plt.close()
# 2) Use fftfreq (BONO si usa su implementación propia) y haga una gráfica de su transformada de
#fourier en función de las frecuencias. Guarde dicha gráfica sin mostrarla en Fourier_trans.png
fy=fourier(np.size(df.iloc[:,1]),df.iloc[:,1]) 
#fx=fftfreq(np.size(df.iloc[:,1]))
fx=(np.arange(np.size(df.iloc[:,1]))/(np.size(df.iloc[:,1])))[range(int(np.size(df.iloc[:,1])/2))]
plt.plot(fx,abs(fy),label='Todo')
plt.xlim(0,0.1)
# 3) Haga un filtro pasa bajos que le permita filtrar el ruido de la señal del punto 1. Use la gráfica de la
#transformada de fourier del punto 3 para determinar un valor apropiado de la frecuencia de corte que
#debe usar para filtrar dicho ruido de alta frecuencia.
fc=0.03 #frecuencia de corte filtro pasa-bajo
low_pass=fx.copy()

low_pass[low_pass<=fc]=np.NaN;low_pass[low_pass>fc]=float(0.0); #Creacion del filtro pasa-bajo basado en frq1
low_pass[low_pass!=float(0.0)]=1
fy2=fy*low_pass #Uso del filto pasa-bajo
plt.plot(fx,abs(fy2),label='Pasa bajo')
plt.savefig('Fourier_trans.png')
plt.close()
#Transformada de Fourier discreta: ejercicio 4-filtro ruido imagen
import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq
import scipy.fft
from scipy import fftpack
# 1) Almacene los datos de la imagen (use imread: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html)
img = plt.imread('moon.jpg')
fimg= scipy.fft.fft2(img)
# mask=fimg>np.percentile(fimg,90)
fiimg2=scipy.fft.ifft2(fimg)
x=20
val=0
fimg[0:x,0:x]=val #Arriba izquierda
#fimg[-x::,-x::]=val #Abajo derecha
fimg[0:x,-x::]=val #Arriba dereha
#fimg[-x::,0:x]=val  #Abajo izquierda
# plt.imshow(np.log(abs(fimg)))
fiimg=scipy.fft.ifft2(fimg)

plt.figure(num=None, figsize=(8, 6), dpi=80)

plt.imsave('LunaFiltrada.png',abs(fiimg),cmap='Greys_r',vmin=fiimg2.real.min(),vmax=fiimg2.real.max());
# Recupere la imagen original a partir de la fase y la amplitud de la transformada de fourier (archivos
# amplitude.dat y phase.dat).
import pandas as pd
mag=pd.read_csv('magnitude.dat',header=None,sep=' ');pha=pd.read_csv('phase.dat',header=None,sep=' ')
scipy.fft.ifft2(np.abs(mag.values)*np.exp((pha.values)*1j))
plt.imshow(scipy.fft.ifft2(np.abs(mag.values)*np.exp((pha.values)*1j)).real)
plt.close()
plt.imsave('amp_pha.png',scipy.fft.ifft2(np.abs(mag.values)*np.exp((pha.values)*1j)).real)