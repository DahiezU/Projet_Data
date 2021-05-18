
import Correspondance as cr
import knnV2
import csv


#test = knnV2.KNN("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainFinale.csv" , "C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTestFinale.csv" , 10 )
#test.knn()
#test.correspondance()
#test.resultat()



'''cor = Correspondance(test.knn() , "C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainSortiSortie.csv")
cor.correspondance()
cor.resultat()'''

class Statitstique():
    def __init__(self, dataTrain , dataTest , pathCsvToCompareTo , pathVraie, kvoisins):
        self.pathCsvToCompareTo = pathCsvToCompareTo
        self.dataTrain  = dataTrain
        self.dataTest = dataTest
        self.kvoisins = kvoisins
        self.pathVraie = pathVraie
        self.resFound = []
        self.resVraie = []
      
    def stockVrai(self):
        with open(self.pathVraie, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader: 
                self.resVraie.append(int(row[-1]))
        print("Resultat Vrai -> ",self.resVraie)

    def calculKnnTab(self):
            for elem in self.dataTest:
                knnUnique = knnV2.KNN(self.dataTrain , elem , self.kvoisins)
                cor= cr.Correspondance(knnUnique.knn() ,  self.pathCsvToCompareTo )
                cor.correspondance()
                self.resFound.append(cor.resultat())
            print("Resultat Trouve -> " ,self.resFound)

    def VFandV(self):
        VP  = 0
        VN = 0 
        FP  = 0 
        FN = 0
        for i in range(len(self.resVraie)):
            if(self.resVraie[i] == 1 and  self.resFound[i] == 1):
                VP+=1
            elif(self.resVraie[i] == 0 and  self.resFound[i] == 0 ):
                VN+=1
            elif(self.resVraie[i] == 1 and  self.resFound[i] == 0 ):
                FN+=1
            elif(self.resVraie[i] == 0 and  self.resFound[i] == 1 ):
                FP+=1
        return {"VP": VP,  "VN":VN  , "FN":FN , "FP":FP}

    def Accuracy(self,dictVal):
        return (dictVal['VP'] +  dictVal['VN'] ) / ( dictVal['VP'] + dictVal['FP'] + dictVal['VN'] + dictVal['FN'] )

    def Precision(self , dictVal):
        return dictVal['VP'] /(dictVal['VP'] + dictVal['FP'])

    def Sensibilite(self , dictVal):
        return dictVal['VP'] /(dictVal['VP'] + dictVal['FN'])

    def F1_score(self , confiance , sensibilite , dictVal):
        return 2*(  (self.Precision(dictVal) * (self.Sensibilite(dictVal)) ) /  ( (self.Precision(dictVal) + (self.Sensibilite(dictVal))) )  )



a = knnV2.csvToarray("C:\\Users\\dahie\\Documents\\SDN-S6\\Projet_Data\\DataV2\\dataTrainFinale.csv" , 
"C:\\Users\\dahie\\Documents\\SDN-S6\\Projet_Data\\DataV2\\dataTestFinale.csv")

#a.convert()

stat   = Statitstique( a.convert()[0] , a.convert()[1] , "C:\\Users\\dahie\\Documents\\SDN-S6\\Projet_Data\\DataV2\\dataTrainSortiSortie.csv", 
"C:\\Users\\dahie\\Documents\\SDN-S6\\Projet_Data\\DataV2\\dataVraie.csv",10)

stat.calculKnnTab()
stat.stockVrai()
print(stat.VFandV())
print("Accuracy : " ,stat.Accuracy(stat.VFandV()))
print(" Precision : " ,stat.Precision(stat.VFandV()))
print("Sensibilite :" , stat.Sensibilite(stat.VFandV()))
print("F1-score : " , stat.F1_score( stat.Precision(stat.VFandV()) ,  stat.Sensibilite(stat.VFandV()) , stat.VFandV() ))