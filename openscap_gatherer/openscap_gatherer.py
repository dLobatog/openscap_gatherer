from __future__ import print_function
import configparser


class OpenscapGatherer:
    """Base class for openscap_gatherer
    """

    def __init__(self, config_file, debug=True):
        """Constructor for openscap_gatherer

        Args:
            config(str): Path to the config file

        Kwargs:
            debug(bool): Whether to print debug info

        """

        self.config_file = config_file
        self.debug = debug
        self.read_config()

    def read_config(self, config_file=None):
        config = configparser.ConfigParser()
        config_file = config_file if config_file is not None else self.config_file
        if self.debug:
            print("[openscap_gatherer] - Reading file - ", config_file)
        config.read(config_file)
        self.policy_uuid = config['compliance']['policy_uuid']
        self.profile = config['compliance']['profile']
        self.content_path = config['compliance']['content_path']
        return config['compliance']
