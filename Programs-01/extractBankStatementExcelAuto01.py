import glob   #to do file name pattern search
import xlrd   #to read excel files
from xlrd.sheet import ctype_text
import datetime

#Function to get the Cell details based on row and column number.
def getCellDetails(row_num,col_num):
    cell = first_sheet.cell(row_num,col_num)
    cell_type = ctype_text.get(cell.ctype,'Unknown Type')
    cell_value = cell.value
    return (cell,cell_type,cell_value)

#Function to convert input date into ISO format.
def convertIsoDate(date_str):
    try:
         iso_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d") #DD/MM/YYYY to YYYY-MM-DD
    except ValueError:
         try:
              iso_date = datetime.datetime.strptime(date_str, "%d/%m/%y").strftime("%Y-%m-%d") #DD/MM/YY to YYYY-MM-DD
         except ValueError:
              try:
                   iso_date = datetime.datetime.strptime(date_str, "%d-%m-%Y").strftime("%Y-%m-%d") #DD-MM-YYYY to YYYY-MM-DD
              except ValueError:
                   try:
                        iso_date = datetime.datetime.strptime(date_str, "%d-%m-%y").strftime("%Y-%m-%d") #DD-MM-YY to YYYY-MM-DD
                   except ValueError:
                        iso_date = 'Invalid Date format'
    return(iso_date)
#===================================================================================================
# Process Axis bank statement file
op_mode = 'w' # Write mode
outfile = r'E:\Chicago_E_Drive\Deepak DOCs\Study\Python\Programs-01\out_message.txt'
f = open(outfile,op_mode)

f.write(100*'=')
file_name_wc = glob.glob('C:/Users/MRSD/Downloads/910010048748350*.xls') # Filename pattern search using glob
print(file_name_wc[0]) # Take 1st file name from the list

file_name = file_name_wc[0]

xl = xlrd.open_workbook(file_name)
sheet_names = xl.sheet_names()

f.write("\n" + "Sheet Names: " + str(sheet_names))
first_sheet = xl.sheet_by_index(0)
f.write("\n" + "First Sheet: " + first_sheet.name)

num_rows = first_sheet.nrows
num_cols = first_sheet.ncols

f.write("\n" + "No of Rows : " + str(num_rows))
f.write("\n" + "No of Columns : " + str(num_cols))

header_found = 'N'
firt_header_line_found = 'N'
txn_count = 0

# Read through all Rows/Columns/Cells
f.write("\n" + 70*'-')
for row_num in range(0,num_rows):
    # Get First Cell details for each row
    current_row = first_sheet.row(row_num)
    first_cell = first_sheet.cell(row_num,0)
    first_cell_type = ctype_text.get(first_cell.ctype,'Unknown Type')
    first_cell_value = first_cell.value

    # Once header is found extract the txn records
    if header_found == 'Y':
       if first_cell_type != 'text' and \
          first_cell_value != '\t':
          #print('Row number ' + str(row_num) + ' : ' + str(current_row))
          txn_count = txn_count + 1
          txn_date = ''
          txn_no = ''
          txn_desc = ''
          debit = ''
          credit = ''
          balance = ''
          
          (cell,cell_type,cell_value) = getCellDetails(row_num,1)
          txn_date = convertIsoDate(cell_value)

          (cell,cell_type,cell_value) = getCellDetails(row_num,2)
          txn_no = cell_value.strip()

          (cell,cell_type,cell_value) = getCellDetails(row_num,3)
          txn_desc = cell_value.strip()

          (cell,cell_type,cell_value) = getCellDetails(row_num,4)
          debit = cell_value.strip()

          (cell,cell_type,cell_value) = getCellDetails(row_num,5)
          credit = cell_value.strip()

          (cell,cell_type,cell_value) = getCellDetails(row_num,6)
          balance = cell_value.strip()

          #print('(txn_date,txn_no,txn_desc,debit,credit,balance) = (%s,%s,%s,%s,%s,%s)' % (txn_date,txn_no,txn_desc,debit,credit,balance))
          f.write("\n" + '%s|%s|%s|%s|%s|%s' % (txn_date,txn_no,txn_desc,debit,credit,balance))

       # Empty line (tab) after the txn records
       if first_cell_type == 'text' and \
          first_cell_value == '\t':
          header_found = 'E'
    # Find header record and set flag
    if first_cell_value == 'SRL NO':
       header_found = 'Y'
       f.write("\n" + 'txn_date|txn_no|txn_desc|debit|credit|balance')

f.write("\n" + 70*'-')
f.write("\n" + 'No of txn records: ' + str(txn_count))
f.write("\n" + 100*'=')

f.close()
#===================================================================================================
# Process HDFC bank statement file
op_mode = 'a'
outfile = r'E:\Chicago_E_Drive\Deepak DOCs\Study\Python\Programs-01\out_message.txt'
f = open(outfile,op_mode)

f.write(100*'=')
file_name_wc = glob.glob('C:/Users/MRSD/Downloads/70109082*.xls')
print(file_name_wc[0])

file_name = file_name_wc[0]

xl = xlrd.open_workbook(file_name)
sheet_names = xl.sheet_names()

f.write("\n" + "Sheet Names: " + str(sheet_names))
first_sheet = xl.sheet_by_index(0)
f.write("\n" + "First Sheet: " + first_sheet.name)

num_rows = first_sheet.nrows
num_cols = first_sheet.ncols

f.write("\n" + "No of Rows : " + str(num_rows))
f.write("\n" + "No of Columns : " + str(num_cols))

header_found = 'N'
firt_header_line_found = 'N'
txn_count = 0

# Read through all Rows/Columns/Cells
f.write("\n" + 70*'-')
for row_num in range(0,num_rows):
    # Get First Cell details for each row
    current_row = first_sheet.row(row_num)
    first_cell = first_sheet.cell(row_num,0)
    first_cell_type = ctype_text.get(first_cell.ctype,'Unknown Type')
    first_cell_value = first_cell.value


    # Once header is found extract the txn records
    if header_found == 'Y':
       if first_cell_type != 'empty':
          #print('Row number ' + str(row_num) + ' : ' + str(current_row))
          txn_count = txn_count + 1
          txn_date = ''
          txn_no = ''
          txn_desc = ''
          debit = ''
          credit = ''
          balance = ''
          
          (cell,cell_type,cell_value) = getCellDetails(row_num,0)
          txn_date = convertIsoDate(cell_value)
    
          (cell,cell_type,cell_value) = getCellDetails(row_num,2)
          txn_no = cell_value.strip()
    
          (cell,cell_type,cell_value) = getCellDetails(row_num,1)
          txn_desc = cell_value.strip()
    
          (cell,cell_type,cell_value) = getCellDetails(row_num,4)
          debit = cell_value
    
          (cell,cell_type,cell_value) = getCellDetails(row_num,5)
          credit = cell_value
    
          (cell,cell_type,cell_value) = getCellDetails(row_num,6)
          balance = cell_value
    
          #print('(txn_date,txn_no,txn_desc,debit,credit,balance) = (%s,%s,%s,%s,%s,%s)' % (txn_date,txn_no,txn_desc,debit,credit,balance))
          f.write("\n" + '%s|%s|%s|%s|%s|%s' % (txn_date,txn_no,txn_desc,debit,credit,balance))
    
       # Blank line after the txn records
       if first_cell_type == 'empty':
          header_found = 'E'
          firt_header_line_found = 'E'
    # Find header record and set flag
    if firt_header_line_found == 'Y':
       if first_cell_value == '********': #Second Header
          header_found = 'Y'
          f.write("\n" + 'txn_date|txn_no|txn_desc|debit|credit|balance')
    if first_cell_value == 'Date': #First Header
       firt_header_line_found = 'Y'

f.write("\n" + 70*'-')
f.write("\n" + 'No of txn records: ' + str(txn_count))
f.write("\n" + 100*'=')

f.close()
#===================================================================================================