#union of sets
A = {1,2,3,4,5,6,3,3}
B = {3,8,9,5,56,4}
print(A|B)
C =A.union(B)
print(C)
#INTERSECTION OF SETS
print(A&B)
C = A.intersection(B)
print(C)
#A - B DIFFERENCE
print(A - B)
print(A.difference(B))
#set symmetric difference everything except the common items
print(A ^ B)
print(A.symmetric_difference(B))
