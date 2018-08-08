from __future__ import print_function
from runner import Runner
import configparser


class OpenscapGatherer:
    """Base class for openscap_gatherer
    """

    def __init__(self, config_file, debug=False):
        """Constructor for openscap_gatherer

        Args:
            config(str): Path to the config file

        Kwargs:
            debug(bool): Whether to print debug info

        """

        self.config_file = config_file
        self.debug = debug
        self.runner = Runner(self.read_config(), debug=self.debug)

    def read_config(self, config_file=None):
        config = configparser.ConfigParser()
        if config_file is None:
            config_file = self.config_file

        if self.debug:
            print("[openscap_gatherer] - Reading file - ", config_file)
        config.read(config_file)
        self.policy_uuid = config['compliance']['policy_uuid']
        self.profile = config['compliance']['profile']
        self.content_path = config['compliance']['content_path']
        self.tailoring_path = config['compliance']['tailoring_path']
        return dict(config['compliance'])

    def run_scan(self):
        self.runner.scan()

    def upload_files(self, files):
        # HHHHHHACKHHHHHHH - URL should be provided by config file
        url = "http://localhost:8080/api/v1/upload"
        print(url)
        # HHHHHHACKHHHHHHH - URL should be provided by config file
        # uploader = Uploader(files, self.runner.results_path, url,
        #                     debug=self.debug)
        # zipped_filepath = uploader.zip()
        # upload_result = uploader.upload(zipped_filepath)
