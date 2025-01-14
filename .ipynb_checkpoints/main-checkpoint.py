

def send_weather_notification():
    
    import requests
    from twilio.rest import Client
    from dotenv import load_dotenv
    import os

    load_dotenv()

    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    FROM_PHONE = os.getenv("FROM_PHONE")
    TO_PHONE = os.getenv("TO_PHONE")

    
    # Get weather forecast
    location = "London,UK"  # Replace with your location
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Extract tomorrow's weather
    tomorrow_weather = data['list'][0]  # Adjust as needed
    description = tomorrow_weather['weather'][0]['description']

    # Decide the notification message
    if "rain" in description:
        message = "It will rain tomorrow. Don't forget your umbrella!"
    elif "clear" in description:     
        message = "Sunny tomorrow! Enjoy the sunshine!"
    else:
        message = f"Tomorrow's weather: {description}."

    # Send SMS via Twilio
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(body=message, from_=FROM_PHONE, to=TO_PHONE)

# For testing locally
'''if __name__ == "__main__":
    send_weather_notification()'''

def cloud_function_entry_point(request):
    # Call your existing function
    send_weather_notification()
    return "Weather notification sent", 200