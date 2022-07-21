import yaml
import sys
from housing.exception import HousingException
def read_yaml(path:str) -> dict:
    try:
        with open(path) as f1:
            d=yaml.safe_load(f1)
        return d
    except Exception as e:
        raise HousingException(e,sys) from e