from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Job:
    company_name: str
    title: str
    date_posted: date
    salary: str
    location: str
    description: str
    url: str
    tags: str
    website: str
