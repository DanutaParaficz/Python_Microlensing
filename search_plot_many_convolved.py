#!/usr/bin/env python
###################################################################################
###################################################################################
#Creates Ligtcurves and performes test if the simulated light cuvres vary the same
# way as data

#CALLING:
#python search_plot_many_convolved.py input 'quasar_name' 'data_file' convolution='YES/NO' convolution_value
#INPUT :

#input - from 1-11 -
#1: 100% dark matter in form of compact objects,
#2: 90% dark matter in form of compact objects,
#3: 80% dark matter in form of compact objects,
#4: 70% dark matter in form of compact objects,
#5: 60% dark matter in form of compact objects,
#6: 50% dark matter in form of compact objects,
#7: 40% dark matter in form of compact objects,
#8: 30% dark matter in form of compact objects,
#9: 20% dark matter in form of compact objects,
#10: 10% dark matter in form of compact objects,
#11: 1% dark matter in form of compact objects

#quasar_name - dicrectory where simulated quasar micorlesning data are e.g. 'HE0435_B_new'

#data_file - real datapoint of quasar lightcurve 'HE0435_all_astrofix_2016'

#convolution='YES/NO' - say if you want to perform convolution of the microlesing maps with source size

#convolution_value - source size with which will be convolved
###################################################################################
###################################################################################

import numpy as np
import os.path
import math
import sys
import pickle
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
import matplotlib.gridspec as gridspec

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
input=sys.argv[1]
quasar_name=sys.argv[2]
data_file=sys.argv[3]
convolution=sys.argv[4]
if len(sys.argv) == 5:
    convolution_value=sys.argv[5]
###################################################################################
# List of statysitical methods for
###################################################################################
def chi2(a, b):
    return np.sum((a-b) * (a-b))

def norm_a_chi2(a, b):
    return np.sum((a-b) * (a-b) / a)

def norm_b_chi2(a, b):
    return np.sum((a-b) * (a-b) / b)

def l1(a, b):
    return  np.sum(np.abs((a-b)))

def std_dev(a):
    return np.std(a)

def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


path=('/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/'+str(quasar_name)+'/mapmag'+str(input)+'.bin')

###################################################################################
# Converts microlensing maps from gerlump into magnitude units and writes it down
###################################################################################

if os.path.exists(path):
    with open(path) as f:
        map_magg = np.fromfile(f,'float')
else:
    with open(str(quasar_name)+'/map'+str(input)+'.bin') as f:
        map = np.fromfile(f,'i',-1,"")
        fline=open(str(quasar_name)+"/mapmeta"+str(input)+".dat").readline().rstrip()
        words = fline.split(" ")
        av_mag=float(words[0])
        av_num=float(words[1])
        map_flux=map*av_mag/av_num
        map_magg=2.5*np.log10(map_flux/av_mag)
        map_magg.mean()
    with open(str(quasar_name)+'/mapmag'+str(input)+'.bin', 'w') as outfile:
        outfile.write(map_magg)
    print outfile        
###################################################################################


###################################################################################
# Reshapes map into 2D and convolves it with source size, if necessary
###################################################################################
print map_magg.size
map2d = map_magg.reshape([10000,10000])
if convolution == 'yes':
    map2d = ndimage.gaussian_filter(map2d, sigma=convolution_value/1.18, order=0)
###################################################################################


###################################################################################
# Mirrors and appends microlensing maps for creating bigger map
###################################################################################
map_small=np.zeros((2500,2500))
for l, i in enumerate(range(0,int(math.sqrt(map_magg.size))-1,4)):
    for k, j in enumerate(range(0,int(math.sqrt(map_magg.size))-1,4)):
        map_small[l,k]= map2d[i,j]

map2d2_small=np.concatenate((map_small, np.fliplr(map_small), map_small, np.fliplr(map_small)), axis=1)
map2d4_small=np.concatenate((map2d2_small, np.flipud(map2d2_small),map2d2_small, np.flipud(map2d2_small)), axis=0)
###################################################################################


###################################################################################
# Creats random lightcurves
###################################################################################
guesses_no = int(1E3)
guesses = np.random.rand(guesses_no, 2)
guesses[:,0] = guesses[:,0] * 9999.
guesses[:,1] = guesses[:,1] * 9999.

source_list=np.loadtxt(open("/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/"+str(data_file)+".rdb","rb"))
dist=(source_list[:,0]-min(source_list[:,0]))*5.#2.18
print max(dist)
BC=source_list[:,3]-source_list[:,5]
print mad(BC)
#likelihood_methods = [chi2, norm_a_chi2, norm_b_chi2, l1]
likelihood_methods = [std_dev, mad]
best_fits = [(-1, sys.float_info.max)] * len(likelihood_methods)
fit_values = []
for i in range(len(likelihood_methods)):
    fit_values.append([])
a_table=[]
import matplotlib
matplotlib.rc('xtick', labelsize=21)
matplotlib.rc('ytick', labelsize=21)
import matplotlib.pyplot as plt
for iteration, (x0, y0) in enumerate(guesses):
    model=[]
    m_slope=(y0-9998.)/(dist.min()-dist.max())
    m_slope_negative=(y0-0.)/(dist.min()-dist.max())
    a=np.random.rand(1)*(m_slope-m_slope_negative)+m_slope_negative
    cos_a = math.cos(a)
    sin_a = math.sin(a)
    a_table.append(a)
    ys = dist * a + y0
    xs = dist

    for x, y in zip(xs, ys): 
        
        if x>=9999. or y>=9999.:
            x_acces=round(x/9999.) 
            y_acces=round(y/9999.) 
            model.append([map2d[int(round(x)-(10000*x_acces-1))][int(round(y)-(10000*y_acces-1))]])
        else:
            model.append(([map2d[int(round(x))][int(round(y))]]))


    if iteration % 100 == 0:
        gs = gridspec.GridSpec(3, 3)
        #plt.figure(figsize=(7,12))
        f=plt.figure(figsize=(10,10))
        ax1 = plt.subplot(gs[0:2,:])
        ax2 = plt.subplot(gs[-1,:])
        ax1.imshow(map2d,origin='lower')
        ax1.axis('off')
        # ax1.plot([min(xs), max(xs)], [min(ys), max(ys)], 'ro-',linewidth=5)
        print min(xs), max(xs), min(ys), max(ys)
        ax2.plot(xs, model,'ro')
        fileName=str(quasar_name)+'/map_'+str(input)+'/convolved_'+str(iteration)
        #ax1.set_xlim([1,10000])
        #ax1.set_ylim([1,10000])
        ax2.set_xlabel("Days",  fontsize=21)
        ax2.set_ylabel("Magnitude",  fontsize=21)
        ax2.set_ylim([-0.8,1.6])
        plt.savefig(fileName, format="png")
        #plt.show()
        plt.clf()


    for method_i, method in enumerate(likelihood_methods):
        fitness = method(model)
        fit_values[method_i].append(fitness)
###################################################################################

###################################################################################
# Saves lists of statistics performed with simulated lightcurves
###################################################################################
f = open(str(quasar_name)+'/stat'+str(input)+'.txt', 'w')
print '\nStatistics:'
for method, values in zip(likelihood_methods, fit_values):
    values = np.asarray(values)
    f.write(method.func_name)
    temp=('Mean =', np.mean(values), '\n')
    f.write(str(temp))
    temp=('Median =', np.median(values), '\n')
    f.write(str(temp))
    temp=('Mean best 100 =', np.mean(np.sort(values)[:100]), '\n')
    f.write(str(temp))
    if method.func_name == 'std_dev':
        les_0_05 = len(values[values<0.05*2.])
        temp=('Less than 0.05 :', les_0_05, 'or', (100.*les_0_05/len(values)),'%')
        f.write(str(temp))
    if method.func_name == 'mad':
        les_0_032 = len(values[values<0.032*2.])
        temp=('Less than 0.032 :', les_0_032, 'or', (100.* les_0_032/len(values)),'%')
        f.write(str(temp))

print '0.'+str(input)+'%'
print 'Less than 0.032 :', les_0_032, 'or', (100.* les_0_032/len(values)),'%'
print 'Less than 0.05 :', les_0_05, 'or', (100.*les_0_05/len(values)),'%'
    
f.close()

#if '-p' in sys.argv:
#for i, (method, values) in enumerate(zip(likelihood_methods, fit_values)):
#    plt.figure(i)
#    plt.title(method.func_name)
#    plt.plot(range(len(values)), values)
#    plt.show()

###################################################################################

