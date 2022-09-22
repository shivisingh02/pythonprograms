my_dict = {1: 'apple' , 2: 'ball'}
val_dict = {
    'employee' : 'Rajendra Singh' , 'age' : 30, 
    "experience" : 10 ,'dept': 'Accounts' ,
    'designation' : 'System officer' , "salary" : 60000,
    'team_size' : 7
}
print(val_dict)
#retreival of value
ans = val_dict['designation'] #key in square brackets 
print(ans)
# print(val_dict['Experience']) keyerror

#adding data in dictionary 
val_dict['company'] = 'Acme.inc'
print(val_dict)
from pprint import pp
pp(val_dict) #pp = pretty printing which displays the dictionary in pretty way 