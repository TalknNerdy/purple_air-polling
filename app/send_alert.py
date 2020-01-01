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
    threshold = config_values["alert_value"].get(watch) or config_values["alert_value"]["default"]
    if data.get(watch) > threshold:
      return (watch, threshold)
  return None

bad_id = select_bad_id(data, config_values)

if bad_id:
  ifttt.send_alert(purple_air.human_friendly(bad_id[0]), data[bad_id[0]], bad_id[1])
else:
  print("no alert")