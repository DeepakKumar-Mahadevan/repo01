#from __future__ import print_function
outfile = r'E:\Chicago_E_Drive\Deepak DOCs\Study\Python\Programs-01\out_message.txt'
#print >> outfile, 'This is a test message'

f = open(outfile,'w')
f.write('This is a test message')
f.close()