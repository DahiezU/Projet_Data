import knnV2

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv


class Correspondance():
    def __init__(self,tabVoisin , csvPath):
        self.tabVoisin = tabVoisin
        self.csvPath = csvPath
        self.valeurRes = []
    
    def correspondance(self):
        datasetTrain = np.genfromtxt(self.csvPath, delimiter=",").astype("int")
        for elem in self.tabVoisin:
            self.valeurRes.append(datasetTrain[elem][-1])
        #print(self.valeurRes)

    def resultat(self):
        #a = ["a", "b", "a"]
        result = dict((i, self.valeurRes.count(i)) for i in self.valeurRes)
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True) )
        #print(list(result.keys())[0])
        return list(result.keys())[0]



#test = knnV2.KNN("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainFinale.csv" , "C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTestFinale.csv" , 10 )
#test.knn()
#test.correspondance()
#test.resultat()



'''cor = Correspondance(test.knn() , "C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainSortiSortie.csv")
cor.correspondance()
cor.resultat()'''