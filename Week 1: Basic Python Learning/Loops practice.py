# Write a Python program that gives the user exactly 3 attempts to enter the correct PIN.

# Use a while loop to repeatedly ask the user to enter their PIN.

# Track how many attempts the user has left.

# If they enter the correct PIN, print "Access Granted!" and stop the loop.

# If they enter the wrong PIN, subtract an attempt and print "Incorrect. You have X attempts left."

# If they use up all 3 attempts and still get it wrong, print "Account Locked." and end the program.

pin=input("enter the real PIN:")
attempts=3

while attempts>0:
    UserInput=input("enter the PIN:")
    if UserInput==pin:
        print("Access Granted!")
        break
    else:
        attempts-=1
        print(f"Incorrect. You have {attempts} attempts left.")
if attempts==0:
    print("Account Locked.")
