#!/usr/bin/python       
import os, time, signal, json, sys

set_off = False

def turn_off():
	global set_off 
	set_off = True
def turn_on():
	global set_off
	set_off = False

def main(fps):
	global set_off
	while not set_off:
		print(fps)
		time.sleep(2)
if __name__ == "__main__":
        main(sys.argv[1]) 
