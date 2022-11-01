import numpy as np
N=6
a=(np.random.random((N,N))*10.0)-5.0
b=(np.random.random((N,1))*10.0)-5.0
for row in range(np.shape(a)[0]):
  b[row]=b[row]/a[row,row]
  a[row,:]=a[row,:]/a[row,row]
  for col in range(row+1,np.shape(a)[0]):
      b[col]=b[col]-b[row]*a[col,row]
      a[col,:]=a[col,:]-a[row,:]*a[col,row]
x=np.zeros(N)
x[N-1]=b[N-1]
for i in range(2,np.size(b)+1):
  x[N-i]=b[N-i]-np.sum((x*(a[N-i,:])))
print('Mi solución da:\n',x)
sol = np.linalg.solve(a, b)
 
print('Con numpy:\n',sol)
