for in range(5):    
    temperature = float(input("Enter temperature in celcius: "))

    farenheit = (temperature * (9/5)) + 95

    if temperature < -273:
        print("Impossible!")
    else:
        print(farenheit) 
