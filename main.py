import app.ifttt as ifttt
import app.purple_air as purple_air
import config

config_values = config.load_config()
data = purple_air.get_data()

if not(len(data)):
  print("no data")
  exit()

def select_bad_id(data, config_values):
  watch_fields = config_values["watch_fields"]
  for field, field_config in watch_fields.items():
    field_config = field_config or {}
    threshold = field_config.get("alert_above") or config_values["default_alert_above"]
    if data.get(field) > threshold:
      title = field_config.get("title", field)
      unit = field_config.get("unit")
      value = " ".join(filter(None, (str(data.get(field)), unit)))
      return (title, value, threshold)
  return None

bad_id = select_bad_id(data, config_values)

if bad_id:
  ifttt.send_alert(bad_id[0], bad_id[1], bad_id[2])
else:
  print("no alert")