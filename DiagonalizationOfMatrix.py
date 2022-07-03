import numpy as np
from numpy import linalg as la

mat = np.array ( [ [1,2,3],[3,4,5],[7,3,4] ] )
#mat = np.array ( [ [1,0,0],[0,1,0],[0,0,1] ] )
print (mat)

#print (la.eig(mat))
dummy,P = la.eig(mat)
#print("P is ",P)

P2= la.inv(P)
#print (la.inv(P))

D = P2 @ mat @ P
print("final\n",D)
print(np.round(D,10))

#print ("Ev from func\n", dummy)
#print ("Diagonal elements\n",np.diagonal(D) )

