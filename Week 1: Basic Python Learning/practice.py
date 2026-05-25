# Write a Python program to check this list of seats:
# row = [1, 1, 0, 1, 0, 0, 1, 0]

# Loop through the list to see if there are two 0s side-by-side.

# If you find two adjacent empty seats, print "Seats found! Let's buy them." and stop looking (stop the loop).

# If you check the entire row and never find two empty seats together, print "No seats together. Let's watch something else."

# Hint: You can't just loop through the items one by one like for seat in row:.
#  You will need a way to look at the "current seat" AND the "next seat" at the same time.

row=[1,1,0,1,0,0,1,0]
prev=0
curr=0

for i in range(len(row)-1):
    if row[i]==0 and row[i+1]==0:
        print("Seats found! Let's buy them.")
        print("Seats are at index",i,"and",i+1)
        break
else:
    print("No seats together. Let's watch something else.")

    
