from pydantic import BaseModel
from typing import Tuple, List, Dict, Any
import yaml


class Adress(BaseModel):
    broker: str
    server: str
    client: str


class Settings(BaseModel):
    adress: Adress


with open("/app/config.yml") as f:
    data = yaml.safe_load(f)

settings = Settings(**data)