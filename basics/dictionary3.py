import helper  as h 
from string import punctuation 
data = h.read('basics/pride_n_prejudice.txt')
print(len(data))
for p in punctuation:
    data = data.replace(p , "")

#split into words and remove spaces and empty strings 
words = [word.strip() for word in data.lower().split()]

print('total words found ' , len (words) )
print('uniques words found: ',len (set(words)))

#create a dictionary 
wc = {}
for word in words:
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1

#sorting the dictionary  -> wc.items() reutrns a list 
wc = sorted (wc.items(), key = lambda x: x[1], reverse = True)

#print top 10 words 
for i in range(10):
    print(wc[i])
