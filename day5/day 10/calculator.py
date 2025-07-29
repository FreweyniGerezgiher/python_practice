# print("here is the calculator")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
# print("5. Exit")
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    if num2==0:
        return "Error! Division by zero is not allowed."
    else:
        return num1/num2
    
# while True:
#     choice = input("Enter your choice (1/2/3/4/5): ")
#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         if choice == '1':
#             add(num1,num2)
#             print(num1,"+",num2,"=",add(num1,num2))
#         elif choice == '2':
#             sub(num1,num2)
#             print(num1,"-",num2,"=",sub(num1,num2))
#         elif choice == '3':
#             mul(num1,num2)
#             print(num1,"*",num2,"=",mul(num1,num2))
#         elif choice == '4':
#             div(num1,num2)
#             print(num1,"/",num2,"=",div(num1,num2))
#         else:
#             print("Invalid input")
operations = {"+":add,
        "-": sub,
        "*": mul,
        "/": div}
def calculator():
    num1 = float(input("Enter first number: "))

    for symbol in operations:
        print(symbol)
    should_cont = True
    while should_cont:
        operation_symbol = input("pick an operation from the line above: ")
        num2 = float(input("Enter second number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(answer)
        if input(f"type 'y' to continue with {answer} or type 'n' start new calculation. : ") == "y":
            num1 = answer
        else:
            should_cont == False
            calculator()
calculator()

                    

