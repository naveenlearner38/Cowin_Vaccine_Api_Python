import requests
from pynotifier import Notification
from datetime import datetime,timedelta
# Manually need to change district id
district_id = '293'
# Need to create 8 days array from current data format: DD-MM-YYYY
# current_date = datetime.today().strftime('%d-%m-%Y')
# end_date = current_date + datetime.timedelta(days=10)
# print(end_date)


# create requests as a function

def getData(getDate):
    cowin_requests = requests.get(
    "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+district_id+"&date="+getDate+"")
    cowin_json = cowin_requests.json()
    return cowin_json


no_vaccines_available = True


def notification(title, message):
    Notification(
        title=title,
        description=message,
        # On Windows .ico is required, on Linux - .png
        icon_path='images/logo_1.ico',
        duration=5,                              # Duration in seconds
        urgency='normal'
    ).send()


def checkVaccineAvailability(covid_json):
    for cowin_centers in covid_json['centers']:
        if cowin_centers['fee_type'] == 'Free':
            for cowin_sessions in cowin_centers['sessions']:
                if(cowin_sessions['min_age_limit'] == 18):
                    if(cowin_sessions['available_capacity'] > 0):
                        # Don't need to use global function or variables
                        no_vaccines_available = False
                        # Hospital Detail
                        # Call the Notification in messge
                        print()
                        notification(title='covid 19 vaccine', message=cowin_centers['name']+' '+'Hospital has covid 19 vaccines');

                        # print(cowin_sessions['available_capacity'])


if __name__ == "__main__":

    # while True:

    today = datetime.now()
    for i in range(0,8):
        day = today + timedelta(days=i)
        # print(day.strftime("%d-%m-%Y"))
        json = getData(day.strftime("%d-%m-%Y"))

        checkVaccineAvailability(json)


    if no_vaccines_available:
        print('No Vaccines Available')

    # After 1 Min need check again