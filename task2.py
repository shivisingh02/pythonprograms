print("enter 10 numbers")
num = []
sum = 0
for i in range(10) :
    n = int(input())
    num.append(n)
    sum = sum + n
num.sort()
mean = sum/10
median = (num[5] + num[6])/2
print("sum of numbers =",sum)
print("mean =", mean)
print("median of numbers = ",median)
mode = 0
f = 0
for x in num:
    counter = num.count(x)
    if(mode < counter):
        mode = counter 
        f = x
print("mode =",f)


