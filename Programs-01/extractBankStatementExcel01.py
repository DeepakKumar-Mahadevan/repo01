import xlrd
from xlrd.sheet import ctype_text

path = "C:/Users/MRSD/Downloads/"
file_name = input("Enter your input CSV file name:\n")
full_file_name = path + file_name

xl = xlrd.open_workbook(full_file_name)
sheet_names = xl.sheet_names()

print("Sheet Names", sheet_names)
first_sheet = xl.sheet_by_index(0)
print("First Sheet: " + first_sheet.name)

num_rows = first_sheet.nrows
num_cols = first_sheet.ncols

print("No of Rows : " + str(num_rows))
print("No of Columns : " + str(num_cols))

header_found = 'N'
txn_count = 0

# Read through all Rows/Columns/Cells
print(100*'=')
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
          print('Row number ' + str(row_num) + ' : ' + str(current_row))
          txn_count = txn_count + 1
          for col_num in range(0,num_cols):
              cell = first_sheet.cell(row_num,col_num)
              cell_type = ctype_text.get(cell.ctype,'Unknown Type')
              cell_value = cell.value
              print('cell(%d,%d) = (type = %s, value = %s)' % (row_num, col_num, cell_type,cell_value))
       if first_cell_type == 'text' and \
          first_cell_value == '\t':
          header_found = 'E'
    # Find header record and set flag
    if first_cell_value == 'SRL NO':
       header_found = 'Y'

print(100*'=')
print('No of txn records: ' + str(txn_count))