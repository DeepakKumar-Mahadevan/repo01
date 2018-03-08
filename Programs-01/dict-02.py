num = {1:'A',2:'B',3:'C'}
print (num.items())
num[4] = 'D'
num[5] = 'E'
print (num.items())
num[6] = 'F'
num[7] = 'G'
num[8] = 'H'
num[9] = 'I'
num[10] = 'J'
print (num.items())
del num[6]
del num[8]
print (num.items())