import random
clearMes = raw_input("Enter a message to be encrypted:\n> ") 


alphabet = [' ' ,'a', 'b', 'c', 
			'd', 'e', 'f', 
			'g', 'h', 'i', 
			'j', 'k', 'l', 
			'm','n', 'o',
			'p', 'q', 'r', 
			's', 't', 'u',
			'v', 'w', 'x', 
			'y', 'z', 'A', 
			'B', 'C', 'D', 
			'E', 'F', 'G', 
			'H', 'I', 'J', 
			'K', 'L', 'M', 
			'N', 'O', 'P', 
			'Q', 'R', 'S', 
			'T', 'U', 'V', 
			'W', 'X', 'Y', 
			'Z']
			
clearMesList = []
numList = []

#Puts all characters in the clear message into a list 
for x in clearMes:
	clearMesList.append(x)

#Compares clear list to alphabet
for x in clearMesList:
	y = 1
	
	#Checks to see if message character is equal to alphabet letter 
	while x != alphabet[y]:
		y = y + 1
		#If the character is not a letter, then it is represented by a 0
		if y > 52:
			y = 0
			break
	#Adds now converted character to numList 
	numList.append(y)

numList2 = [] 
encryptionKey = random.randint(1,500)
#Does math to all the coverted characters
for x in numList:
	x = x + 1000
	x = x * 17
	x = x + 23
	x = x - 743
	x = x + encryptionKey
	x = x + encryptionKey/2
	numList2.append(x)
	

y = 0 
#Converts all ints in numList2 into strings
for x in numList2:
	numList2[y] = str(numList2[y])
	y = y+1


#Joins all numbers in a list into a string 
encryptedstring = "".join(numList2)

print "\nEncrypted message:\n" + encryptedstring

encryptionKey = str(encryptionKey)
print "Your encryption key is: " + encryptionKey 






