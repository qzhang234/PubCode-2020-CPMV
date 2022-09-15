
import numpy as np
import h5py   
from scipy.optimize import curve_fit 


def G2_g2(G2,IP,IF,qmap_sta,qmap_dyn):

    ql_sta_dim = np.amax(qmap_sta)
    ql_dyn_dim = np.amax(qmap_dyn)

    G2q=np.zeros([G2.shape[0],ql_sta_dim])
    IPq=np.zeros([G2.shape[0],ql_sta_dim])
    IFq=np.zeros([G2.shape[0],ql_sta_dim])

    g2=np.zeros([G2.shape[0],ql_dyn_dim])
    g2_err=np.zeros([G2.shape[0],ql_dyn_dim])

    G2 = np.where(G2>=2e-8, 0, G2)
    
    IP_IF = np.multiply(IP,IF)
    IP_IF = np.where(IP_IF == 0, 1e4, IP_IF)
    g2_per_pixel = np.divide(G2,IP_IF)
    g2_per_pixel = np.where(g2_per_pixel > 10, 1, g2_per_pixel)

    for ii in range(ql_sta_dim):
        idx = (qmap_sta == ii+1)
        _ = G2[:,idx.flatten()]
        G2q[:,ii] = np.nanmean(_,axis=1)
        _ = IP[:,idx.flatten()]
        IPq[:,ii] = np.nanmean(_,axis=1)
        _ = IF[:,idx.flatten()]
        IFq[:,ii] = np.nanmean(_,axis=1)

    Isymmq = np.multiply(IPq,IFq)

    for ii in range(ql_dyn_dim):
        idx = (qmap_dyn == ii+1)
        _ = g2_per_pixel[:,idx.flatten()]
        g2_err[:,ii] = np.nanstd(_,axis=1)/np.sqrt(_.shape[1])

    for ii in range(ql_dyn_dim):
        _ = qmap_sta[np.where(qmap_dyn==ii+1)]
        tmpG2q = G2q[:,(np.amin(_)-1):(np.amax(_)-1)]
        tmpIsymmq= Isymmq[:,(np.amin(_)-1):(np.amax(_)-1)]
        g2[:,ii] = np.nanmean(np.divide(tmpG2q,tmpIsymmq),axis=1)

    return g2, g2_err

