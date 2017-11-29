import json

CONFIG_FILE = '../config.json'


def __load_config__(config_file):
    """
    Load and parse JSON file with configuration.
    :param config_file: JSON config file
    :return: parsed JSON object
    """
    return json.loads(open(config_file, 'r').read())


def get_video_file_name():
    """
    Obtain relative path to video file.
    :return: String with file path
    """
    config = __load_config__(CONFIG_FILE)
    return config['video_path']


def get_camera_addr():
    """
    Obtain address of RTSP camera.
    :return: String with camera address
    """
    config = __load_config__(CONFIG_FILE)
    return config['camera_addr']


def get_lanes_obj():
    """
    Get configuration of lanes.
    :return: Object with lanes configuration
    """
    config = __load_config__(CONFIG_FILE)
    return config['lanes']


def get_save_format():
    """
    Get format for saving statistic info.
    :return: String specifying save format
    """
    config = __load_config__(CONFIG_FILE)
    return config['save_format']


def get_save_file_name():
    """
    Get file name, including full path, of file to which statistics will be saved.
    :return: File path
    """
    config = __load_config__(CONFIG_FILE)
    return config['stat_file_name']


def get_small_vehicle_size():
    """
    Get size of small vehicle.
    :return: Number specifying size of small vehicle
    """
    config = __load_config__(CONFIG_FILE)
    sizes = config['vehicle_sizes']

    for size in sizes:
        if 'small' in size:
            return size['small']


def get_large_vehicle_size():
    """
    Get size of large vehicle.
    :return: Number specifying size of large vehicle
    """
    config = __load_config__(CONFIG_FILE)
    sizes = config['vehicle_sizes']

    for size in sizes:
        if 'large' in size:
            return size['large']
