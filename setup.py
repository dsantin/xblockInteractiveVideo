"""Setup for paellainteractivevideo XBlock."""

import os
from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='paellainteractivevideo-xblock',
    version='0.1.2',
    description='XBlock wich shows a interactive video with paella',
    packages=[
        'paellainteractivevideo',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'paellainteractivevideo = paellainteractivevideo:paellainteractiveXBlock',
        ]
    },
    package_data=package_data("paellainteractivevideo", "static"),
)