import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

url='example1.txt'

narray=np.loadtxt(url)

plt.plot(narray,'.')
plt.savefig('aleatorios.png')
plt.close()

url='example2.txt'
narray1=np.loadtxt(url)

plt.plot(narray,'-')
plt.plot(narray1,'.')
plt.savefig('aleatorios_con_impares.png')

