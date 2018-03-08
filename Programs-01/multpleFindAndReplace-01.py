string="  FROM TQIBC02_BFM_CONNECTION ,TQIBF01_BFM_FACILITY."
print ("Input String :\n" + string)
repl_str = '|'
for ch in [' ',',','.']:
   if ch in string:
      string=string.replace(ch,repl_str)
print ("Output String:\n" + string)