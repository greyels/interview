import requests

USGS_ENDPOINT = "https://earthquake.usgs.gov/fdsnws/event/1/query"


def fetch_data(start_time, end_time):
    params = {
        "format": "geojson",
        "starttime": start_time.strftime("%Y-%m-%d"),
        "endtime": end_time.strftime("%Y-%m-%d"),
    }
    response = requests.get(USGS_ENDPOINT, params=params)
    return response.json()
