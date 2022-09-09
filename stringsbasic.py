#defining strings in python 
#all of the following are equivalent
my_string = 'Hello'
print('my_string')
my_string = "Hello"
print(my_string)
my_string = '''Hello'''
print(my_string)
#triple quotes strings can extend to multiple lines
my_string = """hello welcome to the
world of python"""
print(my_string)
a = "excalibur"
print(a[0])#first character
print(a[2] ) #third character
print(a[-1]) #last character
print(a[-3])  #third last character

#slicing string
name = "vijay deenanath chauhan"
print(name[6 : -8])
print(name[:5]) #ommiting the starting index
for i,c in enumerate(name):
    print(i , c)
print(name[-7:]) #ommiting the ending index
print(name[-12:-8]) #nath 
#reverse the string
print(name[::-1])
print(name[:5][ : : -1]) #only reverses a part of string
#every even index character
print(name[:: 2])
#every odd index character
print(name[1::2])
x = chr(65)
print(x)
x = chr(2365)
print(x)
x = chr(12365)
print(x)
x = ord('A')
print(x)
x = ord('a')
print(x)
x = ord('{')
print(x)
a = 'this'
b = 'is'
c = 'amazing'
msg = a + b + c
msg2 =a + ' ' + b +" " + c+ ' '
print(f'{msg} and {msg2}')
#strings can be duplicated
print('hi '*5)
print('__'*7)