#!/bin/sh
cat "input.txt" | openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
openssl x509 -in certificate.pem -noout -sha256 -fingerprint
