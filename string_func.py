#formatting functions 
# - lower
#upper
#swapcase
#capatilize
#title 
#casefold
#ljust
# center 
#rjust

str = 'this is my house is '
num = 7847
print(str.upper())
print(str.lower())
print(str.swapcase())
print(str.capitalize())
print(str.title())
print(str.casefold()) #same as lower case
word = 'hello'
spacing = 20
#allignment fucntions
ljust = word.ljust(spacing,)  #left allignment
print(ljust)
rjust = word.rjust(spacing,'💀')  #right allignment 
print(rjust) #emoji shortcut windows + .
cen = word.center(spacing,'*')  #center alligned
print(cen)
#validation functions return is either true or false
print(str.isupper())
print(str.islower())
print(str.isalpha()) #since space is present and it is a special character the ans is false
print(str.isnumeric())
print(str.isalnum())
print(str.isdigit())
 #utility functions
idx = str.find('this')
if idx == -1: #THIS HANDLES THE ERROR IN CASE THE WORD IS NOT FOUND FOR THE USER TO UNDERSTAND
    print('not found')
else:
    print(f'''this was
    found at {idx}''')
idx2 = str.index("this")
print(idx2)
start_idx = 0 
for i in range(5):
    idx3 = str.find(' is ' , start_idx) #start finding from the given index
    print(f'is was found at {idx3}')
    start_idx = idx3 + 1
num_of_is = str.count(' is ')  #count the number of times a certain word has occured in a string
print(f'is occurs {num_of_is} times')


