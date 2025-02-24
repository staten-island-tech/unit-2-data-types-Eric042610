""" values = [1,2,3,4,5,6,7,8,9,10]
print(values)
for i in values:
    if value == "even":
        print("even")
    else:
        print("odd")
    print(i) """


"""     # Function to check if a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Ask user for a number
user_number = int(input("Enter a number: "))

# Call the function to check
check_odd_even(user_number)
 """

def odd_even(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

user_number = int(input("Enter a number: "))
odd_even(user_number)
