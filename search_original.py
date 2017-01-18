#!/usr/bin/env python

import numpy as np
import math
import sys
import pickle
import matplotlib.pyplot as plt

def chi2(a, b):
    return np.sum((a-b) * (a-b))

def norm_a_chi2(a, b):
    return np.sum((a-b) * (a-b) / a)

def norm_b_chi2(a, b):
    return np.sum((a-b) * (a-b) / b)

def l1(a, b):
    return  np.sum(np.abs((a-b)))

def std_dev(a, b):
    return np.std(a)

with open(sys.argv[1]) as f:
    map = np.fromfile(f,'float64',-1,"")

map2d = map.reshape([10000,10000])

with open('true_vals.bin') as f:
    true_vals = pickle.load(f)

with open('obs_data.bin') as f:
    obs_data = pickle.load(f)

guesses_no = int(1E3)
guesses = np.random.rand(guesses_no, 3)
guesses[:,0] = guesses[:,0] * 5000
guesses[:,1] = guesses[:,1] * 5000
guesses[:,2] = guesses[:,2] *  math.pi / 2.

#guesses[:,0] = true_vals[0][0] + np.random.random() * 2
#guesses[:,1] = true_vals[0][1] + np.random.random() * 2

for expected, data in zip(true_vals, obs_data):

    dist = data[0]
    values = data[1]
    
    print 'Expected:', expected, '\n'

    best_chi2_fit = (-1, sys.float_info.max)
    best_norm_chi2_fit = (-1, sys.float_info.max)
    best_l1_fit = (-1, sys.float_info.max)

    #likelihood_methods = [chi2, norm_a_chi2, norm_b_chi2, l1]
    likelihood_methods = [std_dev]
    best_fits = [(-1, sys.float_info.max)] * len(likelihood_methods)
    fit_values = []
    for i in range(len(likelihood_methods)):
        fit_values.append([])

    for iteration, (x0, y0, a) in enumerate(guesses):

        if iteration % 1000 == 0:
            print 'Iteration :', iteration

        cos_a = math.cos(a)
        sin_a = math.sin(a)

        xs = dist * cos_a + x0
    	ys = dist * sin_a + y0
        
        model = np.asarray([map2d[int(round(x))][int(round(y))] for x, y in zip(xs, ys)])

	for method_i, method in enumerate(likelihood_methods):
            fitness = method(model, values)
            fit_values[method_i].append(fitness)
            if (fitness < best_fits[method_i][1]):
                best_fits[method_i] = (iteration, fitness)
                print 'New', method.func_name, 'min:', best_fits[method_i], '- guess:', (x0, y0, a)


    print '\nExpected:'
    print '    ',expected, '\n'
    print 'Results:'
    for method, fit in zip(likelihood_methods, best_fits):
        x0, y0, a = guesses[fit[0]]
        print '    ', method.func_name, ':', (x0, y0, a), '- iter:', fit[0], '- fit:', fit[1]

    print '\nStatistics:'
    for method, values in zip(likelihood_methods, fit_values):
        values = np.asarray(values)
        print '    ', method.func_name, ':'
        print '       Mean =', np.mean(values)
        print '       Median =', np.median(values)
        print '       Mean best 100 =', np.mean(np.sort(values)[:100])
        les_0_05 = len(values[values<0.05])
        print '       Less than 0.05 :', les_0_05, 'or', (100.*les_0_05/len(values)),'%'

    if '-p' in sys.argv:
        for i, (method, values) in enumerate(zip(likelihood_methods, fit_values)):
            plt.figure(i)
            plt.title(method.func_name)
            plt.plot(range(len(values)), values)
        plt.show()

    break
