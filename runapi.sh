#!/bin/sh

iptables -A INPUT -p tcp --dport 5000 -j ACCEPT
/home/root/venv/bin/python /home/root/echo_API.py
