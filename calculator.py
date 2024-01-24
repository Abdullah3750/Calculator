def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y): 
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    print("\033[1;34;40m=== Simple Calculator ===\033[0m")

    while True:
        print("\nSelect operation:")
        print("\033[1;32;40m1. Addition\033[0m")
        print("\033[1;32;40m2. Subtraction\033[0m")
        print("\033[1;32;40m3. Multiplication\033[0m")
        print("\033[1;32;40m4. Division\033[0m")
        print("\033[1;31;40m5. Exit\033[0m")

        choice = input("\033[1;37;40mEnter choice (1-5): \033[0m")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("\033[1;37;40mEnter first number: \033[0m"))
                num2 = float(input("\033[1;37;40mEnter second number: \033[0m"))

                if choice == '1':
                    print(f"\n\033[1;36;40mResult: {add(num1, num2)}\033[0m")
                elif choice == '2':
                    print(f"\n\033[1;36;40mResult: {subtract(num1, num2)}\033[0m")
                elif choice == '3':
                    print(f"\n\033[1;36;40mResult: {multiply(num1, num2)}\033[0m")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\n\033[1;36;40mResult: {result}\033[0m")
            except ValueError:
                print("\033[1;31;40mInvalid input. Please enter valid numbers.\033[0m")
        elif choice == '5':
            print("\033[1;33;40mExiting calculator. Goodbye!\033[0m")
            break
        else:
            print("\033[1;31;40mInvalid choice. Please enter a number between 1 and 5.\033[0m")

if __name__ == "__main__":
    calculator()
