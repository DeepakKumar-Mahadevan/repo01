digits = [0,1,2,3,4,5,6,7,8,9]
alphabets = ['A','B','C','D','E']

print ("print (digits) :",(digits))
l_digits = len(digits)
print("len(digits) = ",l_digits)

print ("print (alphabets) :",(alphabets))
l_alphabets = len(alphabets)
print("len(alphabets) = ",l_alphabets)

#alphabets[l_alphabets+1] = 'F'
#alphabets[len(alphabets)+1] = 'G'
print(">>> Appending F,G,J")
alphabets.append('F')
alphabets.append('G')
alphabets.append('J')
print ("print (alphabets) : len(alphabets) =",alphabets,":",len(alphabets))

print(">>> Inserting H,I & K (at end)")
alphabets.insert(7,'H')
alphabets.insert(8,'I')
alphabets.insert(len(alphabets),'K')
print ("print (alphabets) : len(alphabets) =",alphabets,":",len(alphabets))

more_aplhabets = ['L','M','N']
print ("print (more_aplhabets) : len(more_aplhabets) =",(more_aplhabets),":",len(more_aplhabets))
print(">>> Extending alphabets with more_aplhabets")
alphabets.extend(more_aplhabets)
print ("print (alphabets) : len(alphabets) =",alphabets,":",len(alphabets))

last_3_aplhabets = ['X','Y','Z']
print ("print (last_3_aplhabets) : len(last_3_aplhabets) =",(last_3_aplhabets),":",len(last_3_aplhabets))
print(">>> Extending alphabets with last_3_aplhabets")
alphabets.extend(last_3_aplhabets)
print ("print (alphabets) : len(alphabets) =",alphabets,":",len(alphabets))

missing_aplhabets = ['O','P','Q','R','S','T','U','V','W']
print ("print (missing_aplhabets) : len(missing_aplhabets) =",(missing_aplhabets),":",len(missing_aplhabets))
print(">>> Extending alphabets with missing_aplhabets")
alphabets.extend(missing_aplhabets)
print ("print (alphabets) : len(alphabets) =",alphabets,":",len(alphabets))

#sorted_aplhabets = alphabets.sort()
#print ("print (sorted_aplhabets) : len(sorted_aplhabets) =",(sorted_aplhabets),":",len(sorted_aplhabets))
print(">>> Sorting alphabets")
alphabets.sort()
print ("print (alphabets) : len(alphabets) =",alphabets,":",len(alphabets))

print ("alphabets @ Position 4,5,5,16,1,11 =",alphabets[3] + alphabets[4] + alphabets[4] + alphabets[15] + alphabets[0] + alphabets[10])

print(">>> Removing 'H' and Poping 13th element")
alphabets.remove('H')
alphabets.pop(13)
print ("print (alphabets) : len(alphabets) =",alphabets,":",len(alphabets))

print(">>> Reversing digits")
digits.reverse()
print ("print (digits) : len(digits) = ",digits,":",l_digits)

print(">>> Poping last element")
alphabets.pop()
print ("print (alphabets) : len(alphabets) =",alphabets,":",len(alphabets))

print(">>> Searching for 'R'")
print ("'R' is found at ",alphabets.index('R'))

print(">>> Slicing 0 to 9 elements")
print (alphabets[0:9])
print(">>> Slicing 10 to 2nd element from last")
print (alphabets[10:-2])
print(">>> Slicing 0 to 9 elements skipping by 2")
print (alphabets[0:9:2])

print(">>> Replacing elements 11 to 15 with 'Z' ")
alphabets[11:15] = 'Z'
print ("print (alphabets) : len(alphabets) =",alphabets,":",len(alphabets))

print(">>> Deleting last 3 elements")
del alphabets[-3:]
print ("print (alphabets) : len(alphabets) =",alphabets,":",len(alphabets))
print(">>> Deleting 5th element")
del alphabets[5]
print ("print (alphabets) : len(alphabets) =",alphabets,":",len(alphabets))
print(">>> Deleting first 9 elements")
del alphabets[0:9]
print ("print (alphabets) : len(alphabets) =",alphabets,":",len(alphabets))

print(">>> Copying all elements to another list")
alphabets_copy = alphabets[:]
print ("print (alphabets) : len(alphabets) =",alphabets,":",len(alphabets))
print ("print (alphabets_copy) : len(alphabets_copy) =",alphabets_copy,":",len(alphabets_copy))