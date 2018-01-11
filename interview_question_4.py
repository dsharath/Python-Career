 def first_unique(string):
    l = len(string)             # intializing l as a length of string
	# checking all the characters in 'l'
	for p in range l:             
 	# # checking unique characters before and after the character. 
	    if string[p] in string[0:p] and string[p] in string[p+1:]: 
		    return None   # retruns None if there is no unique character
    print string[p] # prints the similar cahracters if they found
    return string[p] # Returns the similar characters if they found in the string.
