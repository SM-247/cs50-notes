from cs50 import get_float

# Prompt the user for a valid amount
while True:
    amt = get_float("Enter the amount: ")
    if amt > 0:
        break

# Convert dollars to cents to avoid floating-point issues
amt = round(amt * 100)

# Initialize the count of coins
count = 0

# Define denominations in cents
denominations = [25, 10, 5, 1]

# Calculate the minimum number of coins
for coin in denominations:
    count += amt // coin  # Use integer division to get the number of coins
    amt %= coin           # Update the amount to the remainder

# Output the result
print(count)
