
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


class KNN():

    def __init__(self, pathDonneeTrain , pathDonneTest , kvoisins):
        self.pathDonneeTrain = pathDonneeTrain
        self.pathDonneeTest = pathDonneTest
        self.voisin = []
        self.valeurRes = []
        self.kvoisins = kvoisins

    def knn(self):
        datasetTrain = np.genfromtxt(self.pathDonneeTrain, delimiter=",").astype("int")
        datasetTest = np.genfromtxt(self.pathDonneeTest, delimiter=",").astype("int")
        neigh = NearestNeighbors(n_neighbors= self.kvoisins )
        neigh.fit(datasetTrain)
        b = neigh.kneighbors_graph(datasetTrain)
        print(b)
        self.voisin =  neigh.kneighbors([datasetTest])[1][0] 
        #print(self.voisin)

    def correspondance(self):
        datasetTrain = np.genfromtxt(self.pathDonneeTrain, delimiter=",").astype("int")
        for elem in self.voisin:
            self.valeurRes.append(datasetTrain[elem][-1])
        print(self.valeurRes)

    def resultat(self):
        #a = ["a", "b", "a"]
        result = dict((i, self.valeurRes.count(i)) for i in self.valeurRes)
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True) )
        print(list(result.keys())[0])
        return list(result.keys())[0]


    
        


test = KNN("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainFinale.csv" , "C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTestFinale.csv" , 10 )
test.knn()
#test.correspondance()
#test.resultat()

