import urllib3
import datetime
import sys
import json
http = urllib3.PoolManager()

class AirportStatus:
    def __init__(self, airport_code):
        self.API_URL = "https://nasstatus.faa.gov/api/airport-events"
        self.details = []
        self.airport_delays(airport_code)
        self._display()
    def _get_data_by_airport(self, response, airport_code):
        airport_data = {}
        for airport in response:
            if airport.get('airportId').upper() == airport_code.upper():
                airport_data['Name'] = airport.get('airportLongName')
                airport_data['IATA'] = airport.get('airportId')
                airport_data['Delay'] = airport.get('groundDelay', dict()).get('avgDelay', '')
                airport_data['Weather'] = airport.get('groundDelay', dict()).get('impactingCondition', '')
                airport_data['Status'] = airport.get('departureDelay', 'NA')
        return airport_data

    def _get_faa_data(self, airport_code):
        r = http.request('GET', self.API_URL.format(airport_code))
        response = {}
        if r.status == 200:
            response = json.loads(r.data)
            response = self._get_data_by_airport(response, airport_code)
        return response

    def airport_delays(self, airport_code):
        self.details.append(self._get_faa_data(airport_code))

    def _display(self):
        for airport in self.details:
            resp = airport
            print ("{}, {} ::: Delay (mins) : {} \nStatus : {}\nWeather : {}".format(
                resp.get('Name'),
            	resp.get('IATA'),
            	resp.get('Delay'),
            	resp.get('Status', 'NA'),
                resp.get('Weather'),
                )
            )


if len(sys.argv) != 3:
    airport_code = sys.argv[1].upper()
    re = AirportStatus(airport_code)
else:
    print(
    """
    Usage:

    > python faa.py JFK

    John F Kennedy Intl, JFK, New York ::: Delays : False 
    Status : No known delays for this airport
    Weather : [{'Temp': ['Mostly Cloudy']}]

    """)
