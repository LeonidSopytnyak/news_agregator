import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / 'conf.yaml'


class ConfigLoader:
    @staticmethod
    def load_config():
        with open(CONFIG_PATH, 'r') as conf:
            try:
                config = yaml.safe_load(conf)
                return config
            except yaml.YAMLError as exc:
                print(exc)
