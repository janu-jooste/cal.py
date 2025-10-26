sum = (input("Enter calculation: "))
opp = ['+', '-', '*', '/']

for opp in sum:
    numbers = sum.split(opp)
    if opp == '+':
        result = float(numbers[0]) + float(numbers[1])
        print("Result:", result)
    elif opp == '-':
        result = float(numbers[0]) - float(numbers[1])
        print("Result:", result)
    elif opp == '*':
        result = float(numbers[0]) * float(numbers[1])
        print("Result:", result)
    elif opp == '/':          
        if float(numbers[1]) == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = float(numbers[0]) / float(numbers[1])
            print("Result:", result)
    elif opp == '%':
        result = float(numbers[0]) % float(numbers[1])
        print("Result:", result)
    elif opp == '**':
        result = float(numbers[0]) ** float(numbers[1])
        print("Result:", result)
    elif opp == '<':
        result = float(numbers[0]) < float(numbers[1])
        if result is True :
            print("Result: True")
        else :
            print("Result: False")
    elif opp == '>':
        result = float(numbers[0]) > float(numbers[1])
        if result is True :
            print("Result: True")
        else :
            print("Result: False")
