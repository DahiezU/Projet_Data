import csv
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

def  decale():
    with open('C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\AclabProjet\\Donnees\\dataEssai.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        with open('C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\AclabProjet\\Donnees\\resDonne.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='', quoting=csv.QUOTE_MINIMAL)
            for row in spamreader: 
                    row  = row[0].split(',') 
                # print(len(row))
                    #print(row[0])
                    spamwriter.writerow( [row[0] + ',' , row[1] + ',', row[2] + ',', row[3] + ',', row[4]+ ','  , row[6] + ',', row[5]])








def transformDate(CsvEntre , CsvSorti):
     with open(CsvEntre, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        with open(CsvSorti, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            for row in spamreader: 
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





'''f_date = date(2020, 1, 1)
l_date = date(2020, 1, 1)
delta = l_date - f_date 
print(delta)

date_time_str = '18/09/19 01:55:19'

date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')



res = '2019-01-23T01:54:31.000+0200'
print(delta.days)
'''




dataEntre =  'C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\transfome\\dataTestConvert.csv'
dataSortie = 'C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\transfome\\dateSortie.csv


'''dataEntre =  'C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\transfome\\dataTrainPetit.csv'
dataSortie = 'C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\Projet_Data\\transfome\\datetrainPetitOk.csv' '''


'''transformDate(dataEntre , dataSortie)'''

transformDate(dataEntre , dataSortie)

