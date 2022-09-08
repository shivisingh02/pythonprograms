x = [1,2,3,0,54,0,6,0,8,9,7,8]
for i in x:
    if i== 0:
        continue
    print(i)
#continue with while
i = 1
while i <= 5:
    data = input('enter data')
    if len(data) == 0:
        continue
    print(f'you entered a value of size {len(data)}')
    i = i + 1
 