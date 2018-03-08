import re

s1 = "  FROM|TQIBC02_BFM_CONNECTION|| ,TQIBF01_BFM_FACILITY"
os = re.search(r'(?<=\|TQI)(.*?)(?=\|)',s1)
if os:
   print (os.group(1))
else:
   print ("String not found")
   
os = re.search(r'\|TQI(.*)\|',s1)
if os:
   print (os.group(1))
else:
   print ("String not found")

# End of Line
s2 = "  FROM|TQIBF01_BFM_FACILITY"
os = re.search(r'\|TQI(.*)$',s2)
if os:
   print (os.group(1))
else:
   print ("String not found")

os = re.search(r'(?<=\|TQI)(.*)(?=\|)',s2)
if os:
   print (os.group(1))
else:
   print ("String not found")

# Start of Line
s3 = "TQIBC09_BFM_CUSTOMER|BC09"
os = re.search(r'^TQI(.*)\|',s3)
if os:
   print (os.group(1))
else:
   print ("String not found")

os = re.search(r'(?<=\|TQI)(.*)(?=\|)',s3)
if os:
   print (os.group(1))
else:
   print ("String not found")

# Start & End of Line
s4 = "|TQIBC05_BFM_CONNECTION_CUSTOMER"
os = re.search(r'^TQI(.*)$',s4)
if os:
   print (os)
   print (os.group(1))
else:
   print ("String not found")

os = re.search(r'(?<=\|TQI)(.*)(?=\|)',s4)
if os:
   print (os)
   print (os.group(1))
else:
   print ("String not found")

os = re.search(r'\|TQI(.*)(?=(\||([A-Z]|[0-9])$))',s4)
if os:
   print (os)
   print(os.group(0))
   print (os.group(1))
else:
   print ("String not found")