from pydantic import BaseModel
from typing import Tuple, List, Dict, Any
import yaml
import os


class Adress(BaseModel):
    broker: str
    server: str
    client: str


class Settings(BaseModel):
    adress: Adress


try: 
    with open("/app/config.yml") as f:
        data = yaml.safe_load(f)

except:
    with open("config.yml") as f:
        data = yaml.safe_load(f) 

settings = Settings(**data)