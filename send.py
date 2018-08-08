import requests

for x in range(0,10000):
    url = "http://127.0.0.1:8000/clients/"

    payload = "{\n\t\"name\":\"Hamdan\",\n\t\"email\":\"hamdann"+ str(x) +"@qwords.co.id\",\n\t\"phone\":\"628112243016\"\n}"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTMzNjQwMTg3LCJqdGkiOiJhNjRlYWQ4OTI4ZWQ0NDkzYmVlNDc5MjBiN2ExOWE0MSIsInVzZXJfaWQiOjF9.gcOddkbS0VsfnVrms9GoKfuvHen4ILm5e1ADflsaFfA",
        'Cache-Control': "no-cache",
        'Postman-Token': "203db869-1c5f-4b24-a3b2-02542cfdf2d6"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)