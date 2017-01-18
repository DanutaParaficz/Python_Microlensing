#!/usr/bin/env python

import numpy as np
import os.path
import math
import sys
import pickle
import matplotlib.pyplot as plt

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
input=sys.argv[1]

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


path=('./mapmag'+str(input)+'.bin')


if os.path.exists(path):
    with open(path) as f:
        map_magg = np.fromfile(f,'float')
else:
    with open('map'+str(input)+'.bin') as f:
        map = np.fromfile(f,'i',-1,"")
        fline=open("mapmeta"+str(input)+".dat").readline().rstrip()
        words = fline.split(" ")
        av_mag=float(words[0])
        av_num=float(words[1])
        map_flux=map*av_mag/av_num
        map_magg=np.log10(map_flux/av_mag)
        map_magg.mean()
    with open('mapmag'+str(input)+'.bin', 'w') as outfile:
        outfile.write(map_magg)
    print outfile        

print map_magg.size
map2d = map_magg.reshape([10000,10000])


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


    model = np.asarray([map2d[int(round(x))][int(round(y))] for x, y in zip(xs, ys)])
    


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



