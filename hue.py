#!/usr/bin/python
import pyhue
from random import randint
import logging


class Hue(object):

	bridge_ip = "192.168.1.166"
	bridge_user = "AB8orc63WWaI4-qI8KshwpTlTkPNZslmVNYKq6X2"

	def __init__(self):
		self.log = logging.getLogger(type(self).__name__)
		self.log.debug("Initiating Hue located at %s" % self.bridge_ip)
		self.bridge = pyhue.Bridge(self.bridge_ip, self.bridge_user)
		self.lights = self.bridge.lights
		self.groups = self.bridge.groups
		self.status = True

	def randomiseLight(self):
		hue = randint(0, 65000)
		self.log.debug("Setting light to %s" % hue)
		for light in self.lights:
			light.hue = hue
			
	def randomiseGroup(self):
		hue = randint(0, 65000)
		self.log.debug("Setting group to %s" % hue)
		for group in self.groups:
			group.hue = hue

	def changeState(self):
		self.log.debug("Changing lights state")
		if self.status:
			self.turnOff()
		else:
			self.turnOn()

	def turnOn(self):
		self.log.debug("Turning all lights on")
		self.status = True
		for group in self.groups:
			group.on = True
	
	def turnOff(self):
		self.log.debug("Turning all lights off")
		self.status = False
		for group in self.groups:
			group.on = False
