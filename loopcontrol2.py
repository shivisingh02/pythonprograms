while True:
    price = int(input('enter your price'))
    if price < 0:
        break
    print(f"your enterd amount is {price}")
x = [1,3,9,0,4,3,6,-7,68,78,-6]
for i in x:
    if i < 0 :
        break 
    print(i)