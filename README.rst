================================
Active Battery Health Management
================================


Project summary:
------------------
The Internet of Things (IoT) has become one of the major future trends. Its proliferation has led to an explosive number of battery powered
wireless devices. Battery life has always been one of the biggest limiting factors of those wireless devices.

This project deals with battery health management under battery group replacement requirement. In practice, there are many applications 
where IoT wireless devices (sensors in particular) are installed at hard-to-reach areas or remote locations, where the planning and logistics
of a maintennace trip can be very costly. To reduce the cost, battery group replacement is often required in these scenarios, e.g. replace all
batteries in a sensor network on a maintenance trip, instead of repllacing just one or a few. Unfortunately, existing methods for battery
management exclusively aim to extend lifetime of individual batteries as much as possible, lacking a system level view. A consequence of 
applying such algorithms is that batteries in a sensor network tend to fail at veru different times, posing significant difficulty on 
planning and scheduling of group replacement activities.

The research objective of this project is to develop an active battery health management framework such that batteries in a sensor network
will degrade more uniformly to achieve similar end-of-life times, which will significantly simplify the implementation of a group battery 
replacement policy. In addition, it will effectively extend lifetime of batteries as a group, as it reduces early failures of the battery
individuals that cripples the sensor network and triggers a group replacement request. The controlled battery health degradation processes 
are made possible by dynamically adjusting the quality of service levels assigned to wireless nodes, based on the predicted battery remaining
useful lifetime as a measure of battery health. The success of this project will significantly reduce the overall battery maintenance cost.


Developing Quality of Service Metrics for Structural Health Monitoring (SHM):
-----------------------------------------------------------------------------
Wireless sensor network (WSN) based structural health monitoring has gained the attention of researchers due to its economic feasibility 
and ease in the installation process.Considering common civil applications and reserve energy, a duty cycle strategy is adopted in the
battery-powered wireless sensors. This means a subset of sensor nodes in a network remains active to detect the events of interest while 
the other nodes are either idle or in sleep mode. Depending on the status (active, idle, or sleep), the battery degradation rate at each 
node varies. Even if all the sensors work under similar operational conditions, degradation of the battery level is not uniform because 
of many factors (e.g. battery charging rate, uncertainties due to communication, uncertainties due to weather, sensor locations, etc.). 
Once the power level of a battery reaches its threshold efficiency, it needs to be replaced. However, the replacement of each battery can 
impose huge labor costs because of some hard-to-reach places. Cost can include traveling, scheduling, and logistics of equipment and 
personnel. In this case, group replacement of batteries is preferred, although some batteries can not utilize their full capacity. 
Therefore, effective battery health management is imperative to make group replacement of batteries possible and consequently reduce labor
costs without sacrificing the efficacy of obtained data. 

This study focuses on developing a framework for WSNs to maintain uniform battery degradation at all sensor nodes and to maximize the 
number of active nodes while ensuring a desired quality of service. A realistic sensor node configuration is considered in this study 
where each of the batteries is rechargeable with solar power. Charging rate variability due to weather conditions and spatial variation, 
uncertainties in communication between the nodes, and duty cycles are considered in the framework. Reinforcement Learning based algorithm 
is implemented to develop a model where uniform battery degradation and maximization of the active duty cycle receive positive rewards. The
training and test results show the prominence of this algorithm in achieving effective battery health management systems. Finally, a 
quality index is introduced which can ensure a desired quality of service (QoS) for the network. As an evaluation criterion to estimate 
the accuracy of the health status of the structure, the modal shape parameter is considered. Orthogonality check at each node and for the 
entire network is carried out in terms of modal shape. Then a threshold QoS index is defined which needs to be guaranteed during the sensor
network operation. The prospect of the developed framework is that it can become economically feasible by achieving similar end-of-life 
times for all the batteries, reducing labor costs for replacement without sacrificing the performance of the network. The framework, 
although developed based on structural health monitoring applications, can be implemented in varieties of wireless IoT applications.

Active Control of Battery Degradation at the WSN system level:
--------------------------------------------------------------
To this end, a reinforcement learning (RL) based framework for active control of the battery degradation at the WSN system level is 
propsed in this study with the aim of the battery group replacement. A comprehensive simulation environment was developed in a real-life 
WSN setup, i.e. WSN for a cable-stayed bridge SHM, considering various practical uncertainties. The RL agent was trained under a developed 
RL environment to learn optimal nodes and duty cycles, meanwhile managing battery health at the network level. The training and test 
results showed the prominence of the proposed framework in achieving effective battery health management of the WSN for SHM.

Ongoing: Intorducing Quality of Service metrics:
------------------------------------------------
The performance of a wireless smart sensor network (WSSN) is quantified by user-specific "Quality of Service (QoS)" metrics. 
A practical WSN deployed in the field is almost always built with redundancy. It is achieved either through hardware or algorithms or both. 
Therefore, the minimal QoS can be maintained through different QoS node configuration.In this study, a mode shape-based quality index is 
proposed for the demonstration. 

The main objective is to develop a framework for ensuring a desired QoS based on the system identification quality from a real-life sensor network.
Initially, the accuracy of the estimated mode shape is considered as a quality index. Modal analysis is required to define the quality of 
mode shapeobtained from different sensor node configuration. Then metrices can be introduced to ensure minimal quality throughout the 
network operation.

Ongoing: Modal Analysis on different sensor-node configuration:
---------------------------------------------------------------
For real-life sensor node configurations, a simply supported bridge is considered. Output-based system identification is considered for 
modal analysis. There are different output-based modal analysis methods available e.g. Covariance driven stochastic system identification,
Data driven system identification method etc. For this analysis only Covariance driven stochastic system identification i.e. obtaining 
mode shapes from ambient vibration due to traffic load is considered.

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