from package.profitablePackage import dataTreat as dt

dataTreat = dt()

filePath: str = 'filesCSV/CSVfinale/final_data.csv'
data =  '/home/lasso/WebScrapper-A2T.ro/profitableProducts/profit.csv'

dataTreat.writeToCSV(data, filePath)