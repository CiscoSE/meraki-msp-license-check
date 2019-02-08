import requests
import json
from meraki import meraki
       
api_key = input('Enter your Dashboard API key: ')
org_url = 'https://dashboard.meraki.com/api/v0/organizations'
meraki_headers = {'x-cisco-meraki-api-key': api_key, 'content-type': 'application/json'}
# get all of the organizations this api key has access to
Orgs = requests.get(org_url, headers=meraki_headers)
currentorgs = json.loads(Orgs.text)

Orgs_list={}

#Orgs = [{'id': 653307, 'name': 'Home'}, {'id': 533665, 'name': 'Scott'}]

print(currentorgs)

Orgs_list={}

number = 1

#Create dictionary of results from orgaccess
orgDict = {}
for entry in currentorgs:
	orgDict[number] = {'id':entry['id'], 'name':entry['name']}
	number += 1

keys = sorted(orgDict.keys())
for selection in keys:
	print('%s: %s: %s' % (str(selection),orgDict[selection]['id'], orgDict[selection]['name']))

mySelection = int(input('Select an org: '))

Org_Lic = requests.get('https://dashboard.meraki.com/api/v0/organizations/{0}/licenseState'.format(orgDict[mySelection]['id']), headers=meraki_headers)

licenses = json.loads(Org_Lic.text)
print('You are good until', ' :', licenses['expirationDate'])


