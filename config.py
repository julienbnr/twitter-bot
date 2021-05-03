import json

def get_twitter_credentials():
  return get_file_config('json/twitter_credentials.json')

def get_aws_config():
  return get_file_config('json/config.json')

def get_search_config():
  return get_file_config('json/search.json')

def get_file_config(file_name):
  with open(file_name) as config_json:
    config = json.load(config_json)
    return config
