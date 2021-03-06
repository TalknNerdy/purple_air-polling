import requests
import json
import os

headers = {
    'Content-Type': 'application/json',
}

def send_alert(id, value, threshold):
  event_name = os.environ['ifttt_EVENT_NAME']
  key = os.environ['ifttt_KEY']
  url = f'https://maker.ifttt.com/trigger/{event_name}/with/key/{key}'
  response = requests.post(url, headers=headers, data=json.dumps({'value1': id, 'value2': value, 'value3': threshold}))
  print(response.text)
  print("sent alert", id, value, threshold)