"""Console script for qos."""
#%matplotlib nbagg


import matplotlib.pyplot as plt
import numpy as np
import sysid
import scipy.signal
#----------------------------------------

data19 = np.load("node19data.npz")
y19 = data19["y"]
fs19 = data19["fs"]
true_f19 = data19["true_frequencies"]
true_xi19 = data19["true_damping"]
true_modeshapes19 = data19["true_modeshapes"]
sensor_pos19=data19["sensor_pos"]

s=np.array([0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])
data = np.load("node19-9data.npz")
y = data["y"]
fs = data["fs"]
true_f = data["true_frequencies"]
true_xi = data["true_damping"]
true_modeshapes = data["true_modeshapes"]
sensor_pos=data["sensor_pos"]
ssid = sysid.CovarianceDrivenStochasticSID(y, fs)
"""
_,T=(np.shape(y19))/fs
t = np.arange(0., T, 1 / fs)
plt.figure("Displacement measured node 1 and 10")
plt.plot(t, y19[9], label="node 10")
plt.plot(t, y19[0], label="node 1")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.figure("PSD of Displacement at 1 and 10 node")
for yi in [y19[0], y19[9]]:
    freqs, Pyy = scipy.signal.csd(yi,yi, fs, nperseg=2 ** 12)
    plt.semilogy(freqs, Pyy)
    plt.xlim(0,50)
plt.legend(['node 1','mode 10'])
plt.ylabel('PSD')
plt.xlabel('Frequency (Hz)')
plt.show()"""

modes = dict()
for i, order in enumerate(range(30, 100, 2)):
    A, C, G, R0 = ssid.perform(order, 20)
    modes[order] = sysid.Mode.find_modes_from_ss(A, C, fs)

sd = sysid.StabilizationDiagram()
sd.plot(modes)
f, psd = ssid.psdy(nperseg=2**12)
#sd.axes_psd.semilogy(f, np.trace(np.abs(psd)), color=(0., 0., 0., .5), lw=0.3)
for i in range(2):
    freqs, Pyy = scipy.signal.csd(y[i],y[i], fs, nperseg=2 ** 12)
    sd.axes_psd.semilogy(freqs, Pyy,color=(0., 0., 0.+i, .5), lw=0.3)

plt.show()

modes = sd.picked_modes

fig = plt.figure("Damping estimate")
axd = fig.add_axes((0.1, 0.1, .8, .8))
axd.set(xlabel='Frequency', ylabel='Damping ratio', title='Estimated and true frequency and damping',
        ylim=(0, .10)
        )
figmodes, axes = plt.subplots(ncols=5, nrows=4, dpi=144)
for n in range(true_f19.size):
    ax = axes.flatten()[n]
    un19 = true_modeshapes19[n]
    unn = true_modeshapes19[n, :true_f.size]
    fn19 = true_f19[n]
    xin19 = true_xi19[n]
    nmax = np.argmax([sysid.utils.modal_assurance_criterion(mode.v, unn) for mode in modes])
    mode = modes[nmax]
    line, = axd.plot(fn19, xin19, '.')
    line1, = axd.plot(mode.f, mode.xi, 'x',mec=line.get_color(), mfc=(0, 0, 0, 0))

    v_true = np.r_[0., un19, 0.]
    ax.plot(sensor_pos19, v_true, label='True', lw=0.1, marker='.', markersize=1)
    ax.tick_params(axis='x', labelsize=5)
    ax.tick_params(axis='y', labelsize=5)
    ax.axhline(0., color=(0, 0, 0, .3))

    ax.set_title(f"Mode {n + 1}", x=0.5, y=0.8, fontsize=6, fontweight="bold")
    ax.axis('on')
    ax.set_xlim(0, 1200)
    ax.set_ylim(-1, 1)
    plt.grid(True)
"""
res=[]
for n in range(true_f.size):
    ax = axes.flatten()[n]
    un = true_modeshapes[n]
    unn = true_modeshapes19[n]*s[1:-1]
    unn = unn[np.nonzero(unn)]
    nmax = np.argmax([sysid.utils.modal_assurance_criterion(mode.v, unn) for mode in modes])
    mode = modes[nmax]
    vn = np.r_[0., unn, 0.]
    v = np.r_[0., mode.v, 0.]
    v = sysid.utils.modal_scale_factor(v, vn) * v
    ax.plot(sensor_pos, v.real, label='Estimated', lw=0.1, marker='x', markersize=1)
    if n == 2:
        ax.legend(bbox_to_anchor=(.5, 1.20), loc='lower center', ncol=1)
        axd.legend(['True','Estimated'] )

    mac = sysid.utils.modal_assurance_criterion(unn, mode.v)
    msf=sysid.utils.modal_scale_factor(unn, mode.v)
    res.append([n, mac * 100, msf, ])

"""
#print(res)
plt.show()
#np.savetxt('mac19-9.txt',res,delimiter=',')
print("done")
