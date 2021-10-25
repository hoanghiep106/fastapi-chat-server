import os

from dotenv import load_dotenv


class Config:
    MONGO_URI: str = "mongodb://localhost:27017"
    MAX_POOL_CONNECTIONS: int = 100
    DEFAULT_PAGE_LIMIT: int = 10

    def __init__(self):
        # Support parsing string and integer env correctly
        load_dotenv()
        for attr in dir(self):
            if not attr.isupper():
                continue
            default_value = getattr(self, attr)
            value_type = type(default_value)
            value = os.getenv(attr) or default_value
            value = value_type(value)
            setattr(self, attr, value)
