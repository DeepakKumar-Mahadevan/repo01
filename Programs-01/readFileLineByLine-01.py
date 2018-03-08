#with open("E:/Chicago_E_Drive/Deepak DOCs/Study/Python/Programs-01/testTableUsage-01.txt") as f:
with open(r'E:\Chicago_E_Drive\Deepak DOCs\Study\Python\Programs-01\testTableUsage-01.txt') as f:
    for line in f:
        print (line)
		
import io
#with open('E:/Chicago_E_Drive/Deepak DOCs/Study/Python/Programs-01/testTableUsage-01.txt','rt',newline='') as f:
with io.open(r'E:\Chicago_E_Drive\Deepak DOCs\Study\Python\Programs-01\testTableUsage-01.txt', 'rt', newline='') as f:
    for line in f:
        print (line)