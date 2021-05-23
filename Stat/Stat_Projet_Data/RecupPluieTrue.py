
import pandas as pd
from pandas.core.frame import DataFrame


def openMonCsv(ver):
    data = pd.read_csv(ver)
    return data

def AddHour(data):
    tabHeure = []
    for rowIndex in range(0,len(data)):
        #if(int(str(data[" date/$date"][rowIndex])[12:14]) > heureDebut and int(str(data[" date/$date"][rowIndex])[12:14]) < heureFin ):
        tabHeure.append(int(str(data[" date/$date"][rowIndex])[12:14]))
    data.insert(7, "hour", tabHeure, True)
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


def TrieTaille(tailleMin ,tailleMax, dataframe_collection , monCsv):
    newData_Collection = []
    blockage = 0
    for elem in dataframe_collection:
        if(elem[1] - elem[0] > tailleMin and elem[1] - elem[0] < tailleMax):
            blockage+=1
            newData_Collection.append(monCsv[elem[0]:elem[1]-2])
            if(blockage == 10)  :
                break   
    return newData_Collection


def MoyenneMidPerdiodeFalsePluieVsBeforePluie(newData_Collection):
    tabMoyenneMillieu = []
    tabMoyenneBefore = []
    for elem in newData_Collection:
        if(len(elem) % 2 == 0):  
            tabMoyenneMillieu.append(elem.iloc[int(len(elem)/2):int(len(elem)/2+1)],)
            tabMoyenneBefore.append(elem.iloc[len(elem)-3:len(elem)-2])
        else:  
            tabMoyenneMillieu.append(elem.iloc[int((len(elem)+1)/2):int((len(elem)+1)/2+1)],)
            tabMoyenneBefore.append(elem.iloc[len(elem)-3:len(elem)-2])
            
          
      

    return (tabMoyenneMillieu , tabMoyenneBefore)


def resMoyenneMillieu(tabMoyenneMillieu):
    indexMillieu = 0
    indexMillieuT = 0
    indexMillieuP = 0
    indexMillieuL = 0
    moyenneHumidityMillieu  = 0 
    moyennePressureMillieu = 0
    moyenneTemperatureMillieu= 0
    moyenneLightMillieu = 0
    
    #print(tabMoyenneMillieu)
    for elem in tabMoyenneMillieu:
        # humidity
        values_view = dict(elem[' humidity']).values()
        value_iterator = iter(values_view)
        first_value = next(value_iterator)

        if(first_value != ' ' and  first_value != ''):
            moyenneHumidityMillieu += int(first_value)
            indexMillieu+=1
        # temp
        values_viewT = dict(elem[' temperature']).values()
        value_iteratorT = iter(values_viewT)
        first_valueT = next(value_iteratorT)
        
        if(first_valueT != ' ' and  first_valueT != ''):
            moyenneTemperatureMillieu += int(first_valueT)
            indexMillieuT+=1

        #pressure
        values_viewP = dict(elem[' pressure']).values()
        value_iteratorP = iter(values_viewP)
        first_valueP = next(value_iteratorP)
        
        if(first_valueP != ' ' and  first_valueP != ''):
            moyennePressureMillieu += int(first_valueP)
            indexMillieuP+=1
        
        #ligth
        values_viewL = dict(elem[' light']).values()
        value_iteratorL = iter(values_viewL)
        first_valueL = next(value_iteratorL)
        
        if(first_valueL != ' ' and  first_valueL != ''):
            moyenneLightMillieu += int(first_valueL)
            indexMillieuL+=1
    return {"HumidityM": moyenneHumidityMillieu/indexMillieu , "TemperatureM":moyenneTemperatureMillieu/indexMillieuT,
     "PressureM": moyennePressureMillieu/indexMillieuP, "LightM": moyenneLightMillieu/indexMillieuL}
        

def resMoyenneBefore(tabMoyenneBefore):
    indexMillieu = 0
    indexMillieuT = 0
    indexMillieuP = 0
    indexMillieuL = 0
    moyenneHumidityMillieu  = 0 
    moyennePressureMillieu = 0
    moyenneTemperatureMillieu= 0
    moyenneLightMillieu = 0
    
    #print(tabMoyenneMillieu)
    for elem in tabMoyenneBefore:
        # humidity
        values_view = dict(elem[' humidity']).values()
        value_iterator = iter(values_view)
        first_value = next(value_iterator)

        if(first_value != ' ' and  first_value != ''):
            moyenneHumidityMillieu += int(first_value)
            indexMillieu+=1
        # temp
        values_viewT = dict(elem[' temperature']).values()
        value_iteratorT = iter(values_viewT)
        first_valueT = next(value_iteratorT)
        
        if(first_valueT != ' ' and  first_valueT != ''):
            moyenneTemperatureMillieu += int(first_valueT)
            indexMillieuT+=1

        #pressure
        values_viewP = dict(elem[' pressure']).values()
        value_iteratorP = iter(values_viewP)
        first_valueP = next(value_iteratorP)
        
        if(first_valueP != ' ' and  first_valueP != ''):
            moyennePressureMillieu += int(first_valueP)
            indexMillieuP+=1
        
        #ligth
        values_viewL = dict(elem[' light']).values()
        value_iteratorL = iter(values_viewL)
        first_valueL = next(value_iteratorL)
        
        if(first_valueL != ' ' and  first_valueL != ''):
            moyenneLightMillieu += int(first_valueL)
            indexMillieuL+=1
    return {"HumidityB": moyenneHumidityMillieu/indexMillieu , "TemperatureB":moyenneTemperatureMillieu/indexMillieuT,
     "PressureB": moyennePressureMillieu/indexMillieuP, "LightB": moyenneLightMillieu/indexMillieuL}


monCsv = openMonCsv("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainSorti.csv")
AddHour(monCsv)
maTabPluie = trie(monCsv)
tabDataFrame = SubsetData(maTabPluie)
newCollection = TrieTaille(50,800,tabDataFrame , monCsv)

print(resMoyenneMillieu(MoyenneMidPerdiodeFalsePluieVsBeforePluie(newCollection)[0]))
print(resMoyenneBefore(MoyenneMidPerdiodeFalsePluieVsBeforePluie(newCollection)[1]))