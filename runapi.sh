#!/bin/sh
. venv/bin/activate
pip install -i https://pypi.python.org/simple/ flask
iptables -A INPUT -p tcp --dport 5000 -j ACCEPT
python echo_API.py
