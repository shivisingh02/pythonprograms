from pprint import pp 
movies = {}
movies['top gun: Maverick'] = 8.3
movies['everything everywhere all at once'] = 8.1
movies['spiderman'] = 8.2 
pp(movies)
print('only keys')
for item in movies:
    print(item)
print("keys and value")
for key in movies:
    print(key , movies[key] )

print('using dict.items() method')
for k, v in movies.items():
    print(k,v)

#user input 
for i in range(3):
    name = input("movie name")
    rating = float(input("enter rating: "))
    movies[name] = rating
print('using dict.items() method')
for k, v in movies.items():
    print(k,v)
