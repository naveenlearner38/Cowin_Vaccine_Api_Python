import requests
from pynotifier import Notification


cowin_requests = requests.get(
    "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=265&date=06-06-2021")

cowin_json = cowin_requests.json()

no_vaccines_available = True


def notification(title, message):
    Notification(
        title=title,
        description=message,
        # On Windows .ico is required, on Linux - .png
        icon_path='path/to/image/file/icon.png',
        duration=5,                              # Duration in seconds
        urgency='normal'
    ).send()


def checkVaccineAvailability():
    for cowin_centers in cowin_json['centers']:
        if cowin_centers['fee_type'] == 'Free':
            for cowin_sessions in cowin_centers['sessions']:
                if(cowin_sessions['min_age_limit'] == 18):
                    if(cowin_sessions['available_capacity'] > 0):
                        no_vaccines_available = False
                        print(cowin_sessions['available_capacity'])


if __name__ == "__main__":

    while True:

        checkVaccineAvailability()

        # notification(title='Notification Title', message='Notification Description')

        if no_vaccines_available:
            print('No Vaccines Available')
