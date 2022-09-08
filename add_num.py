ans = 0
while True:
    x = input('enter the number')
    if x.isnumeric():
        ans = int(x) + ans
    else:
        break
print('total =',ans)