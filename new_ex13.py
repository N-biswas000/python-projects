num1=int(input("Enter 1st number :"))
num2=int(input("Enter 2nd number :"))
def greater_num(num1,num2):
    if num1 > num2:
        return "1st number is Greater than 2nd number"
    else:
        return "2nd number is Greater than 1st number"
print(greater_num(num1,num2))