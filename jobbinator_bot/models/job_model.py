from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Job:
    company_name: str
    jobTitle: str
    datePosted: date
    salary: str
    location: str
    job_description: str
    url: str
    tags: str
