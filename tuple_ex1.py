# #tuples are immutable during run time function like remove and append are not allowed
# when we want program to be dynamic we use list 
# tuple is pythons datatype
a = 1,2,3,4 #type => tuple
print(a)
print(type(a))
#trick
x , *y = 1,2,3,4,5 # * is important for multiple assignment to happen
print(x,y)
print(type(x) , type(y))
x = (1,2,3,4,5,6)
y = tuple([2,3,4,5,6]) #converting a list to tuple 
print(x ,y)
print(type(x), type(y))
