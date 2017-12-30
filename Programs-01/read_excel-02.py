import xlrd

#rd = xlrd.open_workbook("file:///E:\Chicago_E_Drive\Deepak%20DOCs\Study\Data%20Analytics\Sample_Data\ManUtdPlayers.xlsx")
#rd = xlrd.open_workbook(r"E:\Chicago_E_Drive\Deepak%20DOCs\Study\Data%20Analytics\Sample_Data\ManUtdPlayers.xlsx")
rd = xlrd.open_workbook(r"E:\Chicago_E_Drive\Deepak DOCs\Study\Data Analytics\Sample_Data\ManUtdPlayers.xlsx")

op = rd.sheet_by_index(0).cell(0,0).value

print("Output: " + op)