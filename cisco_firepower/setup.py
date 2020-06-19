# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="cisco_firepower-rapid7-plugin",
      version="1.0.2",
      description="This plugin utilizes Cisco Firepower to add scan results from a third-party vulnerability scanner Cisco Firepower is a Next-Generation Firewall (NGFW) with NGIPS, incorporating access and application control, threat prevention and firewall capabilities",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_cisco_firepower']
      )
