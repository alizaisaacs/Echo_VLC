from flask import Flask, request, abort
import uuid, json, os, sys
import threading
from threading import Thread
from echo_transmitter import main
from echo_transmitter import turn_off, turn_on

trx = None
config = "/sys/devices/platform/omap/omap_i2c.2/i2c-2/2-0032/all_leds"
start_daemon = "/usr/local/bin/ledd &"

app = flask.Flask(__name__)

	
@app.route('/api/transmit/<uuid>', methods=['POST'])
def transmit(uuid):
	global trx
	
	# Kill daemon process
	os.system("if (fuser %s); then kill -9 $(fuser %s); fi" % (config, config))

	# Extract FPS and start transmission using that value
	data = request.get_json()
	fps = data['FPS']
	
	if trx is None:
		turn_on()
		trx = threading.Thread(target = main, args = (fps,))
		trx.start()
	else:
		return abort(400)
	# Return session ID
        return uuid

@app.route('/api/off/<uuid>', methods=['POST'])
def off(uuid):
	global start_daemon
	global trx
	
	# Terminate transmission and return to original state
	if trx is not None:
		turn_off()
		trx.join()
		os.system(start_daemon) 
		return uuid
	else:
		return abort(400)
	# end thread


if __name__ == "__main__":
    app.run(host='0.0.0.0')

