#types of function 
#non parameterized 
#randint gives number  to u at ramndom if you give it a certsin range 
from random import randint 
def hello():  #function name should be written in lowercase 
    print('hello')
    print('hola')
    print('amigos')
    print('✌️ ✌️ ✌️')

def roll_dice():
    dices = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
    print(" => ",dices[randint(0,5)])
hello()
roll_dice() #calling the function 