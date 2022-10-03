class cat:
#constructor 
    def __init__(self ,name , age , breed): #self refers to a]the class itself(cat)
        #syntax instance_variable 
        #self.<attribute> <parameter>
        self.name = name 
        self.age = age 
        self.breed = breed 

cat1 = cat('soni' , 2 , 'persian')
cat2 = cat('mia' , 2 , 'siamese')

print(cat1.name , cat1.age ,cat1.breed)