import requests

response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')

print(response.json())