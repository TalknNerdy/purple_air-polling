import yaml

def load_config():
  with open('config.yaml') as file:
    return yaml.load(file, Loader=yaml.FullLoader)
