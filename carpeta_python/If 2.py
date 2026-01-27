year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
    if 0!=year%4 and 0!=year%400:
        print("Es un año comun")
    elif 0!= year%100:
        print("Es un año bisiesto")
    else:
        print("Es un año bisiesto")
