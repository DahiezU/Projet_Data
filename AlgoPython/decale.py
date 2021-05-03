import csv
with open('C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\AclabProjet\\Donnees\\dataEssai.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    with open('C:\\Users\\sburd\\OneDrive\\Bureau\\Semestre2\\AclabProjet\\Donnees\\resDonne.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in spamreader: 
                row  = row[0].split(',') 
               # print(len(row))
                #print(row[0])
                spamwriter.writerow( [row[0] + ',' , row[1] + ',', row[2] + ',', row[3] + ',', row[4]+ ','  , row[6] + ',', row[5]])
        