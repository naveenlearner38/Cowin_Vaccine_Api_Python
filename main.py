import requests
import json

cowin_requests = requests.get(
    "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=265&date=06-06-2021")

cowin_json = cowin_requests.json()

# print(cowin_json['centers'][0]['sessions'][0])

no_vaccines_available = True

for cowin_centers in cowin_json['centers']:
    if cowin_centers['fee_type'] == 'Free':
        for cowin_sessions in cowin_centers['sessions']:
            if(cowin_sessions['min_age_limit'] == 18):
                if(cowin_sessions['available_capacity'] > 0):
                    no_vaccines_available = False
                    print(cowin_sessions['available_capacity'])

if no_vaccines_available:
    print('No Vaccines Available')
