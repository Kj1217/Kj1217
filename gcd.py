def gcd(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    
    return x

x = int(input("Enter number:"))
y = int(input("Enter another number: "))

print(f'\nThe gcd of {x} and {y} is {gcd(x,y)}.')
