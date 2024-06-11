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
           if len(product) >= 4:
                try:
                    product[-2] = float(product[-2])
                    product[-1] = float(product[-1])
                except:
                    None
        return prodArray
    
    def addPriceDifference(self, path) -> list:
        prodArray: list = []
        prodArray = self.convertPriceString(path)
        for product in prodArray:
            try:
                product.append.round((product[-2] - product[-1]))
            except:
                None
        return prodArray

    def sortByPriceDifference(self, path) -> list:
        prodArray: list = []
        prodArray = self.addPriceDifference(path)
        for product in prodArray:
            try:
                prodArray.sort(key=lambda x: x[-1], reverse=True)
            except:
                None
        return prodArray