import csv

#with open('E:\Chicago_E_Drive\Deepak DOCs\Study\Data Analytics\Sample_Data\BPL.csv') as csvDataFile:
#with open(r'C:\Users\MRSD\Downloads\910010048748350.csv') as csvDataFile:
with open(r'C:\Users\MRSD\Downloads\70109082_1514533688675.txt') as csvDataFile:

    csvReader = csv.reader(csvDataFile)
    print ("Looping...")
    for row in csvReader:
        if len(row) != 0:    
           print(row)
           print(row[0])
           print(row[1])
           print(row[0],row[2],row[1])
    print ("End Loop!")
    if len(row) != 0:    
       print (row[0])
       print (row)