from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import pandas as pd

#Generate 10 "clouds" of point in space - create input data for kmeans example
samplesCount = 1000
featuresCount = 3
centersCount = 10

X, Y = make_blobs(n_samples = samplesCount, centers = centersCount, n_features = featuresCount, random_state = 42)

#Add a row index
np.savetxt("input.csv", X, delimiter=" ")