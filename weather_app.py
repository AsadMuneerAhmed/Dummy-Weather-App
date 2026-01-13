import datetime
import random


days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


city_list = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta","Hydrabad","Khairpur","Dadu", "Golarchi" ]  # Add more cities if needed


while True:
    
    city_input = input("Enter city name: ").strip().title()

   
    if city_input in city_list:
        
        weather = random.choice(["Sunny", "Cloudy", "Rainy", "Windy"])
        temp = random.randint(7, 30)  # realistic temp range

        today_index = datetime.datetime.today().weekday()  # Monday=0 ... Sunday=6
        current_day = days_list[today_index]
    

    
        print("\n--- Weather Information ---")
        print(f"City: {city_input}")
        print(f"Day: {current_day}")
        print(f"Weather: {weather}")
        print(f"Temperature: {temp}°C")
        print("----------------------------\n")

    else:
        print("City not found in database. Try another city.\n")


    choice = input("Do you want to check another city? (yes/no): ").strip().lower()
    if choice != "yes":
        break

print("Thank you for using the Weather App!")
