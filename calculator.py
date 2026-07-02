print("=== Simple Calculator ===")
print("Operation: +(add), -(subtract), *(multiply), /(divide)")
print("type 'exit' to quit the calculator")

while True:
    
    #get the first number from the user
    user_input1 = input("Enter the first number: (or type 'exit' to ): ").strip()
    if user_input1.lower() == 'exit':
        break
    num1 = float(user_input1)

    #get the mathematical operation from the user
    operation = input("Enter operation: ").strip()
    if operation.lower() == 'exit':
        break

    #get the second number from the user
    user_input2 = input("Enter the second number: (or type 'exit' to ): ").strip()
    if user_input2.lower() == 'exit':
        break
    num2 = float(user_input2)

    #perform the calculation
    if operation == '+':
        result = (num1 + num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
            continue
    else:
        print("Error: Invalid operation.")
        continue

    #display the result