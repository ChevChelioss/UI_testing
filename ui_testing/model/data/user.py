import datetime
from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    birthday: datetime.date
    gender: str
    subject: str
    hobbies: str
    image: str
    state: str
    city: str