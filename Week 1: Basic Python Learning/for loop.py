u=50

for t in range(0,11):
    if u<=0:
        print("the car has stopped")
        break
        
    u-=5
    print(f"speed at this {t} seconds is {u} km/h")