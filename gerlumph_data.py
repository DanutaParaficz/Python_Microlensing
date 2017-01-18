
#=======================================================================================
# Light curves
#=======================================================================================
#=======================================================================================

import numpy as np
res = 10000
f   = open("../lcurves_HE0435_C_new/map_1/prof_1/lc_data.bin","rb")
light1 = np.fromfile(f)
light1.mean()
f   = open("../lcurves_HE0435_C_new/map_2/prof_1/lc_data.bin","rb")
light2 = np.fromfile(f)
light2.mean()
f   = open("../lcurves_HE0435_C_new/map_3/prof_1/lc_data.bin","rb")
light3 = np.fromfile(f)
light3.mean()
f   = open("../lcurves_HE0435_C_new/map_4/prof_1/lc_data.bin","rb")
light4 = np.fromfile(f)
light4.mean()
f   = open("../lcurves_HE0435_C_new/map_5/prof_1/lc_data.bin","rb")
light5 = np.fromfile(f)
light5.mean()
f   = open("../lcurves_HE0435_C_new/map_6/prof_1/lc_data.bin","rb")
light6 = np.fromfile(f)
light6.mean()
f   = open("../lcurves_HE0435_C_new/map_7/prof_1/lc_data.bin","rb")
light7 = np.fromfile(f)
light7.mean()
f   = open("../lcurves_HE0435_C_new/map_8/prof_1/lc_data.bin","rb")
light8 = np.fromfile(f)
light8.mean()
f   = open("../lcurves_HE0435_C_new/map_9/prof_1/lc_data.bin","rb")
light9 = np.fromfile(f)
light9.mean()
f   = open("../lcurves_HE0435_C_new/map_10/prof_1/lc_data.bin","rb")
light10 = np.fromfile(f)
light10.mean()
f   = open("../lcurves_HE0435_C_new/map_11/prof_1/lc_data.bin","rb")
light11 = np.fromfile(f)
light11.mean()

import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
plt.hist(light1,bins=50,range=[-2,1])
ax.set_yscale('log')
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/histogram_1'
plt.savefig(fname2)
fig, ax = plt.subplots()
plt.hist(light2,bins=50,range=[-10,10])
ax.set_yscale('log')
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/histogram_2'
plt.savefig(fname2)
fig, ax = plt.subplots()
plt.hist(light3,bins=50,range=[-10,10])
ax.set_yscale('log')
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/histogram_3'
plt.savefig(fname2)
fig, ax = plt.subplots()
plt.hist(light5,bins=50,range=[-10,10])
ax.set_yscale('log')
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/histogram_5'
plt.savefig(fname2)
fig, ax = plt.subplots()
plt.hist(light6,bins=50,range=[-10,10])
ax.set_yscale('log')
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/histogram_6'
plt.savefig(fname2)
fig, ax = plt.subplots()
plt.hist(light7,bins=50,range=[-10,10])
ax.set_yscale('log')
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/histogram_7'
plt.savefig(fname2)
fig, ax = plt.subplots()
plt.hist(light8,bins=50,range=[-10,10])
ax.set_yscale('log')
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/histogram_8'
plt.savefig(fname2)
fig, ax = plt.subplots()
plt.hist(light9,bins=50,range=[-10,10])
ax.set_yscale('log')
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/histogram_9'
plt.savefig(fname2)
fig, ax = plt.subplots()
plt.hist(light10,bins=50,range=[-10,10])
ax.set_yscale('log')
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/histogram_10'
plt.savefig(fname2)

time=np.arange(60)
import matplotlib.pyplot as plt
plt.plot(time , light[0:60])
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/light_test.pdf'
plt.savefig(fname2)




#=======================================================================================
#=======================================================================================
#=======================================================================================
#=======================================================================================
#=======================================================================================
#MAPS
#=======================================================================================
#=======================================================================================

import astropy.io.fits as fits
import numpy as np
f   = open("mapmag5.bin","rb")
mapa = np.fromfile(f,'i',-1,"")
#hdu = fits.PrimaryHDU(map)
#fits.HDUList([hdu]).writeto('test.fits')

#=======================================================================================
#Convert map to magnification
#=======================================================================================
fline=open("map_1/mapmeta.dat").readline().rstrip()
words = fline.split(" ") 
av_mag=float(words[0])
av_num=float(words[1])
map_flux=map*(av_mag/av_num)
map_magg=-2.5*np.log10(map_flux/av_mag)
map_mag=np.reshape(map_magg,(10000,10000))

fig, ax = plt.subplots()
plt.hist(map_magg,bins=50,range=[-2,1])
ax.set_yscale('log')
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/histogram_1_map'
plt.savefig(fname2)
#=======================================================================================
#Generate full light curves
#=======================================================================================
# from one end to the other
import scipy.ndimage
num = 9999
x0=0.
y0=0.
zi_884=[]
for i in range(9999):
    y1=i
    x1=9999.
    x, y = np.linspace(x0, x1, num), np.linspace(y0, y1, num)
  #  zi.append(scipy.ndimage.map_coordinates(map_mag, np.vstack((x,y))))
    zi_full.append(map_mag[x.astype(np.int), y.astype(np.int)])
    print i

#=======================================================================================
#Resample simulated light curves
#=======================================================================================
diff=[]
for i in range(883):
    diff.append(source_list[i+1,0]- source_list[i,0])

max(diff)

#=======================================================================================
#extract light curves
#=======================================================================================
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt

i = scipy.ndimage.map_coordinates(map, np.vstack((x,y)))
fig, axes = plt.subplots(nrows=1)
axes[0].imshow(map_mag)
axes[0].plot([x0, x1], [y0, y1], 'ro-')
axes[0].axis('image')

axes[1].plot(zi_884[50], 'ro')
axes[2].plot(zi_400[50], 'ro')
plt.show()
#=======================================================================================
