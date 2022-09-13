msg = "We will be seeing the horizon"

words = msg.split()
print(words)
words = msg.split('e') #splits the words from given string 
print(words)
updatedmsg = msg.replace('seeing' , 'viewing')
print(updatedmsg)
updatesmsg = msg.replace('e', " ")
print(updatesmsg)
#join function
path = ['users' , 'mypc' , 'documents' , 'data']
updatemsg = " ".join(path) #used to join together the elements in the list 
print(updatemsg)
#strip()
name = "   giva   is here   now   "
print(name.strip()) #removes extra space from the givens tring 
# does not remove extra spaces between the given words
print(len(name)) #length of the string
msg2 = name.replace(" ", "  ")
print(msg2)

#wap to find all the vowels in the file

