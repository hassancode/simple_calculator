message = "\nEnter 1 for addition\n"
message+= "Enter 2 for subtraction\n"
message+= "Enter 3 for multiplication\n"
message+= "Enter 4 for division\n"
message+= "Enter x for exit"

def add(op1, op2):
    return op1+op2

def multiply(op1, op2):
    return op1*op2

def subtract(op1, op2):
    return op1-op2

def divide(op1, op2):
    return op1/op2



while True:
    print(message)
    selection = input("Enter choice: ")

    if(selection != "1" and selection != "2" and selection != "3" and selection != "4" and selection != "x"):
        print("oops!! wrong choice\n")
        continue

    if (selection == "x"):
        break
    op1 = int(input("Enter first operand: "))
    op2 = int(input("Enter second operand: "))

    if (selection == "1"):
        result = add(op1,op2)

    if (selection == "2"):
        result = subtract(op1,op2)

    if (selection == "3"):
        result = multiply(op1,op2)

    if (selection == "4"):
        result = divide(op1,op2)

    print(result)
    
print("thank you!!")


    
    
