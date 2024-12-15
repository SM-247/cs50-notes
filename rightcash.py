# Prompt the user for a valid amount
while True:
    amt = float(input("Enter the amount: "))
    if amt > 0:
        break

# Convert dollars to cents to avoid floating-point issues
if(amt<1.00):
    amt2 = round(amt * 100)
else:
    amt2=round(amt)


# Initialize the count of coins
count = 0

# Define denominations in cents
denominations = [25, 10, 5, 1]  # Correctly define coin values

# Calculate the minimum number of coins with debug prints
for coin in denominations:
    count += amt2 // coin  # Integer division to calculate number of coins
    amt2 %= coin           # Update the remaining amount
    print(f"After processing {coin}-cent coin: amt2 = {amt2}, count = {count}")  # Debugging

# Output the final result
print(f"Total coins used: {count}")
