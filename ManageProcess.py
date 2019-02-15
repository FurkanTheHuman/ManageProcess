import subprocess
import os
from subprocess import Popen, PIPE, STDOUT
import time

class ManageProcess():
	is_verbose = True
	process = None
	pid = 0
	def __init__(self, is_verbose = True, arglist=""):
		if arglist is not "":
			self.start_process(arglist,is_verbose)

	def is_open(self, wait_for_termination=0):
		try:
			time.sleep(wait_for_termination)
			if self.process.poll() is None:
				return True
			elif self.process.poll() is 0:
				return False
			
		except AttributeError:
			return False

	def start_process(self, arglist, is_verbose = True):
		self.is_verbose = is_verbose
		arglist = arglist.split(" ")
		try:
			if self.process is None:
				if len(arglist) > 0 and is_verbose:
					self.process = subprocess.Popen(arglist, shell=False)
					self.pid = self.process.pid	
				elif len(arglist) > 0:
					DEVNULL = open(os.devnull, 'wb')
					self.process = subprocess.Popen(arglist, stdin=PIPE, stdout=DEVNULL, stderr=STDOUT, shell=False, bufsize=1)
			else:
				self.terminate()
				raise Exception('There are already open processes!')
		except OSError:
			raise OSError('Unrecognized command')			

	def terminate(self):
		self.process.terminate()
		
		returncode = self.process.wait()
		print "Terminated. Return value: %s" %returncode
		return returncode
	#important note use Popen pid to see pid

