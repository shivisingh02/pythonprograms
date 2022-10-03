#default parameter must come after required parameters 
def total(a , b = 3 , c = 0): #a if default parameter 
    return a + b + c 

#named parameters must come after positional parameter 
print(total(5))
print(total(a = 5))
print(total(100, 50))
print(total(a = 100 , b= 50))
print(total(b = 50 , a = 100)) #swapped and working 

print(total(10,10,10))

#polymorphism  
#unlimited number of parameters can be passed in a function 

  #parameters will be handles as tuple 
  # #* means multiple values 

def mean(*numbers):
    print(numbers)
    print(type(numbers))
mean(1,2,3,4)

def means(*numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
print(means(1,2,3,4,5))
print(means(1,2,3,4,333,45,66,5,67))
print(mean())

#keyword arguments 
#def marks(**Kwargs): #to pass unlimited number of parameters 

