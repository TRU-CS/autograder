#!/usr/bin/env bash

# Update package lists and install GCC
apt-get update
apt-get install -y gcc make python3 python3-pip python3-dev

# Install Python dependencies
pip3 install -r /autograder/source/requirements.txt