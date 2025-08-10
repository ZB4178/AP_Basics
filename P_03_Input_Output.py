#Ask the user for their name
username= input("What is your name?")

#Ask the user for their favorite number (integer)
fav_num= int(input("What is your favourite number?"))

#Double, halve and square the users favorite number
double=fav_num*2
halve=fav_num/2
square=fav_num**2

#Greet the user
print("\nHello",username,", your favourite number is ",fav_num)

#Output the results of doubling, halving and squaring their integer
print("\nDoubled=",double)
print("Halving=",halve)
print("Squaring=",square)

print("Have a nice day!")