import requests
import json

token = "7045da5c4078427e94184d101f6f0b9f"
city_name = "São Paulo"
state = "SP"
city_id_url = f"http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={city_name}&state={state}&token={token}"
response = requests.request("GET", city_id_url)
response = json.loads(response.text)
response = response[0]
city_id = response["id"]
print(response)

register_city_url = f"http://apiadvisor.climatempo.com.br/api-manager/user-token/{token}/locales'"
payload = f"localeId[]={city_id}"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
response = requests.request("PUT", register_city_url, headers=headers, data=payload)
print(response)


# climate_url = f"http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{city_id}/current?token={token}"
# response = requests.request("GET", climate_url)
# response = json.loads(response.text)
# print(response)


