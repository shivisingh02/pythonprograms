# #set tuple and list are interchangeable 
x = [1,2,3,4,5,5,6,7,7,7]
xt = tuple(x) #list converted to tuple
xl = list(xt) #tuple converted to list 
xs = set(x)  # list > set 
xst = set(xt) #tuple -> set 
print(x ,xs, xt, xl,xst)

# wap to creat a tuple taking ten inputs from user
x = []
for i in range(10):
      n =int(input("enter number: ") )
      x.append(n)
z = tuple(x)
print(z)
#slicing operation can be also performed on tuple
my_tuple = ('e' , 'x' ,'g', 'c','d')
print(my_tuple[1:4])
