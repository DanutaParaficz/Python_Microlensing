#!/usr/bin/env python

import numpy as np
import math
import pickle

with open('map5.bin') as f:
    map = np.fromfile(f,'i',-1,"")

map2d = map.reshape([10000,10000])

observations = 100
samples = 800

true_vals = []
obs_data = []

for i in range(observations):

    x0 = np.random.rand() * 5000
    y0 = np.random.rand() * 5000
    #print 'Random begin :', x0, ',', y0

    angle = np.random.rand() * math.pi / 2.
    #print 'Random angle :', angle

    true_vals.append([x0, y0, angle])

    dist = np.sort(np.random.rand(samples) * 5000)

    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    xs = dist * cos_a + x0
    ys = dist * sin_a + y0

    values = [map2d[int(round(x))][int(round(y))] for x, y in zip(xs, ys)]

    obs_data.append([dist, values])

with open('true_vals_5.bin', 'w') as f:
    pickle.dump(true_vals, f)
with open('obs_data_5.bin', 'w') as f:
    pickle.dump(obs_data, f)
