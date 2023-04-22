import configparser
import os


class ConfigReader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.config = configparser.ConfigParser()
            cls._instance.config.read(os.path.join(os.path.dirname(__file__), "..", "config.ini"))
        return cls._instance

    @classmethod
    def get_config(cls, key):
        return cls()._instance.config.get("DEFAULT", key)
