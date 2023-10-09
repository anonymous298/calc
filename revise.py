def add(a,b):
    sum = a + b
    return sum

def subtract(a,b):
    sum = a - b
    return sum

def multiplication(a,b):
    sum = a * b
    return sum

def division(a,b):
    sum = a / b
    return sum

def remainder(a,b):
    sum = a % b
    return sum

def exponential(a,b):
    sum = a ** b
    return sum

def display():
    name = input("Enter Your Name Here: ")
    print(f"\nWelcome {name} To Our Calculator")
    
def operators():
    display()

    print("\nPress 1 For Addition")
    print("Press 2 For Subtraction")
    print("Press 3 For Multiplication")
    print("Press 4 For Division")
    print("Press 5 For Take Remainder")
    print("Press 6 For Exponential")
    print("Press 0 For Exit The Calculator")

def operators_input():
    while True:

        operators()
    
        inp = int(input("\nEnter Here: "))

        if inp == 0:
            print("\nExiting The Program")
            break
        
        num1 = int(input("\nEnter Your First Number Here: "))
        num2 = int(input("\nEnter Your Second Number Here: "))

        if inp == 1:
            ans = add(num1,num2)
            print(ans)

        elif inp == 2:
            ans = subtract(num1,num2)
            print(ans)

        elif inp == 3:
            ans = multiplication(num1,num2)
            print(ans)

        elif inp == 4:
            if num2 <= 0:
                print("0 is not divisabla")

            else:
                ans = division(num1,num2)
                print(ans)

        elif inp == 5:
            ans = remainder(num1,num2)
            print(ans)

        elif inp == 6:
            ans = exponential(num1,num2)
            print(ans)

        else:
            print("Enter Valid Input!")

operators_input()