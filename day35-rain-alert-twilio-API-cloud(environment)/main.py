import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os
from dotenv import load_dotenv

load_dotenv("../.env")

MY_NUMBER = os.getenv("MY_NUMBER")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
owm_api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat": 40.759950,
    "lon": -73.796500,
    "exclude":"current,minutely,daily",
    "appid": owm_api_key,
}


response = requests.get(OWM_Endpoint, params= weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])
weather_slice = weather_data["hourly"][:12]

will_rain = False


# print(weather_slice)
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:

    # This is for pythonanywhere
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # client = Client(account_sid, auth_token, http_client=proxy_client)

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️.",
        from_=TWILIO_NUMBER,
        to=MY_NUMBER
    )
    print(message.status)


