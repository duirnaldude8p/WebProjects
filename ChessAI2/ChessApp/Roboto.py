import json

class Brain(object):
	data = open('ChessApp\static\json\playing_data.json')
	dictdata = json.load(data)
	statematrix = dictdata['StateData']['StateMatrix']
	compchoice = 'bpawn4'
	compmove = 'r5D'
	hasmoved = "Y"
	compInCheck = "N"
	compNWInCheck = "N"
	compNEInCheck = "N"
	compSWInCheck = "N"
	compSEInCheck = "N"
	compUpInCheck = "N"
	compDownInCheck = "N"
	compRightInCheck = "N"
	compLeftInCheck = "N"
	first = False
	sec = False
	third = False
	fourth = False
	fifth = False
	move6 = False
	move7 = False
	move8 = False
	move9 = False
	move10 = False
	move11 = False
	move12 = False
	checkmate = 'N'
	freemove = 'Y'
	currentDirectionArray = []
	attackerArray = []
	inGuard = 'N'
	pieceInGuard = ''
	spaceLength = 0;
	canSaveKing = ''
	savers = []
	attackers = []


	def _init_(self):
		data = open('ChessApp\static\json\playing_data.json')
		dictdata = json.load(data)
		self.statematrix = dictdata['StateData']['StateMatrix']
		self.compchoice = 'bpawn4'
		self.compmove = 'r5D'
		self.hasmoved = "Y"
		self.compInCheck = "N"
		self.compNWInCheck = "N"
		self.compNEInCheck = "N"
		self.compSWInCheck = "N"
		self.compSEInCheck = "N"
		self.compUpInCheck = "N"
		self.compDownInCheck = "N"
		self.compRightInCheck = "N"
		self.compLeftInCheck = "N"
		self.checkmate = 'N'
		self.freemove = 'Y'
		self.currentDirectionArray = []
		self.attackerArray = []
		self.inGuard = 'N'
		self.pieceInGuard = ''
		self.spaceLength = 0;
		self.canSaveKing = ''
		self.savers = []
		self.attackers = []
		self.first = False
		self.sec = True
		self.third = True
		self.fourth = True
		self.fifth = True
		self.move7 = True
		self.move8 = True
		self.move9 = True
		self.move10 = True
		self.move11 = True
		self.move12 = True

		#self.currentmatrix = []
		

	def processState(self, currentState):
		
		#self.currentmatrix = currentState
		
		
		if(currentState!=self.statematrix):
			#'''
			self.statematrix = currentState
			#print("human move before: %s - %s"%(self.statematrix[6][5], self.statematrix[4][5]))
			if not self.first:
				# self.compchoice = 'bpawn5'
				# self.compmove = 'r5E'
				# #print("first with elif: %s"%self.first)
				# self.statematrix[6][4].update(pieceId='') 
				# self.statematrix[4][4].update(pieceId='bpawn5')
				# #print("human move after: %s - %s"%(self.statematrix[6][5], self.statematrix[4][5]))
				self.compchoice = 'bpawn4'
				self.compmove = 'r6D'
				self.statematrix[6][3].update(pieceId='') 
				self.statematrix[5][3].update(pieceId='bpawn4')
				self.hasmoved = "Y"
				self.first = True
				self.sec = False
			elif not self.sec:
				self.compchoice = 'bpawn3'
				self.compmove = 'r5C'
				self.statematrix[6][2].update(pieceId='') 
				self.statematrix[4][2].update(pieceId='bpawn3')
				self.hasmoved = "Y"
				self.sec = True
				self.third = False
			elif not self.third:
				self.compchoice = 'bpawn5'
				self.compmove = 'r6E'
				self.statematrix[6][4].update(pieceId='') 
				self.statematrix[5][4].update(pieceId='bpawn5')	
				self.third = True
				self.fourth = False
			elif not self.fourth:
				self.compchoice = 'bqueen'
				self.compmove = 'r6F'
				self.statematrix[7][3].update(pieceId='') 
				self.statematrix[5][5].update(pieceId='bqueen')
				self.hasmoved = "Y"				
				self.fourth = True
				self.fifth = False
			elif not self.fifth:
				self.compchoice = 'bqueen'
				self.compmove = 'r3F'
				self.statematrix[5][5].update(pieceId='') 
				self.statematrix[1][5].update(pieceId='bqueen')
				self.hasmoved = "Y"
				self.fifth = True
				self.move6 = False
			elif not self.move6:
				self.compchoice = 'bpawn1'
				self.compmove = 'r6A'
				self.statematrix[6][0].update(pieceId='') 
				self.statematrix[5][0].update(pieceId='bpawn1')
				self.hasmoved = "Y"
				self.move6 = True
				self.move7 = False
			# elif not self.move7:
			# 	self.compchoice = 'bpawn7'
			# 	self.compmove = 'r5G'
			# 	self.statematrix[6][6].update(pieceId='') 
			# 	self.statematrix[4][6].update(pieceId='bpawn7')
			# 	self.hasmoved = "Y"
			# 	self.move7 = True
			# 	self.move8 = False
			# elif not self.move8:
			# 	self.compchoice = 'bpawn8'
			# 	self.compmove = 'r5H'
			# 	self.statematrix[6][7].update(pieceId='') 
			# 	self.statematrix[4][7].update(pieceId='bpawn8')
			# 	self.hasmoved = "Y"
			# 	self.move8 = True
			# 	self.move9 = False
			# #'''

			print("horay new state")
		else:
			self.hasmoved = "Y"
			print("same state")
		
		
	def setCompInCheck(self, comp, nw, ne, sw, se, up, down, right, left):
		self.compInCheck = comp
		self.compNWInCheck = nw
		self.compNEInCheck = ne
		self.compSWInCheck = sw
		self.compSEInCheck = se
		self.compUpInCheck = up
		self.compDownInCheck = down
		self.compRightInCheck = right
		self.compLeftInCheck = left
		print("hello robot ne: %s"%self.compNEInCheck)

	def setCheckInfo(self, chkmt, freemov, curdir, attarr, ingrd, pingrd, spclngth, csk, svrs, attckrs):
		self.checkmate = chkmt
		self.freemove = freemov
		self.currentDirectionArray = curdir
		self.attackerArray = attarr
		self.inGuard = ingrd
		self.pieceInGuard = pingrd
		self.spaceLength = spclngth
		self.canSaveKing = csk
		self.savers = svrs
		self.attackers = attckrs
		if len(curdir)>=2:
			print("curDir array: %s"%curdir[1])


	def getCompInCheck(self):
		return self.compInCheck

	def getCompNWInCheck(self):
		return self.compNWInCheck

	def getCompNEInCheck(self):
		return self.compNEInCheck

	def getCompSWInCheck(self):
		return self.compSWInCheck

	def getCompSEInCheck(self):
		return self.compSEInCheck

	def getCompUpInCheck(self):
		return self.compUpInCheck

	def getCompDownInCheck(self):
		return self.compDownInCheck

	def getCompRightInCheck(self):
		return self.compRightInCheck

	def getCompLeftInCheck(self):
		return self.compLeftInCheck

	def getState(self):
		return self.statematrix

	def getMove(self):
		return self.compmove

	def getChoice(self):
		return self.compchoice

	def getHasMoved(self):
		return self.hasmoved
	
	def getCheckMate(self):
		return self.checkmate

	def getFreeMove(self):
		return self.freemove

	def getCurrentDirectionArray(self):
		return self.currentDirectionArray

	def getAttackerArray(self):
		return self.attackerArray

	def getInGuard(self):
		return self.inGuard

	def getPieceInGuard(self):
		return self.pieceInGuard

	def getSpaceLength(self):
		return self.spaceLength

	def getCanSaveKing(self):
		return self.canSaveKing

	def getSavers(self):
		return self.savers

	def getAttackers(self):
		return self.attackers

