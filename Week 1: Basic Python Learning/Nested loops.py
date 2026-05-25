# Write a Python program using nested for loops (using the range() function) to print every ticket combination.

# Use an outer loop to count through the rows (1 to 3).

# Use an inner loop to count through the seats (1 to 5).

# For each seat, print a label like this: "Row X - Seat Y".

# The Catch: Seat number 3 in Row 2 is broken! Inside your inner loop,
#  write an if statement so that if the row is 2 AND the seat is 3, you skip printing that ticket (using the continue command).

for row in range(1,4):
    for seat in range(1,6):
      if row==2 and seat==3:
          continue
      print(f"Row {row} - Seat {seat}")