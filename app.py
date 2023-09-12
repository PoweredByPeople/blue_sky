import requests
import environment


def main():

    API_KEY=environment.APIKEY
    URL="https://ridb.recreation.gov/api/v1/"
    ENDPOINT="activities"
    headers = {"accept": "application/json", "apikey": API_KEY}

    request_url = f"{URL}/{ENDPOINT}"

    response = requests.get(request_url, headers=headers, params={"limit":50, "offset": 5})

    print(response.text) 

main()