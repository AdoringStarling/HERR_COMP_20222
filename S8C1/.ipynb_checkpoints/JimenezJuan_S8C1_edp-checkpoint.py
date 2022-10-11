import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('array.txt',delimiter=';',header=None)

for i in range(0,500,50):
	size=np.size(df.iloc[i,:])
	plt.plot(np.linspace(0,2,size),df.iloc[i,:],label='t_'+str(i))
plt.legend()
plt.savefig('cuerda.PNG')
plt.close()