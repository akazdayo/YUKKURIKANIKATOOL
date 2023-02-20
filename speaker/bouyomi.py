import requests

def speak(text='', volume=-1, speed=-1, tone=-1):
    res = requests.get(
        'http://localhost:50080/Talk',
        params={
            'text': text,
            'voice': 1,
            'volume': volume,
            'speed': speed,
            'tone': tone})
    return res.status_code