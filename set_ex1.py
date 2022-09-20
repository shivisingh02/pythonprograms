# a set is an unordered collection of data 
# there are no duplicates Value
# they can perform mathematical operation like union , intersection 
# a set itself is mutable , we can add or remove items
# it can have mixed datatype items  
my_set = {1,2,3,4,5,6} 
print(my_set)
my_set = set([1,2,3,4,5,6]) #we can make set from list 
print(my_set)
# my_set = {1,2,3,[1,4,5,6]} #set cannot have mutable items and list here is one. 
# therefore, there will be error
# print(my_set)

a = set() #to create empty set
for i in range(5):
    a.add(int(input("enter num: "))) #adds only on item to a list at time
print(a)
a.update([2,3,4,5,6]) #to add multiple items to set
print(a)
a.update([1,2] , {1,3,4,6,6}) #to add list and set together to the set a 
print(a)
a.discard(4) #removes the given item from set
print(a)
a.pop()#removes a random item from set
print(a)
a.clear()
print(a)