# IXPE-Analysis

Some analysis notebooks for IXPE data using the maximum likelihood techique outlined in https://arxiv.org/abs/2204.00140, and producing and using models with the Magnetar python package.

* [Reduce-4U.ipynb](Reduce-4U.ipynb)    : reduce the data for 4U 0142+61 including energy correction, period finding and folding
* [Reduce-CenX3.ipynb](Reduce-CenX3.ipynb) : reduce the data for Cen X-3 including source barycentring, period finding and folding
* [MCMC-Julia.jl](MCMC-Julia.jl) : Julia script to perform MCMC estimation of confidence regions on RVM parameters (uses photondata.txt produced by the reduce notebooks): photondata contains phase, 2*cos(2*PA)*modf, 2*sin(2*PA)*modf for each photon (IXPE convention)
* [MaxLike_RVM_uniform.jl](MaxLike_RVM_uniform.jl) : Julia script as above but with uniform prior on PD and photondata contains phase, cos(2*PA)*modf, sin(2*PA)*modf for each photon (PolarLight convention)
* [MCMC-Julia-RVM_v2.jl](MCMC-Julia-RVM_v2.jl) : Julia script that saves every 1,000 samples and continues the MCMC
* [corner-plots-CenX3.ipynb](corner-plots-CenX3.ipynb) : Produce corner plots from the Julia MCMC code
