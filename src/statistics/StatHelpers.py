import json
import os
import errno


class StatHelper:
    """
        Provides methods to work with statistics data.
    """

    def __init__(self):
        self.small_vehicles_count = {
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0
        }

        self.large_vehicles_count = {
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0
        }

        self.all_vehicles_count = {
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0
        }

    def increase_small_count(self, lane_num):
        """
        Increase number of small vehicles on specified lane.
        :param lane_num: Lane Number
        """
        self.small_vehicles_count[lane_num] += 1

    def increase_large_count(self, lane_num):
        """
        Increase number of large vehicles on specified lane.
        :param lane_num: Lane Number
        """
        self.large_vehicles_count[lane_num] += 1

    def increase_all_count(self, lane_num):
        """
        Increase number of all vehicles on specified lane.
        :param lane_num: Lane Number
        """
        self.all_vehicles_count[lane_num] += 1

    def get_small_count(self, lane_num):
        """
        Receive number of small vehicles on specified lane.
        :param lane_num: Lane Number
        :return: Number of vehicles
        """
        return self.small_vehicles_count[lane_num]

    def get_large_count(self, lane_num):
        """
        Receive number of large vehicles on specified lane.
        :param lane_num: Lane Number
        :return: Number of vehicles
        """
        return self.large_vehicles_count[lane_num]

    def get_all_count(self, lane_num):
        """
        Receive number of all vehicles on specified lane.
        :param lane_num: Lane Number
        :return: Number of vehicles
        """
        return self.all_vehicles_count[lane_num]

    def write_stat_to_file(self, filename):
        """
        Writes statistics data to provided file path.
        :param filename: Path to file to which statistics data will be written
        """
        result = {
            'small_vehicles_count': self.small_vehicles_count,
            'large_vehicles_count': self.large_vehicles_count,
            'all_vehicles_count': self.all_vehicles_count
        }

        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        # Writing JSON data
        with open(filename, 'w') as f:
            json.dump(result, f)
