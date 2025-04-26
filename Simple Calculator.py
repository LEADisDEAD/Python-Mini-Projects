

def ADD(num1,num2):
    return (num1+num2)
def SUB(num1,num2):
    return (num1-num2)
def MUL(num1,num2):
    return (num1*num2)
def DIV(num1,num2):
    if num2 == 0:
        print("Cannot divide by 0")
    return (num1/num2)

print("---CALCULATOR---")
flag = True
while(flag==True):
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    choice = input("Enter operator (+,-,*,/) : ")

    match choice:
        case "+":
            res = ADD(num1,num2)
            print(res)
        case "-":
            res = SUB(num1, num2)
            print(res)
        case "*":
            res = MUL(num1, num2)
            print(res)
        case "/":
            res = DIV(num1, num2)
            print(res)
        case _:
            print("Invalid operator")


    choice2 = input("Continue or exit?").lower()
    if(choice2 == "exit"):
        flag = False
    else:
        continue