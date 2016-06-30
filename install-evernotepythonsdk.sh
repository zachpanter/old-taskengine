#!/bin/bash

# Install the Evernote SDK to allow Travis CI builds to function correctly
git clone https://github.com/zachpanter/evernote-sdk-python.git
cd evernote-sdk-python
python setup.py install