import numpy as np
import csv

def monTest(ver):
    
    with open(ver, "r",newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
        
        
        return spamreader


#monTest("C:\\Users\\dahie\\Documents\\SDN-S6\\Projet_Data\\Donnees\\Entrainement\\dataEssai.csv")