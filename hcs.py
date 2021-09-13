# Lets user input their amount of saved money
savings = input("Savings: ")
# Lets user input interest
growth_raw = input("Interest: ")
# Converts percent to decimal
growth = (float(growth_raw) / 100) + 1
# Lets user input the amount of years
years = input("Years: ")
# Calculates the final outcome and rounds it down to 1 decimal
result_raw = int(savings) * float(growth) ** int(years)
result = f"{result_raw:.1f}"
# Prints result for the user to see
print("You will have $" + str(result) + " after " + str(years) + " years. Amazing!")
