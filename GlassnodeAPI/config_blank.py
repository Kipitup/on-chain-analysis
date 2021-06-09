from configparser import ConfigParser

config = ConfigParser()

config.add_section('main')
config.set('main', 'API_KEY', '')

with open('config_file.ini','w+') as f:
    config.write(f)