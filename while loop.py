profit=int(input("enter the profit:"))
year=0

while profit<=20000:
    profit=profit*108/100
    year=year+1

print(f"it will take {year} years to reach this profit")    



