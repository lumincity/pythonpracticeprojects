
def add(x, y):
   return x + y

def sub(x, y):
   return x - y

def multi(x, y):
    return x * y

def divi(x, y):
    return x / y


print("Please Select and Operation")

print(" Enter 'a' for Addition")

print(" Enter 's' for Subtraction")

print(" Enter 'm' for Multiplication")

print(" Enter 'd' for Division")


while True:
    
    c = input("Enter a choice: ")

    if c in ("a", "s", "m", "d"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if c == 'a':
            print(num1, "+", num2, "=", add(num1, num2))

        elif c == 's':
             print(num1, "-", num2, "=", sub(num1, num2))

        elif c == "m":
            print(num1, "*", num2, "=", multi(num1, num2))

        elif c == "d":
            print(num1, "/", num2, "=", divi(num1, num2))

        again = input("Want to keep going? Y/N?  ")
        if again == "n":
          break
        else:
          print("Invalid Input. Please try again")