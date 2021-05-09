
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import NearestNeighbors
import csv




class csvToarray:
        def __init__(self, pathDonneeTrain , pathDonneTest):
            self.pathDonneeTrain = pathDonneeTrain
            self.pathDonneeTest = pathDonneTest
        
        def convert(self):
            datasetTrain = np.genfromtxt(self.pathDonneeTrain, delimiter=",").astype("int")
            datasetTest = np.genfromtxt(self.pathDonneeTest, delimiter=",").astype("int")
            return [datasetTrain , datasetTest]


class KNN():

    def __init__(self, dataTrain ,  dataTest, kvoisins):
        self.voisin = []
        self.valeurRes = []
        self.kvoisins = kvoisins
        self.dataTrain = dataTrain
        self.dataTest = dataTest
        self.resultatFinal = []

    def knn(self):
        '''datasetTrain = np.genfromtxt(self.pathDonneeTrain, delimiter=",").astype("int")
        datasetTest = np.genfromtxt(self.pathDonneeTest, delimiter=",").astype("int")'''
        neigh = NearestNeighbors(n_neighbors= self.kvoisins ) 
        neigh.fit(self.dataTrain)
        self.voisin =  neigh.kneighbors([self.dataTest])[1][0] 
        return self.voisin

    
    
  
        



    


    
        




