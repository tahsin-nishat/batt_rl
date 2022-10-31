# Import the response data from different node configuration
data = np.load("node9data.npz")
y = data["y"]
fs = data["fs"]
true_f = data["true_frequencies"]
true_xi = data["true_damping"]
true_modeshapes = data["true_modeshapes"]


ssid = sysid.CovarianceDrivenStochasticSID(y, fs)

# Testing Covariance driven stochastic system ID

