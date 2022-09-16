books = ['steelheart' ,'touch of eternity' ,'good girl guide to murder' ,'red white and royal blue'
,'love hypothesis','it ends with us' , 'alchemist']
movies = ["sholay" , 'yjhd' ,'queen' ,'brielly ki barfi' , 'english vinglish' , 
'ready' ,'kal ho na ho' , 'znmd' ,'ddlj','tanu weds manu']
books.append('atomic habit') #append function to add items to list
books.append('pride and predujice') #only adds one item at a time
books.append('you can win')
print(books)
print("idx \t bookname")
for i , b in enumerate(books):
    print(f'{i} \t {b}')
 #to update the list at particular index
books[6] = "history"
print(books)
#to insert the item without removing the item
books.insert(3,' geo' )
books.insert(5,"elantris")
print(books)
print("idx \t bookname")
for i , b in enumerate(books):
    print(f'{i} \t {b}')
#to delete item from the list
books.remove(" geo")
books.remove("history")
print(books)
#extend function to add 2 list
books.extend(movies)
print(books)