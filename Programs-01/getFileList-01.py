import glob   #to do file name pattern search

files_list = glob.glob('C:/Users/MRSD/Downloads/File*.txt') # Filename pattern search using glob

print("No of Files : ",len(files_list))

for f in range(len(files_list)): #Range starts from 0 to n-1)
    print(files_list[f])
#print(files_list)
#print(files_list[0]) # Take 1st file name from the list
#file_name = file_name_wc[0]