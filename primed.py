primed = input("Enter a prime number: ")

if primed.isdigit():
    primed = int(primed)
    if primed > 1:
        for i in range(2, int(primed ** 0.5) + 1):
            if (primed % i) == 0:
                print(primed, "is not a prime number")
                break
        else:
            print(primed, "is a prime number")
    else:
        print(primed, "is not a prime number") 