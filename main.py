import requests as req

#Constants
API_KEY = "8519f3e8a64977c81f298e30631f1472"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


input_city = input("Enter your City Name: ")

loading= False

#Request URL
request_url = f"{BASE_URL}?q={input_city}&appid={API_KEY}"

def weather_data(data): 
    #assigning data
    weather = data['weather'][0]['description']
    temp = round(data['main']['temp'] - 273.15,2)
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']

    #printing data
    print("\nWeather: ",weather)
    print("Temperature: ",temp,"celsius")
    print("Humidity: ",humidity,"%")
    print("Air Pressure: ",pressure,"hPa")
    print("Wind Speed: ",wind_speed,"km/h")


#Exceptional Handling
try:
    response = req.get(request_url)
    #Validating the response
    if response.status_code == 200 :
        data = response.json()
        weather_data(data)

    else:
        print("Invalid City Name")

except:
    print("Error while fetching data")




    