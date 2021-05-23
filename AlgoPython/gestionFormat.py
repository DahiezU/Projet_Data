
import csv
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta


class FormatData():
    def __init__(self, pathDonneeTrainEntree , pathDonneTestEntree , pathDonneeTrainSorti , pathDonneeTestSorti):
        self.pathDonneeTrainEntree = pathDonneeTrainEntree
        self.pathDonneeTestEntree = pathDonneTestEntree
 
        self.pathDonneeTrainSorti =  pathDonneeTrainSorti
        self.pathDonneeTestSorti =  pathDonneeTestSorti
 

    def  decale(self ,donneeEntree , donneeSortie):
        with open(donneeEntree, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            with open( donneeSortie, 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                for row in spamreader: 
                        row  = row[0].split(',') 
                        spamwriter.writerow( [row[0] + ',' , row[1] + ',', row[2] + ',', row[3] + ',', row[4]+ ','  , row[6] + ',', row[5]])

    
    
    
    def transformDate(self ,CsvEntre , CsvSorti):
        i = 0
        with open(CsvEntre, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            with open(CsvSorti, 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                for row in spamreader: 
                    if(i==0):
                        next(spamreader)
                        i += 1
                    else:
                        if(row[0] != '' and  row[1] != '' and  row[2] != '' and  row[3] != '' and  row[4] != '' and  row[5] != '' and  row[6] != ''):
                            if(row[0] != ' ' and  row[1] != ' ' and  row[2] != ' ' and  row[3] != ' ' and  row[4] != ' ' and  row[5] != ' ' and  row[6] != ' '):
                                dateEntre  = row[2]
                                f_date = date(int(dateEntre[0:5]), 1, 1)
                                l_date = date(int(dateEntre[0:5]), int(dateEntre[6:8]), int(dateEntre[9:11]))
                                if(f_date == l_date):
                                    spamwriter.writerow([row[0] , row[1] ,  1 , row[3] , row[4] ,  row[6] , row[5]])
                                else:
                                    delta = l_date - f_date 
                                    delta = str(delta).split(' ')
                                    delta = delta[0]
                                    if(int(row[5]) != 0):
                                        spamwriter.writerow([delta , row[1] , delta , row[3] , row[4] ,  row[6] , 1])
                                    else:
                                        spamwriter.writerow([delta , row[1] , delta , row[3] , row[4] ,  row[6] , row[5]])
        
    
    def formateQuPluie(self , CsvEntre , CsvSorti ):
        i = 0
        with open(CsvEntre, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            with open(CsvSorti, 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                for row in spamreader: 
                    if(i==0):
                        next(spamreader)
                        i += 1
                    elif(row[6] != '' and row[6] != ' '):
                        if(int(row[6]) != 0):
                            spamwriter.writerow([row[0] , row[1] , row[2] , row[3] , row[4] ,  row[5] , 1])
                        else:
                            spamwriter.writerow([row[0] , row[1] , row[2] , row[3] , row[4] ,  row[5] , row[6]])
        

    def supprimeLastCaract(self , CsvEntre , CsvSorti):
            with open(CsvEntre, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                with open(CsvSorti, 'w', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                    for row in spamreader: 
                        spamwriter.writerow([row[0] , row[1] ,  1 , row[3] , row[4] ,  row[5] ])






test = FormatData( "C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrain.csv" , "C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTest.csv" ,
"C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainSorti.csv" , "C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTestSorti.csv")


test.formateQuPluie("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainSorti.csv" ,"C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainSortiPluie1.csv" )


'''
test.decale("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrain.csv" , "C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainSorti.csv")
test.decale("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTest.csv" , "C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTestSorti.csv")


test.transformDate("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainSorti.csv" , "C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainSortiSortie.csv")
test.transformDate("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTestSorti.csv" , "C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTestSortiSortie.csv")

test.supprimeLastCaract("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainSortiSortie.csv" , "C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTrainFinale.csv")

test.supprimeLastCaract("C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTestSortiSortie.csv" , "C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\DataV2\\dataTestFinale.csv")'''
































































