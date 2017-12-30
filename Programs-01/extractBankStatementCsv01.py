import csv
path = "C:/Users/MRSD/Downloads/"
inCsvFile = input("Enter your input CSV file name:\n")

header_found = 'N'
txn_count = 0

with open(path + inCsvFile) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    print ("====================================================================================================")
    for row in csvReader:
        if header_found == 'Y':
           if len(row) != 0:
              print(row)
              txn_count = txn_count + 1
           if len(row) == 0:
              header_found = 'E'
        if len(row) != 0:
           if row[0] == 'Tran Date':
              header_found = 'Y'
    print ("====================================================================================================")
    print ("No of txn records: " + str(txn_count))