# Installation

Copy the "christmaslights" directory to your Raspberry Pi. It contains the Python Flask app which controls the RGB LED strip lights.

## Local Access

Within the local network, you'll access this Flask app under `<Raspberry Pi's IP Address>/christmaslights:5001`

### Install Flask and uwsgi

If Flask is not installed already, change to the directory `christmaslights/Lightsapp` and install it with:

    sudo pip install -r requirements

If uwsgi is not installed, install it with:

    sudo pip install uwsgi

## How to start Flask app

To run this Flask app, change to the directory `christmaslights` and run this:

    uwsgi uwsgi.ini

## How to stop Flask app

To kill this Flask app, run this:

    killall -s INT /usr/local/bin/uwsgi

## Nginx as reverse proxy

You can have Nginx or any other web server as a reverse proxy to take incoming HTTP requests on the Raspberry Pi. Configure `nginx.conf` to route all `/christmaslights` requests to the Flask app.

## {Remote} Access the Flask app from outside the home network

You have to set port forwarding on your router so that any incoming TCP connections to the router IP at port 8001 will forward to the Raspberry Pi's IP address at port 5001.
