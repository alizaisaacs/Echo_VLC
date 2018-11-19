from flask import Flask, request, abort
import uuid, json, os, sys
import threading
from threading import Thread
from transmitter import main
from transmitter import turn_off, turn_on

trx = None
config = "/Users/alizaisaacs/transmitter/ledd.sh"
start_daemon = "./ledd.sh &"

app = Flask(__name__)
# app.config["DEBUG"] = TRUE

@app.route('/api/transmit/<uuid>', methods=['POST'])
def transmit(uuid):
        global trx
        
        # Kill deamon process
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
                trx = None
                os.system(start_daemon)
                return uuid
        else:
                return abort(400)
	# end thread

app.run()
