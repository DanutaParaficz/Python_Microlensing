import astropy.time
import dateutil.parser
import numpy as np
from uncertainties import ufloat
import matplotlib.patches as mpatches
import datetime
from jdcal import jd2gcal
from jdcal import MJD_0, MJD_JD2000



source_list=np.loadtxt(open("/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/HE0435_all_astrofix_2016.rdb","rb"))

num_days=source_list[0,0]-source_list[source_list[:,1].size-1,0]
magA=source_list[:,1]
magB=source_list[:,3]
magC=source_list[:,5]
magD=source_list[:,7]

num_days=source_list[source_list[:,1].size-1,0]-source_list[0,0]

years=[str(jd2gcal(MJD_0,52500)[0]),str(jd2gcal(MJD_0,53500)[0]),str(jd2gcal(MJD_0,54500)[0]),str(jd2gcal(MJD_0,55500)[0]),str(jd2gcal(MJD_0,56500)[0]),str(jd2gcal(MJD_0,57500)[0])]
import matplotlib 
matplotlib.rc('xtick', labelsize=12)
matplotlib.rc('ytick', labelsize=12)
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,9), dpi=100)
ax1 = fig.add_subplot(212)
ax1.scatter(np.array(source_list[:,0]), np.array(magA),edgecolor='None',c='r',s=3, label="A")
ax1.scatter(np.array(source_list[:,0])-8., np.array(magB)+0.1,edgecolor='None', c='b',s=3, label="B - 8 days")
ax1.scatter(np.array(source_list[:,0]), np.array(magC),edgecolor='None', c='g',s=3, label="C")
ax1.scatter(np.array(source_list[:,0])-15., np.array(magD)-0.1,edgecolor='None', c='m',s=3, label="D - 15 days")

#plt.legend(loc=2,fontsize=12,markerscale=1)
ax2 = ax1.twiny()
#ax2.set_xlabel("Years",  fontsize=12)
ax1.set_xlabel("JD-2400000 [days]",  fontsize=12)
ax1.set_ylabel("Relative magnitude",  fontsize=12)
ax1.set_xlim(52500,57700)
ax1.set_ylim(-8.9,-11.4)
new_tick_locations = np.array([52500, 53500, 54500,55500,56500,57500])
ax2.set_xlim(ax1.get_xlim())
ax2.set_xticks(new_tick_locations)
ax2.set_xticklabels(years)
plt.text(52780,-9.5, 'D',horizontalalignment='center',fontsize=12, color='magenta')
plt.text(52780,-10.0, 'C',horizontalalignment='center',fontsize=12, color='green')
plt.text(52950,-10.57, 'B - 8 days',horizontalalignment='center',fontsize=12, color='blue')
plt.text(52990,-11.05, 'A - 15 days',horizontalalignment='center',fontsize=12, color='red')
plt.text(55000,-11.8, 'Lightcurves of HE0435-1223 quasar images ',horizontalalignment='center',fontsize=17)
plt.text(55000,-11.65, '(intrisic viariability of quasar + microlensing singal)',horizontalalignment='center',fontsize=17)
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/All_HE0435.pdf'
plt.savefig(fname2, dpi=100)


import matplotlib
matplotlib.rc('xtick', labelsize=90)
matplotlib.rc('ytick', labelsize=90)
import matplotlib.pyplot as plt

num_days=source_list[source_list[:,1].size-1,0]-source_list[0,0]

years=[str(jd2gcal(MJD_0,52500)[0]),str(jd2gcal(MJD_0,53500)[0]),str(jd2gcal(MJD_0,54500)[0]),str(jd2gcal(MJD_0,55500)[0]),str(jd2gcal(MJD_0,56500)[0]),str(jd2gcal(MJD_0,57500)[0])]
import matplotlib
matplotlib.rc('xtick', labelsize=12)
matplotlib.rc('ytick', labelsize=12)
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,9), dpi=100)
ax1 = fig.add_subplot(212)
ax1.scatter(np.array(source_list[:,0]), np.array(magB-magA),edgecolor='None',c='r',s=3, label="B-A")
ax1.scatter(np.array(source_list[:,0]), np.array(magB-magC)+0.4,edgecolor='None',c='g',s=3, label="B-C")
ax1.scatter(np.array(source_list[:,0]), np.array(magB-magD)+0.47,edgecolor='None',c='m',s=3, label="B-D")
#plt.legend(loc=2,fontsize=12,markerscale=1)
ax2 = ax1.twiny()
#ax2.set_xlabel("Years",  fontsize=12)
ax1.set_xlabel("JD-2400000 [days]",  fontsize=12)
ax1.set_ylabel("Relative magnitude",  fontsize=12)
ax1.set_xlim(52500,57700)
ax1.set_ylim(-0.9,0.9)
new_tick_locations = np.array([52500, 53500, 54500,55500,56500,57500])
ax2.set_xlim(ax1.get_xlim())
ax2.set_xticks(new_tick_locations)
ax2.set_xticklabels(years)
plt.text(52780,0.5, 'B-A',horizontalalignment='center',fontsize=12, color='red')
plt.text(52780,0., 'B-C',horizontalalignment='center',fontsize=12, color='green')
plt.text(52780,-0.4, 'B-D',horizontalalignment='center',fontsize=12, color='magenta')
plt.text(55000,1.2, 'Microlensing signal in HE0435-1223 quasar images ',horizontalalignment='center',fontsize=17)

fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/FB_HE0435.pdf'
plt.savefig(fname2)

import matplotlib 
matplotlib.rc('xtick', labelsize=90) 
matplotlib.rc('ytick', labelsize=90) 
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(100,50))
ax1 = fig.add_subplot(111)
ax1.plot(np.array(source_list[:,0])-8., np.array(magB), 'bs',markersize=20, label="A")
ax1.plot(np.array(source_list[:,0]), np.array(magC), 'gs',markersize=20, label="C")
ax1.plot(np.array(source_list[:,0]), np.array(magC-magB)-10., 'rs',markersize=20, label="C-B")
plt.legend(loc=2,fontsize=99,markerscale=2)
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/FBFC_HE0435.pdf'
plt.savefig(fname2)




import matplotlib 
matplotlib.rc('xtick', labelsize=90) 
matplotlib.rc('ytick', labelsize=90) 
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(100,50))
ax1 = fig.add_subplot(111)
ax1.plot(np.array(source_list[:,0]), np.array(magA), 'rs',markersize=20, label="A")
ax1.plot(np.array(source_list[:,0])-15., np.array(magD), 'gs',markersize=20, label="D")
ax1.plot(np.array(source_list[:,0]), np.array(magD-magA)-10., 'bs',markersize=20, label="A-D")
plt.legend(loc=2,fontsize=99,markerscale=2)
fname2='/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/FAFD_HE0435.pdf'
plt.savefig(fname2)

