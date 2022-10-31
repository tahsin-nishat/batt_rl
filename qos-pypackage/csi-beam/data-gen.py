"""Console script for qos."""
#%matplotlib nbagg

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
import sysid
from scipy import io

''' ----- Create a sensor network for a beam with 10 sensors spaced symmetrically from each other---
input for simulating beam geometry
n=# of sensor nodes activated in the network excluding the two support nodes
Lt= Total length of the beam (feet)
Im= Moment of inertia (in^4)
E= modulus of elasticity (psi)
m_bar= mass density per unit length (lb.sec^2/in/in)'''
#pos=np.array([0,10,12.5,16.7,25,30,37.5,50,62.5,70,75,83.3,87.5,90,100])*12
pos=np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])*12
s=np.array([0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1])
pos_n=pos*s
pos_n=pos_n[np.nonzero(pos_n)]
pos_n=np.r_[0,pos_n]
n=len(pos_n)-2

data = np.load("node19data.npz")
y = data["y"]
fs = data["fs"]
s=s[1:-1]
y_n=y*np.array([s]).T
y_n=y_n[~np.all(y_n == 0, axis=1)]

bm = sysid.utils.Beam(pos_n, Im=100, E=6.58*1e6, m_bar=0.1)
"""
n=len(pos)-2

bm = sysid.utils.Beam(pos, Im=100, E=6.58*1e6, m_bar=0.1)


# Determine the time discretization and period

Tmax = 1. / sysid.utils.w2f(bm.get_natural_frequency(1))
fmax = sysid.utils.w2f(bm.get_natural_frequency(n))

'''
T = 1000 * Tmax
fs = 5 * fmax'''

T=180.0
fs=512.0
t = np.arange(0., T, 1 / fs)

# Define loads on system
## Unmeasureable: Stochastic loads on all nodes (Process noise)
w = np.random.normal(size=(n, t.size))*1e1

## Load matrix, f
F = w.copy() # checked random noise looks ok

# Simulate response, displacement at each node measured
_, _, y0 = bm.simulate(t, F)

noise_std = y0.std()

# Add measurement noise
v = np.random.normal(size=y0.shape)* noise_std*15*1e-2
y = y0 + v

plt.figure("Displacement measured last node")
plt.plot(t, y[-1], label="w/noise")
plt.plot(t, y0[-1], label="wo/noise")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.figure("PSD of Displacement at last node")
for yi in [y[-1], y0[-1]]:
    freqs, Pyy = scipy.signal.csd(yi,yi, fs, nperseg=2 ** 12)
    plt.semilogy(freqs, Pyy)
    plt.xlim([0,fmax+10])

for m in range(n):
    plt.axvline(sysid.utils.w2f(bm.get_natural_frequency(m+1)), alpha=.2)

plt.ylabel('PSD')
plt.xlabel('Frequency (Hz)')
plt.show()
"""
bm.set_rayleigh_damping_matrix([bm.get_natural_frequency(1), bm.get_natural_frequency(n)], [.05]*2)

true_frequencies = np.array([bm.get_natural_frequency(i)/(2*np.pi) for i in range(1, n+1)])
true_damping = np.array([bm.get_rayleigh_damping_ratio(i) for i in range(1, n+1)])
true_modeshapes = np.array([bm.get_mode_shape(i) for i in range(1, n+1)])

#io.savemat("nodepeakdata.mat",{'y':y,'fs':fs,'f':true_frequencies,'xi':true_damping,'phi':true_modeshapes,'posSensors':pos})

#print(np.shape(y))

np.savez('node19-11-1data',
         y=y_n, fs=fs,
         true_frequencies=true_frequencies,
         true_damping=true_damping,
         true_modeshapes=true_modeshapes,
         sensor_pos=pos_n
         )
print(np.size(true_frequencies))
print(np.shape(true_modeshapes))
print(np.shape(y_n))
print(np.shape(y))
