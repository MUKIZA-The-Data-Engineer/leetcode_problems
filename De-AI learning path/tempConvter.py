#   CODING A TAEMPERATURE CONVERTER FROM Fahrenheit to Celicius

def convert_temperature(temp, from_unit):

    # Your code here
   
    unit = from_unit.strip().upper()

    try:
        temp  = float(temp)
    except ValueError:
        print("Error: Temperature must a valid number!")
        return 

    if unit == "C":
        farhrenheit = (temp * 9/5) + 32
        print(f"{temp} C = {farhrenheit: .1f} F")

    elif unit == "F":
       Celcius = (temp - 9/5) * 5/9
       print(f"{temp} C = {Celcius: .1f} C")

    else:
        print("Invalid input!")



convert_temperature(100, 'C')      # Outputs: 100°C = 212.0°F
convert_temperature(32, 'F')       # Outputs: 32°F = 0.0°C
convert_temperature("invalid", 'C') # Outputs: Error: Temperature must be a valid number!
convert_temperature(100, 'X') 

















 # while True:
    #     try:
    #         temp = float(input("Enter your temperature in Fahrenheit"))
    #         if temp > 0:
    #             break
    #         print("the value must be greater than zero")
    #     except ValueError:
    #         print("Invalid error pleae enter a MF number bro: ")

    # while True:
    #         try:
    #             from_unit = float(input("Enter your temperature in Celicius"))
    #             if from_unit > 0:
    #                 break
    #             print("the value must be greater than zero")
    #         except ValueError:
    #             print("Invalid error pleae enter a MF number bro: ")

