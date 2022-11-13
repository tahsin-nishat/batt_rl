================================
Active Battery Health Management
================================


Project summary
----------------
The Internet of Things (IoT) has become one of the major future trends. Its proliferation has led to an explosive number of battery powered
wireless devices. Battery life has always been one of the biggest limiting factors of those wireless devices which poses different challenges
thourghout their operation.

This project deals with battery health management under battery group replacement requirement. In practice, there are many applications 
where IoT wireless devices (sensors in particular) are installed at hard-to-reach areas or remote locations, where the planning and logistics
of a maintennace trip can be very costly. To reduce the cost, battery group replacement is often required in these scenarios, i.e. replace all
batteries in a sensor network on a maintenance trip, instead of replacing just one or a few. Unfortunately, existing methods for battery
management exclusively aim to extend lifetime of individual batteries as much as possible, lacking a system level view. A consequence of 
applying such algorithms is that batteries in a sensor network tend to fail at very different times, posing significant difficulty on 
planning and scheduling of group replacement activities.

The research objective of this project is to develop an active battery health management framework such that batteries in a sensor network
will degrade more uniformly to achieve similar end-of-life times, which will significantly simplify the implementation of a group battery 
replacement policy. In addition, it will effectively extend lifetime of batteries as a group, as it reduces early failures of the battery
individuals that cripples the sensor network and triggers a group replacement request. The controlled battery health degradation processes 
are made possible by dynamically adjusting the quality of service levels assigned to wireless nodes, based on the predicted battery remaining
useful lifetime as a measure of battery health. The success of this project will significantly reduce the overall battery maintenance cost.


Quality of Service Metrics for Structural Health Monitoring
-----------------------------------------------------------
As a part of the project, this study focuses on battery health management through structural health monitoring (SHM) applications, which 
heavily relies on battery-powered wireless sensor network (WSN) and often deployed at hard-to-reach places. Hence, it is an ideal IoT 
application field which can be significantly benefited if the project is successful.

WSN based structural health monitoring has gained the attention of researchers due to its economic feasibility and easy installation process. 
Considering common civil applications and to reserve energy, a duty cycle strategy is often adopted in the wireless sensors. This means a 
subset of sensor nodes in a network remains active to detect the events of interest while the other nodes are either idle or in sleep mode. 
Depending on the status (active, idle, or sleep), the battery degradation rate at each node varies. Even if all the sensors work under 
similar operational conditions, degradation of the battery level is not uniform due to variability in battery charging rate, uncertainties 
due to weather, sensor locations, etc. Once the power level of a battery reaches its threshold efficiency, it needs to be replaced. To 
reduce the labor cost, group replacement of batteries is preferred. However, variability in battery lifetime creates significant difficulty 
for group replacement decision making. Existing literature in battery management only focus on individual battery lifetime instead of 
system level which only increase battery life variability. The current study deals with system level battery management. 


For mission critical civil structures, being able to detect the event of ineterest (e.g. extreme load, damage or crack growth) is very 
crucial. Hence, maintaining the desired performance level of the WSN during its operation is mandatory. The performance of a WSN is 
quantified by user-specific "Quality of Service (QoS)" metrics. A practical WSN deployed in the field is almost always built with 
redundancy. It is achieved either through hardware or algorithms or both. Therefore, the minimal QoS can be maintained through different 
node configuration. In this study, a mode shape-based quality index is proposed for the demonstration.

In summary, this study aims to develop a framework for active battery health management for a real-life wireless sensor network while 
maintaining the required quality of service (QoS) metrics at the system level.

1. Active Control of Battery Degradation at the WSN system level:
-----------------------------------------------------------------
At first, an attempt is taken to develop a framework for WSNs to maintain uniform battery degradation at all sensor nodes while maximizing 
the number of active nodes. A reinforcement learning (RL) based simualated environment is devleoped to represent a realistic sensor node 
configuration of Jindo Bridge (i.e. a cable stayed bridge in Korea). Figure 1 shows the 112 senosr node configuration.

Following uncertainties are considered to simuate the realistic environment:

a. The sensors are rechargeable with solar power. Solar energy varies at different days of the year depending on the weather. To include 
the solar power variability, using System Advisor Model (SAM) solar profile data is generated for 2013 to 2019. These data are used during 
training and testing of the model.

b. Solar harvesting uncertainties due to spatial variation is considered. Figure 2 represents the solar harvesting uncertainties at 
different sensor node configuration.

c. Uncertaining in wireless communication is included in the model.

Finally the The RL agent was trained under the developed RL environment to learn optimal nodes and duty cycles, meanwhile managing battery 
health at the network level. The agent is trained for 30 days period (with 3 hr interval data 240 steps in an episode) and tested on 360 
days data. During training, uniform battery degradation and maximization of the active duty cycle receive positive rewards. To this end, 
the training and test results show the prominence of this algorithm in achieving effective battery health management of the WSN for SHM.

.. image:: /doc/figure/jindo-bridge.png
    :width: 400
    :alt: Jindo Bridge sensor node configuration

2. Intorducing Quality of Service metrics at the WSN system level (Ongoing):
----------------------------------------------------------------------------
In this ongoing part of the study, mode shape is introduced as a quality index to ensure desired the QoS for the network. In other words,
the accuracy of the estimated mode shape would represent the performance of the network.

Modal analysis is required to define the QoS index at each node level to achieve the desired the QoS at the system level. A 100 feet long 
simply supported bridge is considered for the modal analysis. For different sensor node configuration, estimated mode shape accuarcy will 
vary. Depending on how much accuracy is required, a reference mode shape needs to be selected. Initially, 5 feet evenly spaced 19 sensor 
nodes are considered as reference sensor node configuration and the obtained mode shape will be the reference mode shape. We want to focus 
on obtaining up to mode number 5 and for the selected configuration these mode shapes can be detected with good accuracy.

Output-based system identification is considered for the modal analysis. There are different output-based modal analysis methods available 
e.g. Covariance driven stochastic system identification, Data driven system identification method etc. For this analysis, only covariance 
driven stochastic system identification i.e. obtaining mode shapes from ambient vibration due to traffic load is considered. The reason is,
if we want to use the developed framework for real-life response data, we can do that.

A python package is developed to automate the modal analysis of a simply supported bridge for different sensor-node configuration. A 
detailed description of how to use the python package for data generation and modal analysis is given in the "qos\qos-pypackage\csi-beam\readme"


Funding Agency:
---------------
The project is funded by the National Science Foundation (NSF).

Credits
-------

1. This project package was created from the template of Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_.

    .. _Cookiecutter: https://github.com/audreyr/cookiecutter
    .. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

2. To create python package for modal analysis of beam, the algorithm of strid_ (basically developed for shear frame) is followed:
     
     .. _strid: https://github.com/Gunnstein/strid