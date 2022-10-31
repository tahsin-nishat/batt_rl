=======
QoS_NSF
=======


* Overview:
The performance of a wireless smart sensor network (WSSN) is quantified by user-specific "Quality of Service (QoS)" metrics. 
A practical WSN deployed in the field is almost always built with redundancy. It is achieved either through hardware or algorithms or both. 
Therefore, the minimal QoS can be maintained through different QoS node configuration.

* The main objective of this ongoing project is to develop a framework for ensuring a desired QoS based on the system identification quality from a real-life sensor network.
Initially, the accuracy of the estimated mode shape is considered as a quality index. Modal analysis is required to define the quality of mode shape
obtained from different sensor node configuration. Then metrices can be introduced to ensure minimal quality throughout the network operation.

* Modal Analysis:
For real-life sensor node configurations, a simply supported bridge is considered. Output-based system identification is considered for modal analysis.
There are different output-based modal analysis methods available e.g. Covariance driven stochastic system identification, Data driven system identification method etc.
For this analysis only Covariance driven stochastic system identification i.e. obtaining mode shapes from ambient vibration due to traffic load is considered.



Features
--------

* TODO

Credits
-------

1. This project package was created from the template of Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_.

    .. _Cookiecutter: https://github.com/audreyr/cookiecutter
    .. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

2. To create python package for modal analysis of beam, the algorithm of strid_ (basically developed for shear frame) is followed:
     
     .. _strid: https://github.com/Gunnstein/strid