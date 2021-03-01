import http.client
import json


def request_random_number_face(number):
    number = int(number)

    conn = http.client.HTTPSConnection("numbersapi.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "8736ff2b2emsh87f1617c53d4b65p1a7121jsn4b29408aeb9d",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
    }

    conn.request("GET", "/" + str(number) + "/trivia?fragment=true&notfound=floor&json=true", headers=headers)

    res = conn.getresponse()
    data = res.read().decode('utf-8')
    json_data = json.loads(data)

    if json_data['number'] != number:
        json_data['error'] = 'No fact was found for the number \'' + str(number) + '\''

    return json_data
