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

# Main Routine Goes Here
for item in range(0, 2):
    width = num_check("width: ")
    print(width)

print()

for item in range(0, 2):
    height = num_check("Height: ")
    print(height)
