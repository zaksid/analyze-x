import json

CONFIG_FILE = '../config.json'


def load_config(config_file):
    return json.loads(open(config_file, 'r').read())


def get_file_name():
    config = load_config(CONFIG_FILE)
    return config['video_path']

def get_lanes():
    config = load_config(CONFIG_FILE)
    return config['lanes']
