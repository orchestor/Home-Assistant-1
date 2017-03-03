#!/usr/bin/python
import time
import logging
from datetime import datetime
import os
# Custom modules
import hue
import device
import inspect
"""
Level		Numeric value
CRITICAL	50
ERROR		40
WARNING		30
INFO		20
DEBUG		10
NOTSET		0
"""


class Main(object):

	running = True

	def __init__(self):
		self.initLogger()
		self.hue = hue.Hue()
		self.scott = device.Device("20:62:74:01:D7:9C", "Scott")

	# Configures and initiates the Logging library
	def initLogger(self):
		date = datetime.now().strftime("%d_%m_%y")
		month = datetime.now().strftime("%m")
		day = datetime.now().strftime("%d")
		# Logging
		self.log = logging.getLogger()
		self.log.setLevel(logging.DEBUG)
		format = logging.Formatter(fmt = "%(asctime)s - %(module)s - %(levelname)s: %(message)s", datefmt = "%d-%m-%Y %H:%M")
		# For screen logging
		screen = logging.StreamHandler()
		screen.setLevel(logging.DEBUG)
		screen.setFormatter(format)
		self.log.addHandler(screen)
		# Check if log folder exists, create it if not
		log_dir = os.getcwd() + "/logs"
		if not os.path.exists(log_dir):
			os.makedirs(log_dir)
			self.log.debug("Creating log dir: %s" % log_dir)
		# For file logging
		logfile = logging.FileHandler("logs/ha-%s.log" % date)
		logfile.setLevel(logging.WARNING)
		logfile.setFormatter(format)
		self.log.addHandler(logfile)

	def start(self):
		try:
			prev_state = None
			while self.running:
				if(self.scott.getDeviceStatus()):
					state = 1
					self.hue.randomiseGroup()
				else:
					state = 0

				time.sleep(1)

				if prev_state != state:
					prev_state = state
					self.hue.changeState()

		except KeyboardInterrupt:
			self.log.error("Program interrupted")


if __name__ == "__main__":
	Main().start() 
