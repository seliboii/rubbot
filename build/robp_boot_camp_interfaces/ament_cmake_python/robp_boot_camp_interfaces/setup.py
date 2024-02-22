from setuptools import find_packages
from setuptools import setup

setup(
    name='robp_boot_camp_interfaces',
    version='1.0.0',
    packages=find_packages(
        include=('robp_boot_camp_interfaces', 'robp_boot_camp_interfaces.*')),
)
