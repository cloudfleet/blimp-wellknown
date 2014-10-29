from debian:wheezy


run (apt-get update && apt-get install -y python python-flask)
copy . /opt/cloudfleet/app
workdir /opt/cloudfleet/app

cmd python -u wellknown.py

expose 80