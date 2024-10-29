import numpy as np
import matplotlib .pyplot as plt
def cyclic_delay(x,m):
 y=[]
 N=len(x)
 for n in range(0,N):
    if n-m>=0:
      idx=(n-m)%N
    else:
      idx=N+(n-m)
    y.append(x[idx])
 return(y)
x=[0,1,2,3]
m=int(input("enter the value of delay:")) 
y=cyclic_delay(x,m)
print(y)
def circular_convolution(x1,x2):
    N=len(x1)
    y=np.zeros(N)
    for n in range(N):
        y[n] = sum(x1[m]*x2[(n-m)% N] for m in range(N))
    return y
x1=[1,2,0,1]
x2=[2,2,1,1]
print( circular_convolution(x1,x2))
plt.plot(circular_convolution(x1,x2))
plt.show()
