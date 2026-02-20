#Jorge Ibarra
#2/17/2026
#Module 9.2 Assignment CSD325

# This program will ask the user to input a zip code and then use the OpenWeatherMap API to retrieve the current weather information for that location. 
# The program will validate the zip code input, make an API request, and display the temperature and "feels like" temperature to the user. The user can continue entering zip codes or exit the program as desired.

import requests, json, re

# declaring variables to store api endpoint and api id
url = 'https://api.openweathermap.org/data/2.5/weather'
appid = "906b6939735602a519447e37a839d229"

# function to print json formatted 
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_weather_by_zip():
    # initiating loop with boolean statement
    while True:
        zip_code = input("Enter the zip code: ")

        # using regex to confirm zip_code is a full match for only digits and length of 5
        if re.fullmatch("[0-9]{5}", zip_code):
            modified_url = f'{url}?zip={zip_code},us&units=imperial&APPID={appid}'
            response = requests.get(modified_url)

            # connection test and priting connection status 
            print(response.status_code)
            received_response = response.json()

            #calling function to print json response
            jprint(received_response)
            # extracting temperature and real feel temperature from json response and printing to user
            temp = received_response["main"]["temp"]
            real_temp = received_response["main"]["feels_like"]
            print(f"The temperature is {temp} but it feels like {real_temp}")
        else:
            # if input validation fails returning a message to user
            print("Invalid zip: " + zip_code)

        # providing an option to continue entering zip codes or exiting app
        user_input = input(
            "Enter any key to proceed with another zip code or type 'exit' to quit: "
        ).strip().lower()

        if user_input == "exit":
            break


# start program
get_weather_by_zip()