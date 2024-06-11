from package.profitablePackage import dataTreat as dt

dataTreat = dt()

filePath: str = 'filesCSV/CSVfinale/final_data.csv'

data = dataTreat.sortByPriceDifference(filePath)

for x in data:
    print(x)
