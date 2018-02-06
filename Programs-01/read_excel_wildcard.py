import glob
import xlrd
from xlrd.sheet import ctype_text

path = "C:/Users/MRSD/Downloads/"
file_name_wc = glob.glob('C:/Users/MRSD/Downloads/70109082_*.xls')
print(file_name_wc[0])

full_file_name = file_name_wc[0]

xl = xlrd.open_workbook(full_file_name)
sheet_names = xl.sheet_names()

print("Sheet Names", sheet_names)
first_sheet = xl.sheet_by_index(0)
print("First Sheet: " + first_sheet.name)

#row = first_sheet.row(0)
#print(row)

num_rows = first_sheet.nrows
num_cols = first_sheet.ncols

print("No of Rows : " + str(num_rows))
print("No of Columns : " + str(num_cols))

# List All Rows
#print(100*'=')
#for row_num in range(0,first_sheet.nrows):
#    print('%d - %s' % (row_num, first_sheet.row(row_num)))
#print(100*'=')

# List All Cells
#print(100*'=')
#for row_num in range(0,num_rows):
#    for col_num in range(0,num_cols):
#        cell = first_sheet.cell(row_num,col_num)
#        print('cell(%d,%d) - %s' % (row_num, col_num, cell))
#print(100*'=')

# List All Cells
print(100*'=')
for row_num in range(0,num_rows):
    for col_num in range(0,num_cols):
        cell = first_sheet.cell(row_num,col_num)
        cell_type = ctype_text.get(cell.ctype,'Unknown Type')
        cell_value = cell.value
        print('cell(%d,%d) = (type = %s, value = %s)' % (row_num, col_num, cell_type,cell_value))
print(100*'=')