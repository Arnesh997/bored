import requests


url = 'http://www.boredapi.com/api/activity/'
def activitygenerator():
    Data = requests.get(url)
    json_data = Data.json()
    activity_Data = json_data['activity']
    activity_type = json_data['type']
    print(activity_Data)
    print(activity_type)

for (i) in range(0, 10):
    activitygenerator()