# you might need to install these
#import Pkg 
#Pkg.add("AdaptiveMCMC")
#Pkg.add("FLoops")
#Pkg.instantiate()

#
# N.B. This script does not save the samples as it proceeds, so be sure to ask for enough time to complete the MCMC chain
#
# The likelihood calculation itself is parallelized, so it runs a single long chain of 2,000,000 samples.  Usually it is sufficient 
# to drop the first 100,000 for burn in and skip each 100.
#
# For example, if one did 32 parallel chains and dropped the first 100,000, one would have to do 3,200,000 samples before getting anything useful
# and another 1,900,000 samples to get the same number as the parallel likelihood calculation, for a total of 5,100,000 samples.
#
#

using DelimitedFiles, FLoops, AdaptiveMCMC


function MaxLike_RVM_uniform(param::Array{Float64}, data::Matrix{Float64})
    if param[1]<0 || param[1]>1 || param[2]<0 || param[2]>180 || param[3]>90 || param[3]<0 || param[4]<-90 || param[4]>90 || param[5]<0 || param[5]>1        
        return -Inf
    end
    l=size(data)[2]
    radang=param[4]/180*pi
    polfrac=param[1]
    halfamb=(param[2]-param[3])/2/180*pi
    halfapb=(param[2]+param[3])/2/180*pi
    shalfamb=sin(halfamb)
    chalfamb=cos(halfamb)
    shalfapb=sin(halfapb)
    chalfapb=cos(halfapb)
    @floop for i in 1:l
        @inbounds tanhalfC=tan((data[1,i]-param[5])*pi)
        halfAmB=atan(shalfamb,shalfapb*tanhalfC)
        halfApB=atan(chalfamb,chalfapb*tanhalfC)
        twoang=2*((halfApB-halfAmB)+radang)
        qloc=cos(twoang)
        uloc=sin(twoang)
        # 0.5 follows the IXPE convention 
        @inbounds @reduce ( c+=log(1+0.5*polfrac*(qloc*data[2,i]+uloc*data[3,i])) )
    end 
    return c
end

#
#
# the file below is created by the data reduction scripts
# it contains the phase, evtlist['Q']*modf, evtlist['U']*modf if a text file of three rows and nphoton columns.
#
#

foro = readdlm("photondata.txt")
p0= [0.2, 5, 5, 45, 0.5]
niter=2_000_000

print("Files loaded. Beginning MCMC\n")

out4 = adaptive_rwm(p0, 
                    x->MaxLike_RVM_uniform(x,foro)+
		    log(abs(sin(x[2]/180*pi)))+log(abs(sin(x[3]/180*pi))),
                    niter; b=0, algorithm=:am)

allout=out4.X

open("minimum2M.txt", "w") do io
           writedlm(io, allout)
end
