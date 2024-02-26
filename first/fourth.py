# ask for the current month
current_month = int(input("The current month is: "))

# check if the input is correct
while current_month > 12:
    # while it's not print the error
    print("Error: The month should be less than or equal to 12.")
    # demand again the current month
    current_month = int(input("Please enter a valid month: "))

# ask for the current day
current_day = int(input("The current day of the month is: "))

# check if the input is correct
while current_day > 30:
    # while it's not print the error
    print("Error: The day should be less than or equal to 30.")
    # demand again the current day
    current_day = int(input("Please enter a valid day: "))

# calculate the remaining days
days_remaining = (30 - current_day) + (12 - current_month) * 30

# print the result
print("The days remaining till the end of the month are:", days_remaining)
