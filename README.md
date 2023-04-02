# IXPE-Analysis

Some analysis notebooks for IXPE data using the maximum likelihood techique outlined in https://arxiv.org/abs/2204.00140.

IXPE Reduction:

* [Reduce-CenX3.ipynb](Reduce-CenX3.ipynb) : reduce the data for Cen X-3 including source barycentring, period finding and folding
* [Reduce-Generic-IXPE.ipynb](Reduce-Generic-IXPE.ipynb) : reduce the data for a generic IXPE pulsar observation including solar system and source barycentring, period from GBM and folding.  This example is Her X-1 during the main-on.

Julia MCMC:

* [MCMC-Julia.jl](MCMC-Julia.jl) : Julia script to perform MCMC estimation of confidence regions on RVM parameters (uses photondata.txt produced by the reduce notebooks): photondata contains phase, 2cos(2*PA)*modf,  2*sin(2*PA)*modf for each photon (IXPE convention)
* [PBS-Julia-Script](PBS-Julia-Script) : Run the Julia script on a PBS server with 32 CPUs

Precession:

* [Precession-HerX1-Final.ipynb](Precession-HerX1-Final.ipynb) : Python notebook to derive formulae for a precessing triaxial body and applying them to the polarization angle measurements of Her X-1

