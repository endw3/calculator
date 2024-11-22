print("Welcome to the calculator")
print("available arithmetic operations (multiplication, division, addition, subtraction, power)")
operation = input("What process do you want? ").lower()

if operation == "addition":
    x = int(float(input("Enter number 1 : ")))
    y = int(float(input("Enter number 2 : ")))
    z = x+y
    print("The result: ",z)
    
elif operation == "subtraction":
    x = int(float(input("Enter number 1 : ")))
    y = int(float(input("Enter number 2 : ")))
    z = x-y
    print("The result: ",z)
    
elif operation == "multiplication":
    x = int(float(input("Enter number 1 : ")))
    y = int(float(input("Enter number 2 : ")))
    z = x*y
    print("The result: ",z)
    
elif operation == "division":
    x = int(float(input("Enter number 1 : ")))
    y = int(float(input("Enter number 2 : ")))
    z = x/y
    print("The result: ",z)

elif operation == "power":
    x = int(float(input("Enter number : ")))
    y = int(float(input("Enter the power number : ")))
    z = x**y
    print("The result: ",z)
    
    
    
    