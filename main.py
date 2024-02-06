import time


def addition(a, b):
    return a + b


def substraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


print("Booting up calc v3.1....")
time.sleep(3)
name = input("Enter your name: ")
print(f"Signing in as {name}")
time.sleep(2)

while True:
    print("\n-- WELCOME TO THE CLI CALCULATOR --")
    a = int(input("Please enter your number(s) of choice: "))
    b = int(input("Please enter your number(s) of choice: "))

    print("Collecting data...")
    time.sleep(4)

    print("Press 1 for Addition")
    print("Press 2 for Substraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("Press 5 for exit")

    print("-" * 45)
    user_choice = int(input("Choose one: "))
    print("Processing, please wait...")
    time.sleep(3)

    if user_choice == 1:
        result = addition(a, b)
        print(f"The result is = {result}")

    elif user_choice == 2:
        result = substraction(a, b)
        print(f"The result is = {result}")

    elif user_choice == 3:
        result = multiplication(a, b)
        print(f"The result is = {result}")

    elif user_choice == 4:
        result = division(a, b)
        print(f"The result is = {result}")

    elif user_choice == 5:
        print("Exiting system....")
        time.sleep(3)
        print(f"Exit succesful! Goodbye {name}")
        break
    else:
        print("Invalid argument(s), please try again!")
