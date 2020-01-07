import requests
import json 
import os
import re

# See sample.json to understand format
def get_data():
  id = os.environ['purpleair_ID']
  key = os.environ['purpleair_KEY']
  params = (
      ('key', key),
      ('show', id),
  )
  response = requests.get('https://www.purpleair.com/data.json', params=params)
  if response.status_code == 429:
    print("purple_air - 429 error")
    return {}
  elif not(response.status_code == 200):
    print("purple_air - unknown error", response.text)
    return {}
  text = response.text
  print(f"purple_air status={response.status_code}; text={text}")

  # sometimes they put a *** instead of the id, making the JSON invalid
  re.sub(r'\*{3}', '\"***\"', text)
  data = json.loads(text)

  return _format_data(data)

def _format_data(data):
  return dict(zip(data["fields"], data["data"][0]))
