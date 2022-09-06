for i in range(100):
    print(i, end = ', ')
print("\n")
#range with starting limit 
for i in range(10 ,21):
    print( i , end = ',, ')
print(" \n")
#gap in range
for i in range(1 ,10 , 2):
    print(i , end=",,, ")
print('\n')
#reverse loop
for i in range(10 , 0 , -1):
    print(i , end=", ")
print('\n')
#enumerate function
data = [2,3,4,3,6,4,69,6]
for i ,d in enumerate(data):
    print(i)
for i , d in enumerate(data):
    print(i)
for i , d in enumerate(data):
    print(d)
print("\n") 
#zip function
fruits = ['apple' , 'kiwi' , 'banana' , 'cherry']
price = [23,34,56,56]
for f , p in zip(fruits , price):
    print(f , p)
