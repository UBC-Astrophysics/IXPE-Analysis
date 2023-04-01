# IXPE-Analysis

Some analysis notebooks for IXPE data using the maximum likelihood techique outlined in https://arxiv.org/abs/2204.00140.

* [Reduce-CenX3.ipynb](Reduce-CenX3.ipynb) : reduce the data for Cen X-3 including source barycentring, period finding and folding
* [MCMC-Julia.jl](MCMC-Julia.jl) : Julia script to perform MCMC estimation of confidence regions on RVM parameters (uses photondata.txt produced by the reduce notebooks): photondata contains phase, 2*cos(2*PA)*modf, 2*sin(2*PA)*modf for each photon (IXPE convention)
* [Precession-HerX1-Final.ipynb](Precession-HerX1-Final.ipynb) : Python notebook to derive formula for a precessing triaxial body and applying them to the polarization angle measurements of Her X-1
