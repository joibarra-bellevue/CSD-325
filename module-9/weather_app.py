import requests, json, re

# declaring variables to store api endpoint and api id
url = 'https://api.openweathermap.org/data/2.5/weather'
appid = "906b6939735602a519447e37a839d229"


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

            # connection test (uncomment if needed)
            print(response.status_code)

            received_response = response.json()

            # formatted output for debugging (uncomment if needed)
            jprint(received_response)

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