weatherTemp=float(input("Hi Ji!!! What's the weather today:"))
if weatherTemp <= 10:
    print(f"{weatherTemp} °C is too cold!! Wear a warm coat and scarf!")
elif weatherTemp > 10 and weatherTemp < 25:
    print(f"{weatherTemp} °C is mild cold!! Wear A light jacket bro!")
elif weatherTemp >25:
    print(f"{weatherTemp} °C is so hot!!! Wear T-shirt that would be perfect!")
else:
    print(f"{weatherTemp} It's a Correct weater bro!")
