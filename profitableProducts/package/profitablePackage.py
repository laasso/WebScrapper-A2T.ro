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
                product.append(product[-2] - product[-1])
            except:
                None
        return prodArray

    def sortByPriceDifference(self, path) -> list:
        prodArray: list = []
        prodArraySort: list = []
        prodArray = self.addPriceDifference(path)
        valid_products = []
        for product in prodArray:
            if len(product) >= 4:
                try:
                    if isinstance(product[-1], (int, float)) and product[-1] >= 0:
                        valid_products.append(product)
                except TypeError:
                    print(f"Non-iterable value found at position: {product[-1]}")
        prodArraySort = sorted(valid_products, key=lambda x: x[-1], reverse=True)
        return prodArraySort
