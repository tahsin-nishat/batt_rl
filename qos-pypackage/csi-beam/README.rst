=====
sysid
=====

Description of the "sysid" package
-----------------------------------
This is a python package for system identification of a simply supported beam. There are different system identification methods available 
for any structure (based on input and output data or output only data). However, in practice, measuring the input force properly is not 
always straightforward (due to traffic load or other environmental uncertainties). Also, the material characteristics can not be determined 
accurately. Therefore, output-based system identification is the practical solution. The current package utilize the output based covariance driven
stochastic system identification algorithm. We plot a stabilization diagram from the response data and select the stable poles to identify 
the natural frequencies, damping ratios and mode shapes. The response data are simulated by using several known parameters i.e. mass density, 
modulus of elasticity, moment of inertia, length of the bridge and number of sensor nodes and locations. Practical response data can also 
be used instead of simulated response data.

The main objective of this package is to automate the data generation and system identification of a real-life bridge system particularly 
for mode shapes for different sensor node configuration . We can set a reference mode shape for a specific sensor node configuration. Then 
by varying the node configuration (number or location), we can compare the accuarcy of the obtained mode shapes to the reference mode shapes 
in terms of modal assurance criteria (MAC) or Modal Scale Factor (MSF). The following figure represents the approach:

.. image:: /doc/figures/algorithm.png
   :width: 600
   :alt: Algorithm

A detailed description of how to use this package is given in the following sections

Installation
------------

Either download the repository to your computer and install, e.g. by **pip**

::

   pip install .


or install directly from github

::

   pip install git+https://github.com/tahsin-nishat/qos/tree/master/qos-pypackage/csi-beam/sysid


or install directly from the python package index

::

   pip install sysid


Usage
-----

1. Response Data Generation:
----------------------------
You can use this file for simulating the response (i.e. displacement, velocity or acceleration) at different nodes due to ambient noise 
(e.g. traffic load).

* Open "data-gen.py". Define the location (`pos`) and position of sensor nodes (`s`). Define the moment of inertia, modulus of elasticity, 
   mass density to generate response data .

* The current code generate the displacement as response data. You can also select to generate velocity or acceleration to be your response 
   data.

* After running the file you can create and save response data as `npz` format. It also saves the true natural frequencies, true damping ratios, 
   true mode shapes, sensor location which can be used for further analysis.

The code example below shows how generate response data from different sensor node configuration

.. code:: python

   import numpy as np
   import matplotlib.pyplot as plt
   import scipy.signal
   import sysid

   ''' ----- Create a sensor network for a beam with 10 sensors spaced symmetrically from each other--- '''
   # input for simulating beam geometry

   pos=np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])*12 # defining the  19 sensor locations and 2 support 
                                                               # locations of a 100 feet long simply supported bridge for reference mode shape
   s=np.array([0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1]) # Define the active sensor node 1 for active, 0 for sleep node
   Im=100 # Moment of inertia (in^4)
   E=6.58*1e6 # modulus of elasticity (psi)
   m_bar=0.1 # mass density per unit length (lb.sec^2/in/in)
   pos_n=pos*s
   pos_n=pos_n[np.nonzero(pos_n)]
   pos_n=np.r_[0,pos_n]
   n=len(pos_n)-2

   bm = sysid.utils.Beam(pos, Im, E, m_bar)

   # Determine the time discretization and period

   T=180.0
   fs=512.0
   t = np.arange(0., T, 1 / fs)

   # Define loads on system
   ## Unmeasureable: Stochastic loads on all nodes (Process noise/traffic load)
   
   w = np.random.normal(size=(n, t.size))*1e1

   ## Load matrix, f

   F = w.copy()

   # Simulate response, displacement at each node measured
   _, _, y0 = bm.simulate(t, F) # the 1st, 2nd and 3rd cols represent acceleration, velocity and displacement data respectively

   noise_std = y0.std()

   # Add measurement noise
   v = np.random.normal(size=y0.shape)* noise_std*15*1e-2 # 15% measurement noise
   y = y0 + v

   # To plot the simulated response (with and without noise) at different nodes (here last)
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

   for m in range(n):
      plt.axvline(sysid.utils.w2f(bm.get_natural_frequency(m+1)), alpha=.2) # Plot true natural frequencies which are obtained using material characteristics

   plt.ylabel('PSD')
   plt.xlabel('Frequency (Hz)')
   plt.show()

   bm.set_rayleigh_damping_matrix([bm.get_natural_frequency(1), bm.get_natural_frequency(n)], [.05]*2)

   true_frequencies = np.array([bm.get_natural_frequency(i)/(2*np.pi) for i in range(1, n+1)])
   true_damping = np.array([bm.get_rayleigh_damping_ratio(i) for i in range(1, n+1)])
   true_modeshapes = np.array([bm.get_mode_shape(i) for i in range(1, n+1)])

   np.savez('response-data',
            y=y_n, fs=fs,
            true_frequencies=true_frequencies,
            true_damping=true_damping,
            true_modeshapes=true_modeshapes,
            sensor_pos=pos_n
            )
   
   print("done")


The following figure shows the simulated response at node 1 and node 10

.. image:: /doc/figures/response.png
   :width: 600
   :alt: response


2. System Identification
-------------------------
You can use the package to identify natural frequencies, damping ratios and mode shapes from the generated data or practical response data.
Finally you can make a comparison between reference and estimated mode shapes and save the information for further analysis.

* generate the response data (both for reference and estimation)

* goto "sys-id". You can use the same file to whether you want to obtain the reference mode shape or make an estimation of mode shape for 
   different sensor node configuration other than reference configuration

* Define the model order, number of blocks to be used for covariance.

* In the stabilization diagram, pick the poles manually with the mouse click. It generates the mode shape diagram and gives you frequency 
   and damping information. The following figure shows an example of stabilization diagram and picked plot for 9 sensor nodes.

.. image:: /doc/figures/stabilization-diagram.png
   :width: 800
   :alt: stabilization-diagram

* While making a comparison between two mode shapes, you need to import both the refernce mode shape data and the data to be used for 
   comparison. The following figure shows an example of compared mode shapes up to 5 in between reference mode shapes with 19 sensor nodes and 
   estimated mode shapes with 9 sensor nodes.

.. image:: /doc/figures/comparison.png
   :width: 800
   :alt: Mode shape comparison

The code example below shows how the modes of a stochastic system can be obtained from measurements of the output `y`.


.. code:: python

   import matplotlib.pyplot as plt
   import numpy as np
   import sysid
   import scipy.signal

   '''
   # the following data is for the reference mode shape 
   data19 = np.load("refdata.npz")
   y19 = data19["y"]
   fs19 = data19["fs"]
   true_f19 = data19["true_frequencies"]
   true_xi19 = data19["true_damping"]
   true_modeshapes19 = data19["true_modeshapes"]
   sensor_pos19=data19["sensor_pos"] '''
 
   # The following data is for the estimated mode shape with sensor node configuration different from reference node configuration

   s=np.array([0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]) # Define the sensor location
   data = np.load("response-data.npz") 
   y = data["y"]
   fs = data["fs"]
   true_f = data["true_frequencies"]
   true_xi = data["true_damping"]
   true_modeshapes = data["true_modeshapes"]
   sensor_pos=data["sensor_pos"]

   ssid = sysid.CovarianceDrivenStochasticSID(y, fs)

   # Most often, we do not know the model order, and instead we overestimate
   # model order and pick the physical modes with the help of a stabilization
   # diagram. Strid also includes a stabilization diagram and functionality to
   # pick modes directly from the plot.
   # First, we must estimate modes for a range of different model orders

   modes = dict()
   for i, order in enumerate(range(30, 100, 2)): # Define and the model number tobe used in stabilization diagram (here from 30 to 100 with increment of 2)
      A, C, G, R0 = ssid.perform(order, 20) # Define the number of blocks to be used for covariance (here 20)
      modes[order] = sysid.Mode.find_modes_from_ss(A, C, fs)

   sd = sysid.StabilizationDiagram()
   sd.plot(modes)
   f, psd = ssid.psdy(nperseg=2**12)
   
   for i in range(2):
      freqs, Pyy = scipy.signal.csd(y[i],y[i], fs, nperseg=2 ** 12)
      sd.axes_psd.semilogy(freqs, Pyy,color=(0., 0., 0.+i, .5), lw=0.3)

   plt.show()

   modes = sd.picked_modes # If you do not pick any plot the modes returned would be []

   # You can only use the following part for comparison only if you have imported the reference data
   '''
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

   
   plt.show()
   np.savetxt('com-data.txt',res,delimiter=',') # saves the MAC and MSF data in .csv format '''

   print("done")



Credits:
--------
1. A significant contribution for this package comes from the following github project named strid_

  .. _strid: https://github.com/Gunnstein/strid
