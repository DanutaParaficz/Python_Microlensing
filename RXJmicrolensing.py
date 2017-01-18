import astropy.time
import dateutil.parser
import numpy as np
from uncertainties import ufloat
import matplotlib.patches as mpatches
import datetime
from jdcal import jd2gcal  
from jdcal import MJD_0, MJD_JD2000


source_list=np.loadtxt(open("/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/RXJ1131_datapoints.txt","rb"))
source_list_AD=np.loadtxt(open("/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/RXJ1131_A-Dtimeshifted.rdb","rb"))
source_list_BD=np.loadtxt(open("/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/RXJ1131_B-Dtimeshifted.rdb","rb"))

magA=source_list[:,1]+0.7
magB=source_list[:,3]
magC=source_list[:,5]
magD=source_list[:,7]
magDmagA=source_list_AD[:,1]
magDmagB=source_list_BD[:,1]
num_days=source_list[source_list[:,1].size-1,0]-source_list[0,0]

years=[str(jd2gcal(MJD_0,52500)[0]),str(jd2gcal(MJD_0,53500)[0]),str(jd2gcal(MJD_0,54500)[0]),str(jd2gcal(MJD_0,55500)[0]),str(jd2gcal(MJD_0,56500)[0]),str(jd2gcal(MJD_0,57500)[0])]
import matplotlib
matplotlib.rc('xtick', labelsize=12)
matplotlib.rc('ytick', labelsize=12)
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,9), dpi=100)
ax1 = fig.add_subplot(212)
ax1.scatter(np.array(source_list[:,0]), np.array(magA)+2.,edgecolor='None',c='r',s=3, label="A")
ax1.scatter(np.array(source_list[:,0]), np.array(magB),edgecolor='None', c='b',s=3, label="B - 8 days")
ax1.scatter(np.array(source_list[:,0]),  np.array(magC)-0.8,edgecolor='None', c='g',s=3, label="C")
ax1.scatter(np.array(source_list[:,0])-92., np.array(magD)+0.5,edgecolor='None', c='m',s=3, label="D - 15 days")

#plt.legend(loc=2,fontsize=12,markerscale=1)
ax2 = ax1.twiny()
#ax2.set_xlabel("Years",  fontsize=12)
ax1.set_xlabel("JD-2400000 [days]",  fontsize=12)
ax1.set_ylabel("Relative magnitude",  fontsize=12)
ax1.set_xlim(52500,57700)
ax1.set_ylim(-8.5,-13.3)
new_tick_locations = np.array([52500, 53500, 54500,55500,56500,57500])
ax2.set_xlim(ax1.get_xlim())
ax2.set_xticks(new_tick_locations)
ax2.set_xticklabels(years)
plt.text(52980,-9.99, 'D - 92 days',horizontalalignment='center',fontsize=12, color='magenta')
plt.text(52890,-12.4, 'C',horizontalalignment='center',fontsize=12, color='green')
plt.text(52890,-13.0, 'B',horizontalalignment='center',fontsize=12, color='blue')
plt.text(52890,-11.05, 'A',horizontalalignment='center',fontsize=12, color='red')
plt.text(55000,-14.2, 'Lightcurves of RXJ1131-1231 quasar images ',horizontalalignment='center',fontsize=17)
plt.text(55000,-13.8, '(intrisic viariability of quasar + microlensing singal)',horizontalalignment='center',fontsize=17)
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/All_RXJ.pdf'
plt.savefig(fname2)


import matplotlib 
matplotlib.rc('xtick', labelsize=90) 
matplotlib.rc('ytick', labelsize=90) 
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(100,50))
ax1 = fig.add_subplot(111)
ax1.plot(np.array(source_list[:,0]), np.array(magC), 'rs',markersize=20, label="C")
ax1.plot(np.array(source_list[:,0]), np.array(magB), 'bs',markersize=20, label="B")
ax1.plot(np.array(source_list[:,0]), np.array(magB-magC)-10., 'gs',markersize=20, label="B-C")
plt.legend(loc=2,fontsize=99,markerscale=2)
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/FBFC_RXJ.pdf'
plt.savefig(fname2)





import matplotlib 
matplotlib.rc('xtick', labelsize=90) 
matplotlib.rc('ytick', labelsize=90) 
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(100,50))
ax1 = fig.add_subplot(111)
ax1.plot(np.array(source_list[:,0]), np.array(magA), 'rs',markersize=20, label="A")
ax1.plot(np.array(source_list[:,0])-92., np.array(magD)-2., 'bs',markersize=20, label="C")
ax1.plot(np.array(source_list_AD[:,0]), np.array(magDmagA)-9., 'gs',markersize=20, label="A-D")
plt.legend(loc=2,fontsize=99,markerscale=2)
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/FAFD_RXJ.pdf'
plt.savefig(fname2)



import matplotlib 
matplotlib.rc('xtick', labelsize=12)
matplotlib.rc('ytick', labelsize=12)
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,9), dpi=100)
ax1 = fig.add_subplot(212)

ax1.scatter(np.array(source_list[:,0]), np.array(magB-magA), edgecolor='None',c='r',s=3, label="B-A")
ax1.scatter(np.array(source_list[:,0]), np.array(magB-magC),edgecolor='None',c='g',s=3, label="B-C")
ax1.scatter(np.array(source_list_BD[:,0])+92, np.array(magDmagB)+1.,edgecolor='None',c='m',s=3, label="B-D")
ax1.set_xlim(52500,57700)
ax1.set_ylim(-1.5,1.4)
ax2 = ax1.twiny()
#ax2.set_xlabel("Years",  fontsize=12)
ax1.set_xlabel("JD-2400000 [days]",  fontsize=12)
ax1.set_ylabel("Relative magnitude",  fontsize=12)
new_tick_locations = np.array([52500, 53500, 54500,55500,56500,57500])

new_tick_locations = np.array([52500, 53500, 54500,55500,56500,57500])
ax2.set_xlim(ax1.get_xlim())
ax2.set_xticks(new_tick_locations)
ax2.set_xticklabels(years)
plt.text(52780,0.1, 'B-A',horizontalalignment='center',fontsize=12, color='red')
plt.text(52780,-0.95, 'B-C',horizontalalignment='center',fontsize=12, color='green')
plt.text(52780,-0.45, 'B-D',horizontalalignment='center',fontsize=12, color='magenta')
plt.text(55000,1.7, 'Microlensing signal in RXJ1131-1231 quasar images ',horizontalalignment='center',fontsize=17)

fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/FB_RXJ.pdf'
plt.savefig(fname2)

