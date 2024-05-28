class Calculator:
    def __init__(self,num1,num2):
        self.n1 = num1
        self.n2 = num2

    def addition(self):
        """This method adds the two numbers"""
        return self.n1 + self.n2
    
    def subtraction(self):
        """This method subtracts the two numbers"""
        return self.n1 - self.n2
    
    def multiplication(self):
        """This method multiplies the two numbers"""
        return self.n1 * self.n2
    
    def division(self):
        """This method divides the two numbers"""
        try:
            divide = self.n1 / self.n2
            return divide
        except ZeroDivisionError:
            print("The second number can't be zero. The output will be set to None.")
    
    def exponent(self):
        return num1 ** num2
    
quitP = 0
print("Welcome to the Caluculator Program")
while quitP != 1:
    response = 'y'
    num1 = int(input("\nEnter a number: "))
    num2 = int(input("Enter the second number: "))

    while response != 'n':
        
        calc = Calculator(num1,num2)

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
        
        response = input("Do you want to use the same numbers? Enter y/n: ")
        if response == 'n':
            print("\n1.Quit the program\n2.Enter new numbers")
            quitP = int(input("Enter 1 or 2 to quit the program or to continue: "))
        else:
            pass
print("Thanks for using this Program!")