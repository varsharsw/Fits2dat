import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from matplotlib.cbook import flatten
import glob   
import os

def fitstodat(fitsfile):
  sp=fits.open(fitsfile)
  bintable=sp[1]
  x=bintable.columns['WAVELENGTH']
  y=bintable.columns['FLUX']
  
  x.name
  x.unit
  xfactor=1
  if x.unit=='nm' :
      xfactor=10.0
  y.name
  y.unit
  yfactor=0
  if (y.unit.split(' ')[0].split('^')[0]=='10') :
    yfactor=float(y.unit.split(' ')[0].split('^')[1])
  yfactor=10**yfactor
  
  W=bintable.data[x.name].T *xfactor
  F=bintable.data[y.name].T *yfactor

  filename=fitsfile.split('.')[0]
  concated= np.c_[np.hstack((W[2:-3,])),np.hstack((F[2:-3,]))]
  sorted_array = concated[concated[:,0].argsort()]
  np.savetxt(filename+'.dat', sorted_array)
    
    
    
#filelist = [f for f in glob.glob("*.fits")]
#l=len(filelist)

#for i in range(0,l):
#    fitstodat(filelist[i])
    
fitsfile=input("enter fits file")
fitstodat(fitsfile)