import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('t0.txt',delimiter=';',header=None)
df=df.drop(100, axis=1)
t0=df[0:100]
t100=df[100:200]
t1000=df[200:300]
t2500=df[300:400]

fig, axs = plt.subplots(2, 2,constrained_layout = True)
im=plt.imshow( t0.values, cmap='hot',vmin=0,vmax=100)
axs[0, 0].imshow( t0.values, cmap='hot',vmin=0,vmax=100)
axs[0, 0].set_title('T=0s')
axs[0, 1].imshow( t100.values, cmap='hot',vmin=0,vmax=100)
axs[0, 1].set_title('T=100s')
axs[1, 0].imshow( t1000.values, cmap='hot',vmin=0,vmax=100)
axs[1, 0].set_title('T=1000s')
axs[1, 1].imshow( t2500.values, cmap='hot',vmin=0,vmax=100)
axs[1, 1].set_title('T=2500s')
fig.colorbar(im, ax=axs.ravel().tolist(),label='Temperatura')

fig.savefig('diff.png')
plt.close()