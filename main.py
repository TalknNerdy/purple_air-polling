import app.ifttt as ifttt
import app.purple_air as purple_air
import config

config_values = config.load_config()
data = purple_air.get_data()

if not(len(data)):
  print("no data")
  exit()

def select_bad_id(data, config_values):
  for watch in config_values["watch_fields"]:
    expected = config_values["alert_value"].get(watch) or config_values["alert_value"]["default"]
    if data.get(watch) > expected:
      return watch
  return None

watch = select_bad_id(data, config_values)

if watch:
  ifttt.send_alert(watch, data[watch])
else:
  print("no alert")