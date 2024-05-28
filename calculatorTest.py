import Calculator # type: ignore

response = 'y'

while response == 'y':
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter the second number: "))
    
    calc = Calculator.Calculator(num1,num2)

    print("\n1. Additiion\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation")
    choice = int(input("\nEnter a number between 1-5 to choose your choice: "))

    if choice == 1:
        print(f'{num1} + {num2} = {calc.addition()}')
    elif choice == 2:
        print(f'{num1} - {num2} = {calc.subtraction()}')
    elif choice == 3:
        print(f'{num1} * {num2} = {calc.multiplication()}')
    elif choice == 4:
        print(f'{num1} / {num2} = {calc.division()}')
    elif choice == 5:
        print(f'{num1} ** {num2} = {calc.exponent()}')