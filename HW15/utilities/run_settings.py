import configparser
import os

from HW15.CONSTS import ROOT_DIR

abs_path = os.path.abspath(fr"{ROOT_DIR}/configurations/configuration.ini")
config = configparser.RawConfigParser()
config.read(abs_path)


class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_driver_id():
        return config.get('browser', 'browser_id')

    @staticmethod
    def get_api_url():
        return config.get('app_info', 'api_url')

    @staticmethod
    def get_test_password():
        return config.get('app_info', 'test_password')
