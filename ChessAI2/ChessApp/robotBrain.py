class robotBrain(object):
	
	def _init_(self):
		self.compMovesTo = 'r5H'
		self.compChooses = 'bpawn8'

	def processState(self, counter):
		if counter == 1:
			self.compMovesTo = 'r5B'
			self.compChooses = 'bpawn2'
		elif counter == 2:
			self.compMovesTo = 'r4B'
			self.compChooses = 'bpawn2'
		elif counter == 3:
			self.compMovesTo = 'r3B'
			self.compChooses = 'bpawn2'
		elif counter == 4:
			self.compMovesTo = 'r5C'
			self.compChooses = 'bpawn3'

	def getRobChs(self):
		return self.compChooses
	
	def getRobMvTo(self):
		return self.compMovesTo


