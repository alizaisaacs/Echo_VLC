#!/bin/sh

iptables -A INPUT -p tcp --dport 5000 -j ACCEPT
/home/root/venv/bin/python echo_API.py
