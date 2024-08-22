import requests

# Your WeatherAPI key
api_key = "50f60cc39b1d42408c2210737241508"
base_url = "https://api.weatherapi.com/v1/current.json"

def get_weather(city_name):
    url = f"{base_url}?key={api_key}&q={city_name}"
    
    # Make a request to the WeatherAPI
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract and format the weather information
        location = data['location']
        current = data['current']
        
        city = location['name']
        temperature = current['temp_c']
        humidity = current['humidity']
        description = current['condition']['text']
        
        return (f"Weather in {city}:\n"
                f"Temperature: {temperature}°C\n"
                f"Humidity: {humidity}%\n"
                f"Description: {description}")
    else:
        return "City not found or API request failed."

def main():
    while True:
        city_name = input("Enter city name (or 'quit' to exit): ")
        if city_name.lower() == 'quit':
            break
        print(get_weather(city_name))

if __name__ == "__main__":
    main()
