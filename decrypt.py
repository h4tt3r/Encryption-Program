hiddenMes = raw_input("Enter a message to decrypt:\n> ")
enKey = raw_input("What is your encryption key?\n> ")

enKey = int(enKey)

#Function to split a string into pairs of 5's 
def by5(s):
    out = []
    while len(s):
        out.insert(0, s[-5:])
        s = s[:-5]
    return out

#Splits string into 5's and adds it to numList
numList = by5(hiddenMes)






alphabet = [' ', 'a', 'b', 'c', 
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

#Does reverse math of encrypt.py		
numList2 = []
y = 0
for x in numList:
	x = int(x)
	x = x - enKey 
	x = x - enKey/2
	x = x + 743
	x = x - 23 
	x = x / 17
	x = x - 1000
	
	numList2.append(x)


clearMesList = []
for x in numList2:
	y = 1
	
	#Checks to see if number is equal to number of a certain letter in alphabet list
	while x != y:
		y = y + 1
		#If its a space, add a space
		if y > 52:
			y = 0
			break
	#Adds new letter based on what number x was equal to, as it was the corresponding number-
	#for the one in the alphabet list 
	clearMesList.append(alphabet[y])

#Joins them together into a string
clearmessage = "".join(clearMesList)



print "Decrypted Message:\n" + clearmessage
	


