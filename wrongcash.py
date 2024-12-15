from cs50 import get_float
amt=get_float("Enter the amount: ")
count=0
denominations=[25,10,5,1]
for i in range(4):
    if amt>denominations[i]: 
        amt=amt-denominations[i]  
        count=count+1
    else:
        i=i+1
print(count)
"""
#The if condition doesn't account for multiple coins of the same denomination:
#You are subtracting only one coin's value (amt = amt - denominations[i]) per iteration, which means the loop doesn't consider that you might need multiple coins of the same denomination.
Floating-point precision issues:
When dealing with floating-point values (e.g., dollars and cents), comparisons like amt > denominations[i] may fail due to floating-point precision errors. It's better to work with integers (e.g., cents) to avoid this.
The else block and incrementing i manually:
Incrementing i manually in the else block is unnecessary, as the for loop already handles i iteration.
"""
