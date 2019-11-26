import os
from setuptools import setup

setup(
    name = "ilforcefields",
    version = "0.0.0",
    author = "Matt Thompson",
    author_email = "matt.thompson@vanderbilt.edu",
    description = ("A collection of ionic liquid forcefields and builders"),
    entry_points={
        "foyer.forcefields": [
            "load_LOPES = ilforcefields.ilforcefields:load_LOPES",
            "load_KPL = ilforcefields.ilforcefields:load_KPL",
            "load_NGKPL = ilforcefields.ilforcefields:load_NGKPL",
        ],
    },
)
