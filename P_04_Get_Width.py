# Ask user for width and loop until they
# enter a number that is more than zero

error = "Please enter a number more than 0\n"
while True:

    try:
        #Ask user for number
        width = float(input("Width:"))

        #Check number is more than zero
        if width> 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)