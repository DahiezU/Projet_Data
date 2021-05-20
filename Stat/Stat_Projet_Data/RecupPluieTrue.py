
import pandas as pd
from pandas.core.frame import DataFrame
def openMonCsv(ver):
    data = pd.read_csv(ver)
    return data

def trie(data) :
    tabindexDebutFinPluieFalse = []
    for rowIndex in range(0,len(data)-1):
        if(rowIndex != len(data)-1):
           
            if(data[" rain"][rowIndex] == ' 0' and rowIndex == 1):
                tabindexDebutFinPluieFalse.append(rowIndex)
            if(data[" rain"][rowIndex] == ' '):
                rowIndex += 1
            elif(data[" rain"][rowIndex+1] == ' '):
                rowIndex += 1
            elif(int(data[" rain"][rowIndex]) <= 0 and  int(data[" rain"][rowIndex+1]) > 0 ):
                tabindexDebutFinPluieFalse.append(rowIndex+3)
            elif (int(data[" rain"][rowIndex])  > 0  and  int(data[" rain"][rowIndex+1]) <= 0):
                tabindexDebutFinPluieFalse.append(rowIndex+3)
    #print(tabindexDebutFinPluieFalse)
    return tabindexDebutFinPluieFalse


def SubsetData(tabindexDebutFinPluieFalse):
    dataframe_collection = [] 
    for i in range(0,len(tabindexDebutFinPluieFalse)):
        if( i % 2 == 0):
            if(i+1 != len(tabindexDebutFinPluieFalse)):
                dataframe_collection.append((tabindexDebutFinPluieFalse[i],tabindexDebutFinPluieFalse[i+1]))
    return dataframe_collection


def TrieTaille(tailleMin , dataframe_collection , monCsv):
    newData_Collection = []
    blockage = 0
    for elem in dataframe_collection:
        if(elem[1] - elem[0] > tailleMin):
            blockage+=1
            newData_Collection.append(monCsv[elem[0]:elem[1]-2])
            if(blockage == 10)  :
                break   
    return newData_Collection

monCsv = openMonCsv("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainSorti.csv")
maTabPluie = trie(monCsv)
tabDataFrame = SubsetData(maTabPluie)
newCollection = TrieTaille(50,tabDataFrame , monCsv)

print(newCollection)
