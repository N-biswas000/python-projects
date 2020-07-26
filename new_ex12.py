num1=int(input("Enter 1st no :"))
num2=int(input("Enter 2nd no :"))
def greater_num(num1,num2):
    if num1 > num2:
        return "1st no is greater then 2nd no"
    else:
        return "2nd no is greater than 1st no"
print(greater_num(num1,num2))