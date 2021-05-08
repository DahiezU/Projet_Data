
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import NearestNeighbors
import csv



'''>>> samples = [[0., 0., 0.], [0., .5, 0.], [1., 1., .5]]
>>> from sklearn.neighbors import NearestNeighbors
>>> neigh = NearestNeighbors(n_neighbors=1)
>>> neigh.fit(samples)
NearestNeighbors(n_neighbors=1)
>>> print(neigh.kneighbors([[1., 1., 1.]]))
(array([[0.5]]), array([[2]]))'''


dataset = np.genfromtxt("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\transfome\\dataTestPetit.csv", delimiter=",").astype("int")

numpy_array = np.genfromtxt("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\transfome\\dataTestPetit.csv", delimiter=",").astype("int")


neigh = NearestNeighbors(n_neighbors=5)


neigh.fit(dataset)


print(neigh.kneighbors([[111,   73 ,111,   1004 ,   14 ,   0 ]]))