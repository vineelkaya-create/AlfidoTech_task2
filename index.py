import requests
from datetime import datetime

print("====== WEATHER INFORMATION USING API ======")

# Take city name input
city = input("Enter city name: ")

# OpenWeatherMap API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid="your api_key"&units=metric"

try:
    # Sending GET request
    response = requests.get(url, timeout=10)

    # Convert response into JSON
    data = response.json()

    # Check successful response
    if response.status_code == 200:

        # Extract required information
        city_name = data["name"]
        country = data["sys"]["country"]

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        weather = data["weather"][0]["description"]

        wind_speed = data["wind"]["speed"]
        visibility = data.get("visibility", 0) / 1000   # meters to km

        sunrise_timestamp = data["sys"]["sunrise"]
        sunset_timestamp = data["sys"]["sunset"]

        # Convert timestamps into readable time
        sunrise = datetime.fromtimestamp(sunrise_timestamp).strftime("%I:%M:%S %p")
        sunset = datetime.fromtimestamp(sunset_timestamp).strftime("%I:%M:%S %p")

        # Current Date and Time
        current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

        # Filtering logic
        if temperature > 30:
            climate = "Hot"
        elif temperature > 20:
            climate = "Warm"
        else:
            climate = "Cool"

        # Display output
        print("\n====== WEATHER REPORT ======")

        print("Date & Time:", current_time)

        print("\nLocation Details")
        print("City:", city_name)
        print("Country:", country)

        print("\nWeather Details")
        print("Temperature:", temperature, "°C")
        print("Feels Like:", feels_like, "°C")
        print("Humidity:", humidity, "%")
        print("Pressure:", pressure, "hPa")
        print("Weather Condition:", weather)
        print("Climate Type:", climate)

        print("\nWind & Visibility")
        print("Wind Speed:", wind_speed, "m/s")
        print("Visibility:", visibility, "km")

        print("\nSun Timings")
        print("Sunrise:", sunrise)
        print("Sunset:", sunset)

    else:
        print("\nInvalid city name or API key.")
        print("Error Message:", data["message"])

# Connection Error
except requests.exceptions.ConnectionError:
    print("Internet connection error.")

# Timeout Error
except requests.exceptions.Timeout:
    print("Request timed out.")

# General Request Errors
except requests.exceptions.RequestException as e:
    print("Error:", e)

print("\n====== PROGRAM COMPLETED ======")
