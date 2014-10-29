#! /bin/bash

apt-get update && \
apt-get upgrade -y && \
apt-get install python-pip -y && \
(cd /vagrant && pip install -r requirements.txt)
