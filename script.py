#Program to make a simple python calculator

#Addition Function
def add(x,y):
    return x+y

#Subtraction Function
def minus(x,y):
    return x-y

#multiply
def multiply(x,y):
    return x*y

#divide
def divide(x,y):
    return x/y

print("Please selection your option: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

while True:
    #Getting the users input
    choice = input("Enter your choice: ")
    
    #checking if the input is valid
    if choice in ('1','2','3','4'):
        no1 = float(input("Enter First Number: "))
        no2 = float(input("Enter Second Number: "))

        #Choice selected is addition
        if choice == '1':
            print("The addition of " + str(no1) + " and " + str(no2) + " is " + str(add(no1, no2)))
        
        #choice selected is subtraction
        elif choice == "2":
            print("The subtraction of " + str(no1) + " from " + str(no2) + " is " + str(minus(no1, no2)))
        
        #choice selected is multiply
        elif choice == "3":
            print("The mulitiplication of " + str(no1) + " and " + str(no2) + " is " + str(multiply(no1, no2)))
        
        #choice selected is divide
        else:
            print ("The Division of " + str(no1) + " from " + str(no2) + " is " + str(divide(no1, no2)))

    #exiting the program
    elif choice == "5":
        break
    
    #invalid option given
    else:
        print("Invalid option")