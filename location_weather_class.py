class LocationWeatherForecast():
    """
    LocationWeatherForecast class instantiated an object with a given location
    and can retrieve weather forecasts(future and historical) via Dark Sky API

    Params
    lat - location latitude, float
    long - location longitude, float
    api_key - personal API key for Dark Sky (https://darksky.net/dev)

    Upon initialization the object will make one call to the API and retrieve 
    the most current daily forecast
    """
    
    def __init__(self, lat, long, api_key):
        self.base_url = "https://api.darksky.net/forecast"
        self.lat = lat
        self.long = long
        self.api_key = api_key
        
        current_time = datetime.datetime.now()
        current_date = current_time.strftime('%Y-%m-%d')
        request_url = (url + api_key +'/' + str(lat) + ',' + str(long) + 
                            ',' + current_date + 'T12:00:00')
        response = requests.get(request_url)
        current_forecast = response.json()['daily']['data'][0]['icon']
        
        self.timezone = response.json()['timezone']
        self.location_name = self.timezone.split('/')[-1]
        self.current_forecast = current_forecast
        
    def retrieve_daily_forecast(self, date_str, time_str='12:00:00'):
        """
        returns general daily forecast given a specific date

        takes input date string in the format 01-01-2020
        """
        time = date_str + 'T' + time_str
        request_url = url + self.api_key +'/' + str(self.lat) + ',' + str(self.long) + ',' + time
        response = requests.get(request_url)
        
        weather = response.json()['daily']['data'][0]['icon']
        
        return weather