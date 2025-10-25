sum = (input("Enter calculation: "))
opp = ['+', '-', '*', '/']

if '+' in sum:
    numbers = sum.split('+')
    result = float(numbers[0]) + float(numbers[1])
    print("Result:", result)
elif '-' in sum:
    numbers = sum.split('-')
    result = float(numbers[0]) - float(numbers[1])
    print("Result:", result)
elif '*' in sum:
    numbers = sum.split('*')
    result = float(numbers[0]) * float(numbers[1])
    print("Result:", result)
elif '/' in sum:            
    numbers = sum.split('/')
    if float(numbers[1]) == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = float(numbers[0]) / float(numbers[1])
        print("Result:", result)
else:
    print("Error: Invalid operation. Please use +, -, *, or /.")