from helper import read
data = read('pride_n_prejudice.txt')
from string import ascii_lowercase #import all the alphabet in english 

for letter in ascii_lowercase:
    counter = data.count(letter)
    print(f'{letter} found {counter} times')

from string import ascii_uppercase #import all the alphabets in uppercase
for letter in  ascii_uppercase:
    counter = data.count(letter)
    print(f'{letter} found {counter} times')

#wap to find the most occuring alphabet and its frequency
max = 0
for i , n in zip(ascii_lowercase , ascii_uppercase):
    counter1 = data.count(i)
    counter2 = data.count(n)
    if counter1 > counter2 and counter1 > max:
        max = counter1
        alpha = i
    else:
        if counter2 > max:
            max = counter2
            alpha = n
print(f'the max ocurring letter is {alpha} and it ocurrs {max} times')

#wap to find vowels in the given data file
for vowel in "aeiouAEIOU":
    print(f'{vowel} is found {data.count(vowel)} times')
#wap to remove all the punctuations from the string
str= 'hel@rh$.!fbhhf!()jfgdhdh%#'
from string import punctuation 
for marks in punctuation:
    str = str.replace(marks , '')
print(str)