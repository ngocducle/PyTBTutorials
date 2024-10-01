import numpy as np

N = 100

theta = np.pi/4 

phi = -N*np.arctan( (np.sin(theta/2))**2 * np.sin(2*np.pi/N) / ( (np.cos(theta/2)**2 + (np.sin(theta/2))**2 * np.cos(2*np.pi/N) ) ) )

print('phi = '+str(phi/np.pi)+'pi') 

X = -2.0*(np.sin(theta/2))**2 

print('X = '+str(X)+'pi')