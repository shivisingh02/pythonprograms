#return function 
#reutrn keyword to return the answer from the function 
def get_salary():
    val = int(input('enter amt: ')) #input is usally is not used inside the functions 
    fine = 0.09
    sal = val * fine 
    return sal
sal = get_salary()
print('salalry =',sal )
print(get_salary())

final_salary = get_salary() + 1000
print(final_salary)