import datetime

str = input("Enter date as a string :\n")

try:
     out_date = datetime.datetime.strptime(str, "%d/%m/%Y").strftime("%Y-%m-%d")
except ValueError:
     try:
          out_date = datetime.datetime.strptime(str, "%d/%m/%y").strftime("%Y-%m-%d")
     except ValueError:
          try:
               out_date = datetime.datetime.strptime(str, "%d-%m-%Y").strftime("%Y-%m-%d")
          except ValueError:
               try:
                    out_date = datetime.datetime.strptime(str, "%d-%m-%y").strftime("%Y-%m-%d")
               except ValueError:
                    out_date = 'Invalid Date format'

print(out_date)