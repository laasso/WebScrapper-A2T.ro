from package.profitablePackage import dataTreat as dt

dataTreat = dt()

filePath: str = 'filesCSV/CSVfinale/final_data.csv'

data = dataTreat.convertPriceString(filePath)

for x in data:
    print(x)
