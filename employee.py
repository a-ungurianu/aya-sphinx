from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    """Name of the employee"""
    job_title: str
    """Job title"""

