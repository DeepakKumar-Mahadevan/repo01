import re

string="  FROM TQIBC02_BFM_CONNECTION ,TQIBF01_BFM_FACILITY."
print ("Input String :\n" + string)

rep = {" ":"|" , ",":"|" , ".": "|"} # define desired replacements here

rep = dict((re.escape(k), v) for k, v in rep.items())
pattern = re.compile("|".join(rep.keys()))
string = pattern.sub(lambda m: rep[re.escape(m.group(0))], string)

print ("Output String:\n" + string)