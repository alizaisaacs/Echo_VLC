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
	led1 = open(os.path.join("/sys/devices/platform/omap/omap_i2c.2/i2c-2/2-0032",
		"all_leds"), "w")                                      
	led2 = open(os.path.join("/sys/devices/platform/omap/omap_i2c.2/i2c-2/2-0033",
		"all_leds"), "w")                                      
	led3 = open(os.path.join("/sys/devices/platform/omap/omap_i2c.2/i2c-2/2-0034",
		"all_leds"), "w")                                      
	led4 = open(os.path.join("/sys/devices/platform/omap/omap_i2c.2/i2c-2/2-0035",
		"all_leds"), "w")
 
	# Open JSON file
	with open('/home/root/data.json', 'r') as json_data:
		data = json.load(json_data)   
 
	# ColorValues class to store JSON data
	class ColorValues:
		def __init__(self, red, green, blue):
			self.red = red
			self.green = green
			self.blue = blue
		def __str__(self):
			return  "%d %d %d %d %d %d %d %d %d" %(self.green,
				self.blue, self.green, self.blue, self.green,
				self.blue, self.red, self.red, self.red)
 
	# Add JSON data variables to a list
	data_list = []
	for string in data:
		red = int(string[1:3], 16)
		green = int(string[3:5], 16)
		blue = int(string[5:7], 16)
		cv = ColorValues(red, green, blue)
		data_list.append(cv)
 
	sleep_time = float(fps)
 
	# If input is positive, print JSON data to the LEDs                                   
	sleep_time = 1/sleep_time
	
	while not set_off:
		for cv in data_list:
			if set_off:
				break
			led1.write(str(cv))
			led1.truncate()
			led2.write(str(cv))
			led2.truncate()
			led3.write(str(cv))
			led3.truncate()
			led4.write(str(cv))
			led4.truncate()
			time.sleep(sleep_time)
 
if __name__ == "__main__":
	main(sys.argv[1])
