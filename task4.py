n1 = int(input("enter the num of terms"))
n2 = int(input("enter the number of terms"))
x =[]
y =[]
for i in range(n1):
    s = int(input("enter num "))
    x.append(s)
for i in range(n2):
    s1 = int(input("enter num "))
    y.append(s1)
z =[]
for v , b in zip(x ,y):
    sum = v + b
    z.append(sum)
print(z)

#