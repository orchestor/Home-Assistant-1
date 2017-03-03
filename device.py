#!/usr/bin/python
import bluetooth
import logging


class Device(object):

	def __init__(self, address, owner):
		self.log = logging.getLogger(type(self).__name__)
		self.address = address
		self.owner = owner
		self.log.debug("Initiating Device %s (%s)" % (self.owner, self.address))

	def getDeviceStatus(self):
		self.log.debug("Getting status for device %s (%s)" % (self.owner, self.address))
		if bluetooth.lookup_name(self.address, 5) is not None:
			self.log.debug("%s is home" % self.owner)
			self.status = True
			return True
		else:
			self.log.debug("%s has gone out!" % self.owner)
			self.status = False
			return False
