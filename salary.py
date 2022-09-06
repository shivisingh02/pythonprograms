sal = int(input('enter salary: '))
if sal > 100000:
    da = 3.5
    hra = 9.1
elif sal > 80000:
    da = 3.2 
    hra = 9
elif sal > 60000:
    da = 2.8
    hra = 9
elif sal > 50000:
    da = 2.5 
    hra = 8
elif sal > 40000:
    da = 2.5
    hra = 7.7
elif sal > 30000:
    da = 2.2 
    hra = 8
elif sal > 20000:
    da = 2.2
    hra = 7
elif sal > 10000 :
    da = 2.2 
    hra = 6
else:
    print('invalid salary')
sal = sal + (da / 100 * sal) + (hra / 100 * sal)
print(f'da = {da} and hra = {hra} salary = {sal}')