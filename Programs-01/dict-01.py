mrsdvapm = {}
mrsdvapm['Mahadevan'] = '1955-09-07'
mrsdvapm['Radha'] = '1962-02-19'
mrsdvapm['Shiva'] = '1986-08-30'
mrsdvapm['Deepak'] = '1988-10-13'
mrsdvapm['Vaishali'] = '1988-10-22'
mrsdvapm['Priya'] = '1991-07-18'
mrsdvapm['Arjun'] = '2014-09-22'
mrsdvapm['Mithran'] = '2018-01-06'

print (100*"=")
print ("dict: print (mrsdvapm)")
print (30*"-")
print (mrsdvapm)
print (100*"=")

print ("keys: print (mrsdvapm.keys())")
print (30*"-")
print (mrsdvapm.keys())
print (100*"=")

print ("values: print (mrsdvapm.values())")
print (30*"-")
print (mrsdvapm.values())
print (100*"=")

print ("items: print (mrsdvapm.items())")
print (30*"-")
print (mrsdvapm.items())
print (100*"=")

print ("based on key: print (k,',',mrsdvapm[k])")
print (30*"-")
for k in sorted(mrsdvapm.keys()):
    print (k,',',mrsdvapm[k])
print (100*"=")

print ("key and value: print (k + '=' + v)")
print (30*"-")
for k, v in mrsdvapm.items():
    print (k + '=' + v) 
print (100*"=")

print ("Count : len(mrsdvapm) = " , len(mrsdvapm))
print (100*"=")