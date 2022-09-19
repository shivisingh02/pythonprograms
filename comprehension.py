x = [1,2,3,2,3,4,3]
x2 = [i**2 for i in x]
print(x2)
#syntax of comprehensiom newlist = [operation loop condition]
#xcube = [i**3 for i in x]
#xeven = [i for i in x if i % 2 == 0]
xodd = [ i for i in x if not(i% 2 == 0)]
print(xodd)
xeven = [i ** i for i in x if x%2 == 0]
 
