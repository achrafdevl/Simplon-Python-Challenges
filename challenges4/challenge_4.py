import numpy as np


matrice1 =np.array([ [1, 2], [3, 4] ])
matrice2 =np.array([ [5, 6], [7, 8] ])


multiplication = np.dot(matrice1 , matrice2)
print(multiplication)
print("*************")
transpose = np.transpose(multiplication)
print(transpose)

print("*************")
inverse= np.linalg.inv(multiplication)
print(inverse)
