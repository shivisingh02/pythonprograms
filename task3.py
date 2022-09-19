#wap to take al ist of five names and display each name in reverse 
#wap to creat a fibonacci series using the concept of list (0 ,1, 1,2 ,3,5 ,8 ,11..)
#wap to generate a new list that contains the square of each number from existing list 
#wap to generate a new list from an existing list of numbers that contain only odd numbers 
#wap to generate a new list by adding 2 list elements  

#1
names =[]
for i in range(5):
    str = input("enter name: ")
    names.append(str)
for name in names:
    print(name[::-1])

#2
n = int(input("enter the num of terms"))
a = 0 
b = 1 
series = []
sum = a + b
series.append(sum)
for i in range(n-1):
    sum = a+b
    a = b
    b = sum
    series.append(sum)
print(series)

#3
num = []
x = int(input("enter num of terms"))
for i in range(x):
    y = int(input("enter the number: "))
    num.append(y)
sq =[]
for i , b  in enumerate(num):
    square = b*b
    sq.append(square)
print(sq)
    
#4
num = int(input("enter num of terms"))
x =[]
for i in range(num):
    n = int(input("enter the number: "))
    if not(n%2== 0):
        x.append(n)
print(x)






    
