import json

people_string = '''
{
    "people": [
        {
            "name": "boss",
            "phone": "554-3333",
            "emails": null,
            "has_license": true
        },
        {
            "name": "sara",
            "phone": "111-1133",
            "emails": ["sahh@naver.com", "abc11@gmail.com"],
            "has_license": false
        }
    ]
}
'''
#-----------------------------------------
'''json object explain, loads and dumps'''
# data = json.loads(people_string)
# print(type(data))
# print(type(data["people"]))

# for person in data['people']:
#     print(person['name'])

# for person in data['people']:
#     del person['phone']

# new_string = json.dumps(data, indent=2, sort_keys=True)

# print(new_string)

#-----------------------------------------------
'''json file load and reform data then save as newfile'''
# with open('states.json') as f:
#     data = json.load(f)

# for state in data['states']:
#     print(state['name'], state['abbreviation'])
#     del state['area_codes']

# with open('new_states.json', 'w') as f:
#     json.dump(data, f, indent=4)
    
#-------------------------------------------------------
'''using real world data practice(yahoo finance)'''

from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=4))

print(len(data['list']['resources']))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(usd_rates['USD/EUR'])
