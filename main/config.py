import os

from dotenv import load_dotenv


class Config:
    MONGO_URI: str = "mongodb://localhost:27017"
    DEFAULT_PAGE_LIMIT: int = 10

    def __init__(self):
        load_dotenv()
        for attr in dir(self):
            if not attr.isupper():
                continue
            default_value = getattr(self, attr)
            value_type = type(default_value)

            value = os.getenv(attr) or default_value

            if value and isinstance(default_value, list) and isinstance(value, str):
                value = value.split(",")
            elif value_type is bool and isinstance(value, str):
                value = value.lower() in ["true", "yes", "t", "i", "1"]
            else:
                value = value_type(value)

            setattr(self, attr, value)
