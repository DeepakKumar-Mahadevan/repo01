import re

# Function to replace spaces, commas, dots with Pipes
def format_line(f_line):
    repl_str = '|'
    for ch in [' ',',','.']: #Characters to be replaced
        if ch in f_line:
           f_line=f_line.replace(ch,repl_str)
    f_line = "|" + f_line + "|" #Prefix $ Suffix | for regex to work
    return(f_line)

with open(r'E:\Chicago_E_Drive\Deepak DOCs\Study\Python\Programs-01\testTableUsage-01.txt') as f:
    for line in f:
        line = line.strip('\n') # Remove line feed
        #print("Input :" + line)
        o_line = format_line(line)
        #print("Format:" + o_line)
        # Extract string in between |TQI & |
        find_str = re.search(r'(?<=\|TQI)(.*?)(?=\|)',o_line)
        if find_str:
           print ("TQI" + find_str.group(1))
        #else:
        #   print ("String not found : " + line)