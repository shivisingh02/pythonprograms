#1 
str = "hello world"
print(str)
#2
str = input("enter string : ")
print(len(str))
#3
str= "Python is great"
print(str[10:])
#4
str = "hello world"
print(str[::-1])
#5 
str = "How are you?"
print(str.upper())
#6
str = "How Is It Going?"
print(str.lower())
#8
words = ["Python" , "is" , "to" , 'easy ','learn']
str=''
for i , d  in enumerate(words):
    str = str + " " + d
print(str)
#9
print("Hi my name is Shivi\nI want to study Python\nI study at RRIMT" )
#10
str = """to move to newline '\n' is used"""
print(str)
#11
n  = 15 
print(f'the variable is {n}')
#12
s1 = 'python'
s2 = 'is'
s3 = 'great'
str = s1 + ' ' + s2 + " " + s3
print(str)
#13 
str = "#" * 20
print(str)
#14 
for i in range(1 , 10):
    print(f'{i}. \n')
#15
str = input("enter string: ")
str = str + " "
s =""
for i in range(len(str)):
    if str[i] == " ":
        print(s)
        print("\n")
        s = ""
    else:
        s = s + str[i] 
#16 
str = input("enter string :")
n = len(str)
if str[n-1] == "?":
    print('true')
else:
    print("false")
#17
str = input('enter string :')
print(str.count("e"))
#18
str = input("enter num: ")
if str.isnumeric():
    print("yes")
else:
    print("no")
#19 
text = "     this is not a good string     "
print(text.strip())
#20
str = input("enter string: ")
for i in range(len(str)):
    if str[i].upper():
        print("found")
        break
#21
name = "Joe, Mark, David, Tom, Chris, Robert"
name = name + ","
str =[]
names = ""
for i in range(len(name)):
    if name[i] == ",":
        names.strip()
        str.append(names)
        names = ""
    else:
        names = names + name[i]    
print(str)
#22
text = 'this is some  text'
text = text + " "
text_updated = ""
x = ""
for i in range(len(text)):
    if text[i] == " ":
        s = s + "aye"
        text_updated = text_updated + " " + s
        s = ""
    else:
        s = s + text[i]
print(text_updated)
#23
str = input("enter string : ")
idx = str.find('fyi')
if idx >= 0:
    print('found')
else:
    print('not found')
#24
str = '%p32@!*_*!t68h#&on202'
from string import punctuation 
for marks in punctuation:
    str = str.replace(marks , '')
print(str)
#25
text = "this is a paragraph which is written just for the purpose of providing to let the average word length be calculated"
text = text + " "
sum = 0 
str = ""
f = 0
for i in range(len(text)):
    if text[i] == " ":
        sum = sum + len(str)
        str = ""
        f =  f+1
    else:
        str = str+text[i]
avg = sum//f
print("average word length = " , avg) 

        

    
