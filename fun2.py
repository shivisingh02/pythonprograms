#simple interest 
from re import T


def amount():
    p = int(input('enter amount: '))
    r = float(input("enter rate of interest: "))
    t = int(input('enter time: '))
    si = (p * r * t) /100
    amt = p + si 
    return amt , si
amt ,si = amount()
print(f'the amount will be {amt} on simple interest {si}')
print('total amount:' ,amount())
print(amount()[0]) #to only print amount 
