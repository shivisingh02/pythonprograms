#we can access individual items using indexing
#x[0] 
#negative indexing is also allowed
#slicing is also allowed in list
movies = ["sholay" , 'yjhd' ,'queen' ,'brielly ki barfi' , 'english vinglish' , 
'ready' ,'kal ho na ho' , 'znmd' ,'ddlj','tanu weds manu']
print(len(movies))
print(movies)
movies.sort() #sort does not work on mixed datatype list
print(movies) #sorting the list

movies.reverse() #reversing the list
print(movies) #list is updated after applying following functions

print("first movie",movies[0])
print(f"last movie {movies[-1]}")
print(f"first 3 movies {movies[:3]}")
print("all movies except first 3" , movies[3:])
print("movies at even index ",movies[::2])