using DelimitedFiles, FLoops, AdaptiveMCMC


function maxlikerotation2_floop(param::Array{Float64}, data::Matrix{Float64})
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


foro = readdlm("photondata.txt")

out4 = adaptive_rwm([ 6.14394854e-02, -9.78690448e-02+180,  3.56972834e-02,  4.51436712e+01,
       -2.37867433e-01+1], x->maxlikerotation2_floop(x, foro), 2_000_000; algorithm=:am)

allout=out4.X

open("minimum2M.txt", "w") do io
           writedlm(io, allout)
end
