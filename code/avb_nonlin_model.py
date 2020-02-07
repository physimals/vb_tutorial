"""
Simple implementation of analytic Variational Bayes to infer a 
nonlinear forward model

This implements section 4 of the FMRIB Variational Bayes tutorial 1.
"""
import numpy as np

# This starts the random number generator off with the same seed value
# each time, so the results are repeatable. However it is worth changing
# the seed (or simply removing this line) to see how different data samples
# affect the results
#np.random.seed(0)

# Ground truth parameters
A_TRUTH = 10
LAMBDA_TRUTH = 1.0
NOISE_PREC_TRUTH = 100
NOISE_VAR_TRUTH = 1/NOISE_PREC_TRUTH
NOISE_STD_TRUTH = np.sqrt(NOISE_VAR_TRUTH)

# Observed data samples are generated by Numpy from the ground truth
# Gaussian distribution. Reducing the number of samples should make
# the inference less 'confident' - i.e. the output variances for
# MU and BETA will increase
N = 100
t = np.linspace(0, 5, 50)
DATA_CLEAN = A_TRUTH * np.exp(-LAMBDA_TRUTH * t)
DATA_NOISY = DATA_CLEAN + np.random.normal(0, NOISE_STD_TRUTH, [50])
print("Data samples are:")
print(t)
print(DATA_CLEAN)
print(DATA_NOISY)

import sys
sys.exit(1)
# Priors - noninformative because of high variance
#
# Note that the noise posterior is a gamma distribution
# with shape and scale parameters c, b. The mean here is
# b*c and the variance is c * b^2. To make this more 
# intuitive we define a prior mean and variance for the 
# noise parameter BETA and express the prior scale
# and shape parameters in terms of these
#
# So long as the priors stay noninformative they should not 
# have a big impact on the inferred values - this is the 
# point of noninformative priors. However if you start to
# reduce the prior variances the inferred values will be
# drawn towards the prior values and away from the values
# suggested by the data
m0 = 0
v0 = 1000
beta_mean0 = 1
beta_var0 = 1000
b0 = beta_var0 / beta_mean0
c0 = beta_mean0**2 / beta_var0

def update(means, cov, s, c):
    cov = s*c*np.dot(J.t(), J) + C0
    means = np.linalg.inv(cov) * s * c * J.t() * (k + J * means) + C0 * means0
    c = N/2 + c0
    s = 1/(1/s0 + 1/2 * np.dot(k.t(), k) + 1/2 * np.trace(np.linalg.inv(cov) * J.t() * J))

# Initial values for the posterior hyperparameters.
#
# If the iterative process is working correctly this should
# not affect the outcome. However in more complex models
# the starting point is more important and if badly chosen could
# lead the the iteration reaching a local minimum rather than
# the best solution
m = 0
v = 10
beta_mean1 = 1.0
beta_var1 = 10
b = beta_var1 / beta_mean1
c = beta_mean1**2 / beta_var1
print("Iteration 0: (m, v, b, c) = (%f, %f, %f, %f)" % (m, v, b, c))

# VB iterative update

# Equation 3.15 - these depend only on the data
S1 = np.sum(DATA)
S2 = np.sum(np.square(DATA))

for vb_iter in range(10):

    # Equation 3.17
    m = (m0 + v0 * b * c * S1) / (1 + N * v0 * b * c)

    # Equation 3.18
    v = v0 / (1 + N * v0 * b * c)

    # Equation 3.20
    X = S2 - 2*S1*m + N * (m**2 + v)

    # Equation 3.21
    b = 1 / (1 / b0 + X / 2)
    
    # Equation 3.22
    c = N / 2 + c0

    print("Iteration %i: (m, v, b, c) = (%f, %f, %f, %f)" % (vb_iter+1, m, v, b, c))

print("Inferred mean/precision of Gaussian: %f, %f" % (m, c * b))
print("Inferred variance on Gaussian mean/precision: %f, %f" % (v, c * b**2))