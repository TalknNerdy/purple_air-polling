import requests
import json
import os

headers = {
    'Content-Type': 'application/json',
}

def send_alert(id, value):
  event_name = os.environ['ifttt_EVENT_NAME']
  key = os.environ['ifttt_KEY']
  url = f'https://maker.ifttt.com/trigger/{event_name}/with/key/{key}'
  response = requests.post(url, headers=headers, data=json.dumps({'high_id': id, 'high_value': value}))
  print("sent alert", id, value)