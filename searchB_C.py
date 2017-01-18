#!/usr/bin/env python

import numpy as np
import os.path
import math
import sys
import pickle
import matplotlib.pyplot as plt
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot


input=11#sys.argv[1]

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


path_C=('../HE0435_C_new/mapmag'+str(input)+'.bin')
path_B=('../HE0435_B_new/mapmag'+str(input)+'.bin')

if os.path.exists(path_C):
    with open(path_C) as f:
        map_magg_C = np.fromfile(f,'float')
else:
    with open('../HE0435_C_new/map'+str(input)+'/map.bin') as f:
        map = np.fromfile(f,'i',-1,"")
        fline=open("./HE0435_C_new/mapmeta"+str(input)+".dat").readline().rstrip()
        words = fline.split(" ")
        av_mag=float(words[0])
        av_num=float(words[1])
        map_flux=map*av_mag/av_num
        map_magg_C=np.log10(map_flux/av_mag)
        map_magg_C.mean()
    with open('../HE0435_C_new/mapmag'+str(input)+'.bin', 'w') as outfile_C:
        outfile_C.write(map_magg_C)
    print outfile_C  
 
if os.path.exists(path_B):
    with open(path_B) as f:
        map_magg_B = np.fromfile(f,'float')
else:
    with open('../HE0435_B_new/map'+str(input)+'/map.bin') as f:
        map = np.fromfile(f,'i',-1,"")
        fline=open("../HE0435_B_new/mapmeta"+str(input)+".dat").readline().rstrip()
        words = fline.split(" ")
        av_mag=float(words[0])
        av_num=float(words[1])
        map_flux=map*av_mag/av_num
        map_magg_B=np.log10(map_flux/av_mag)
        map_magg_B.mean()
    with open('../HE0435_B_new/mapmag'+str(input)+'.bin', 'w') as outfile_B:
        outfile_B.write(map_magg_B)
    print outfile_B      

print map_magg_C.size
print map_magg_B.size
map2d_C = map_magg_C.reshape([10000,10000])
map2d_B = map_magg_B.reshape([10000,10000])

guesses_no = int(1E3)
guesses = np.random.rand(guesses_no, 2)
guesses[:,0] = guesses[:,0] * 9999.
guesses[:,1] = guesses[:,1] * 9999.

source_list=np.loadtxt(open("/Users/danka/Documents/MY_PUBLICATIONS/PremodialBHMicrolensing/HE0435_all_astrofix_2016.rdb","rb"))
dist=(source_list[:,0]-min(source_list[:,0]))*2.16
BC=source_list[:,3]-source_list[:,5]
print mad(BC)
#likelihood_methods = [chi2, norm_a_chi2, norm_b_chi2, l1]
likelihood_methods = [std_dev, mad]
best_fits = [(-1, sys.float_info.max)] * len(likelihood_methods)
fit_values = []
for i in range(len(likelihood_methods)):
    fit_values.append([])
a_table=[]

for iteration, (x0, y0) in enumerate(guesses):
    
    m_slope=(y0-9998.)/(dist.min()-dist.max())
    m_slope_negative=(y0-0.)/(dist.min()-dist.max())
    a=np.random.rand(1)*(m_slope-m_slope_negative)+m_slope_negative
    cos_a = math.cos(a)
    sin_a = math.sin(a)
    a_table.append(a)
    ys = dist * a + y0
    xs = dist
    


    model_C = np.asarray([map2d_C[int(round(x))][int(round(y))] for x, y in zip(xs, ys)])
    model_B = np.asarray([map2d_B[int(round(x))][int(round(y))] for x, y in zip(xs, ys)])
    model = model_C-model_B
    
    
    
    if iteration % 2000 == 0:
#        fig, axes = plt.subplots(nrows=2)
        ax01 = subplot2grid((2, 2), (0, 0))
        ax02 = subplot2grid((2, 2), (0, 1))
        ax03 = subplot2grid((2, 2), (1, 0), colspan=2, rowspan=1)
        ax01.imshow(map2d_C)
        ax01.axis('off')
        ax01.set_xlim(1,9999)
        ax02.set_ylim(1,9999)
        ax02.set_xlim(1,9999)
        ax01.set_ylim(1,9999)
        ax01.plot([min(xs), max(xs)], [min(ys), max(ys)], 'ro-')
        ax02.imshow(map2d_B)
        ax02.axis('off')
        ax02.plot([min(xs), max(xs)], [min(ys), max(ys)], 'ro-')
        ax03.plot(xs, -model,'ro')
        ax03.set_xlabel("Days",  fontsize=21)
        ax03.set_ylabel("Magnitude",  fontsize=21)
        fileName=str(iteration)
        plt.savefig(fileName, format="png")
        plt.show()
        plt.clf()
        print fileName
    
    for method_i, method in enumerate(likelihood_methods):
        fitness = method(model)
        fit_values[method_i].append(fitness)
 

f = open('stat'+str(input)+'.txt', 'w')
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
    print method.func_name
    print 'Mean best 100 =', np.mean(np.sort(values)[:100])
    print 'STD of best 100 =', np.std(np.sort(values)[:100])

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



