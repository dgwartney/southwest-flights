#!/usr/bin/env python
import requests

url = "https://www.southwest.com/api/air-booking/v1/air-booking/page/air/booking/shopping"

payload = "{\"originationAirportCode\":\"SJC\",\"destinationAirportCode\":\"DEN\",\"departureDate\":\"2018-08-16\",\"returnDate\":\"2018-08-19\",\"departureTimeOfDay\":\"ALL_DAY\",\"returnTimeOfDay\":\"ALL_DAY\",\"adultPassengersCount\":\"1\",\"seniorPassengersCount\":\"0\",\"tripType\":\"roundtrip\",\"fareType\":\"USD\",\"passengerType\":\"ADULT\",\"redirectToVision\":\"true\",\"leapfrogRequest\":\"true\",\"application\":\"air-booking\",\"site\":\"southwest\"}"
headers = {
    'accept-language': "en-US,en;q=0.9",
    'accept-encoding': "gzip, deflate, br",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    'content-type': "application/json",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'x-api-key': "l7xx944d175ea25f4b9c903a583ea82a1c4c",
    'x-channel-id': "southwest",
    'Cache-Control': "no-cache",
    'Postman-Token': "65db086c-e50f-4b00-8e5c-635570a2abcb"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
