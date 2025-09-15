# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "Please enter a number more than 0\n"
    while True:

        try:
            #Ask user for number
            response = float(input(question))

            #Check number is more than zero
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

# Main routine starts here

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("width: ")
    height = num_check("Height: ")
    cost = num_check("Cost per Meter: ")

    # Calculate cost / perimeter
    perimeter = 2 * (width + height)
    money = perimeter * cost
    # Display output
    print()
    print(f"Perimeter: {perimeter} meters")
    print(f"Cost of whole thing: {money} dollars")

    #Ask user if they want to keep going

    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the Fence Cost calculator")