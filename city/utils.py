from datetime import datetime

import requests


def get_weather(lat, lon):
    API_URL = f'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon=-{lon}'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;"}
    response = requests.get(API_URL, headers=headers)
    data = response.json()
    time_series = data['properties']['timeseries']

    now = datetime.now()
    index = -1

    for i in range(0, len(time_series) - 1):
        date = datetime.strptime(time_series[i]['time'], "%Y-%m-%dT%H:%M:%S%z")
        if date.date() >= now.date():
            index = i
            break

    if index == -1:
        return None

    time_series = time_series[index:]
    return time_series[1]


if __name__ == '__main__':
    print(get_weather('0.347596', '32.582520'))
