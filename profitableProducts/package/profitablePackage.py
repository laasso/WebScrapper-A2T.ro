import os
import csv

class dataTreat:

    def readCsv(self, path) -> list:
        prodArray: list = []
        with open(path, newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader) 
            for row in reader:
                prodArray.append([(x) for x in row]) 
        return prodArray


    def convertPriceString(self, path) -> list:
        prodArray: list = []
        prodArray = self.readCsv(path)
        for product in prodArray:
            for attribute in product:
                product[-2:] = float(attribute[-2:])
        return prodArray


