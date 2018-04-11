import json

class Brain(object):
	data = open('static\json\playing_data.json')
	dictdata = json.load(data)
	statematrix = dictdata['StateData']['StateMatrix']
	compchoice = ''
	compmove = ''
	hasmoved = "N"
	compremove = ''
	hasremoved = 'N'
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
	piecesRemovedList = []
	currentDirectionArray = []
	attackerArray = []
	inGuard = 'N'
	pieceInGuard = ''
	spaceLength = 0;
	canSaveKing = ''
	kingHasMoved = 'N'
	rook1HasMoved = 'N'
	rook2HasMoved = 'N'
	savers = []
	attackers = []
	pawnIdArray = []
	brainpiececolour = ''
	brainpiecetype = ''
	trainstatemat = statematrix

	def _init_(self):
		data = open('static\json\playing_data.json')
		dictdata = json.load(data)
		self.statematrix = dictdata['StateData']['StateMatrix']
		self.trainstatemat = self.statematrix
		self.compchoice = ''
		self.compmove = ''
		self.hasmoved = "N"
		self.compremove = ''
		self.hasremoved = 'N'
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
		self.piecesRemovedList = []
		self.currentDirectionArray = []
		self.attackerArray = []
		self.inGuard = 'N'
		self.pieceInGuard = ''
		self.spaceLength = 0;
		self.canSaveKing = ''
		self.kingHasMoved = 'N'
		self.rook1HasMoved = 'N'
		self.rook2HasMoved = 'N'
		self.savers = []
		self.attackers = []
		self.pawnIdArray = []
		self.brainpiececolour = ''
		self.brainpiecetype = ''
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
		
	def getColour(self, pieceId):
		my_colour = pieceId[:1] 
		if my_colour == "w":
			return "white"
		elif my_colour == "b":
			return "black"
		else:
			return "none"

	def getType(self, pieceId):
		my_type = pieceId[1:-1]
		if my_type in "king":
			my_type = "king"
		elif my_type in "queen":
			my_type = "queen"
	
		return my_type

	def getTrainState(self):
		return self.trainstatemat

	def setTrainState(self, newstate):
		self.trainstatemat = newstate

	def basicRookMovement(self, i, j, state, col):
		rookPlaces = []
		
		right = j
		left = j
		up = i
		down = i

		startr = False
		startl = False
		startu = False
		startd = False

		for n in range(0, 8):
			# print("n: %s"%n)
			if right < 8 and right >= 0:
				nextval = state[i][right]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					# print("np: %s"%nextpiece)
					if nextpiece == '' or startr == False:
						startr = True
						rookPlaces.append(nextval)
						right = right + 1
					else:
						my_colour = self.getColour(nextpiece)
						if my_colour is not col:
							rookPlaces.append(nextval)
						break

		for a in range(0, 8):
			if left < 8 and left >= 0:
				nextval = state[i][left]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					# print("npl: %s"%nextpiece)
					if nextpiece == '' or startl == False:
						startl = True
						rookPlaces.append(nextval)
						left = left - 1
					else:
						my_colour = self.getColour(nextpiece)
						if my_colour is not col:
							rookPlaces.append(nextval)
						break

		for b in range(0, 8):
			if up < 8 and up >= 0:
				nextval = state[up][j]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					print("npl: %s"%nextpiece)
					if nextpiece == '' or startu == False:
						startu = True
						rookPlaces.append(nextval)
						up = up + 1
					else:
						my_colour = self.getColour(nextpiece)
						if my_colour is not col:
							rookPlaces.append(nextval)
						break

		for c in range(0, 8):
			if down < 8 and down >= 0:
				nextval = state[down][j]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					if nextpiece == '' or startd == False:
						startd = True
						rookPlaces.append(nextval)
						down = down - 1
					else:
						my_colour = self.getColour(nextpiece)
						if my_colour is not col:
							rookPlaces.append(nextval)
						break


		return rookPlaces	

	def basicBishopMovement(self, i, j, state, col):
		places = []
		
		trright = j
		trup = i
		tlleft = j
		tlup = i
		brright = j
		brdown = i
		blleft = j
		bldown = i


		starttr = False
		starttl = False
		startbr = False
		startbl = False

		for n in range(0, 8):
			# print("n: %s"%n)
			if trright < 8 and trright >= 0 and trup < 8 and trup >= 0:
				nextval = state[trup][trright]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					# print("np: %s"%nextpiece)
					if nextpiece == '' or starttr == False:
						starttr = True
						places.append(nextval)
						trright = trright + 1
						trup = trup + 1
					else:
						my_colour = self.getColour(nextpiece)
						if my_colour is not col:
							places.append(nextval)
						break

		for a in range(0, 8):
			# print("n: %s"%n)
			if tlleft < 8 and tlleft >= 0 and tlup < 8 and tlup >= 0:
				nextval = state[tlup][tlleft]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					# print("np: %s"%nextpiece)
					if nextpiece == '' or starttl == False:
						starttl = True
						places.append(nextval)
						tlleft = tlleft - 1
						tlup = tlup + 1
					else:
						my_colour = self.getColour(nextpiece)
						if my_colour is not col:
							places.append(nextval)
						break

		for b in range(0, 8):
			# print("n: %s"%n)
			if brright < 8 and brright >= 0 and brdown < 8 and brdown >= 0:
				nextval = state[brdown][brright]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					# print("np: %s"%nextpiece)
					if nextpiece == '' or startbr == False:
						startbr = True
						places.append(nextval)
						brright = brright + 1
						brdown = brdown - 1
					else:
						my_colour = self.getColour(nextpiece)
						if my_colour is not col:
							places.append(nextval)
						break


		for c in range(0, 8):
			# print("n: %s"%n)
			if blleft < 8 and blleft >= 0 and bldown < 8 and bldown >= 0:
				nextval = state[bldown][blleft]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					# print("np: %s"%nextpiece)
					if nextpiece == '' or startbl == False:
						startbl = True
						places.append(nextval)
						blleft = blleft - 1
						bldown = bldown - 1
					else:
						my_colour = self.getColour(nextpiece)
						if my_colour is not col:
							places.append(nextval)
						break


		return places	

	def whitePawn(self, i, j, state, firsttime):
		places = []
		trright = j + 1
		trup = i + 1
		tlleft = j - 1
		tlup = i + 1 
		up = i
		
		if firsttime:
			if up+1 < 8 and up+1 >= 0:
				nextval = state[up+1][j]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					if nextpiece == '':
						places.append(nextval)
			
			if up+2 < 8 and up+2 >= 0:
				nextval = state[up+2][j]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					if nextpiece == '':
						places.append(nextval)
			
			if trright < 8 and trright >= 0 and trup < 8 and trup >= 0:
				nextval = state[trup][trright]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					my_colour = self.getColour(nextpiece)
					if my_colour is "black":
						places.append(nextval)

			if tlleft < 8 and tlleft >= 0 and tlup < 8 and tlup >= 0:
				nextval = state[tlup][tlleft]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					my_colour = self.getColour(nextpiece)
					if my_colour is "black":
						places.append(nextval)
		else:
			if up+1 < 8 and up+1 >= 0:
				nextval = state[up+1][j]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					if nextpiece == '':
						places.append(nextval)
			
			if trright < 8 and trright >= 0 and trup < 8 and trup >= 0:
				nextval = state[trup][trright]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					my_colour = self.getColour(nextpiece)
					if my_colour is "black":
						places.append(nextval)

			if tlleft < 8 and tlleft >= 0 and tlup < 8 and tlup >= 0:
				nextval = state[tlup][tlleft]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					my_colour = self.getColour(nextpiece)
					if my_colour is "black":
						places.append(nextval)


		return places	

	def blackPawn(self, i, j, state, firsttime):
		places = []
		trright = j - 1
		trup = i - 1
		tlleft = j + 1
		tlup = i - 1 
		up = i
		
		if firsttime:
			if up-1 < 8 and up-1 >= 0:
				nextval = state[up-1][j]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					if nextpiece == '':
						places.append(nextval)
			
			if up-2 < 8 and up-2 >= 0:
				nextval = state[up-2][j]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					if nextpiece == '':
						places.append(nextval)
			
			if trright < 8 and trright >= 0 and trup < 8 and trup >= 0:
				nextval = state[trup][trright]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					my_colour = self.getColour(nextpiece)
					if my_colour is "white":
						places.append(nextval)

			if tlleft < 8 and tlleft >= 0 and tlup < 8 and tlup >= 0:
				nextval = state[tlup][tlleft]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					my_colour = self.getColour(nextpiece)
					if my_colour is "white":
						places.append(nextval)
		else:
			if up-1 < 8 and up-1 >= 0:
				nextval = state[up-1][j]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					if nextpiece == '':
						places.append(nextval)

			if trright < 8 and trright >= 0 and trup < 8 and trup >= 0:
				nextval = state[trup][trright]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					my_colour = self.getColour(nextpiece)
					if my_colour is "white":
						places.append(nextval)

			if tlleft < 8 and tlleft >= 0 and tlup < 8 and tlup >= 0:
				nextval = state[tlup][tlleft]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					my_colour = self.getColour(nextpiece)
					if my_colour is "white":
						places.append(nextval)


		return places	

	def basicPawnMovement(self, i, j, state, firsttime, colour):
		if colour is "white":
			return self.whitePawn(i, j, state, firsttime)
		elif colour is "black":
			return self.blackPawn(i, j, state, firsttime)
		return []

	def basicHorseMovement(self, i, j, state, col):
		places = []

		up = i + 2
		upr = j + 1
		upl = j - 1

		down = i - 2
		downr = j + 1
		downl = j - 1

		right = j + 2
		rightu = i + 1
		rightd = i - 1

		left = j - 2
		leftu = i + 1
		leftd = i - 1

		if up < 8 and up >= 0 and upr < 8 and upr >= 0:
			nextval = state[up][upr]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				# print("np: %s"%nextpiece)
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)

		if up < 8 and up >= 0 and upl < 8 and upl >= 0:
			nextval = state[up][upl]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)

		if down < 8 and down >= 0 and downr < 8 and downr >= 0:
			nextval = state[down][downr]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)

		if down < 8 and down >= 0 and downl < 8 and downl >= 0:
			nextval = state[down][downl]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)

		if right < 8 and right >= 0 and rightu < 8 and rightu >= 0:
			nextval = state[rightu][right]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)

		if right < 8 and right >= 0 and rightd < 8 and rightd >= 0:
			nextval = state[rightd][right]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)

		if left < 8 and left >= 0 and leftu < 8 and leftu >= 0:
			nextval = state[leftu][left]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)
					
		if left < 8 and left >= 0 and leftd < 8 and leftd >= 0:
			nextval = state[leftd][left]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)

		return places

	def basicKingMovement(self, i, j, state, col):
		places = []

		up = i + 1
		right = j + 1
		bottom = i - 1
		left = j - 1

		if up < 8 and up >=0:
			nextval = state[up][j]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)

		if up < 8 and up >= 0 and right < 8 and right >=0:
			nextval = state[up][right]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)


		if right < 8 and right >= 0:
			nextval = state[i][right]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)

		if bottom < 8 and bottom >= 0 and right < 8 and right >=0:
			nextval = state[bottom][right]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)

		if bottom < 8 and bottom >= 0:
			nextval = state[bottom][j]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)

		if bottom < 8 and bottom >= 0 and left < 8 and left >=0:
			nextval = state[bottom][left]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)

		if left < 8 and left >= 0:
			nextval = state[i][left]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)

		if up < 8 and up >= 0 and left < 8 and left >=0:
			nextval = state[up][left]
			if nextval is not None:
				nextpiece = nextval['pieceId']
				if nextpiece == '':
					places.append(nextval)
				else:
					my_colour = self.getColour(nextpiece)
					if my_colour is not col:
						places.append(nextval)

		return places




	def processState(self, currentState):
		
		
		self.hasmoved = "N"
		self.hasremoved = "N"
		
		if(currentState!=self.statematrix):
			#'''
			self.statematrix = currentState
			# if not self.first:
			# 	self.compchoice = 'bpawn5'
			# 	self.compmove = 'r5E'
			# 	self.statematrix[6][4].update(pieceId='') 
			# 	self.statematrix[4][4].update(pieceId='bpawn5')
			# 	self.hasmoved = "Y"
			# 	self.first = True
			# 	self.sec = False
			# elif not self.sec:
			# 	self.compchoice = 'bqueen'
			# 	self.compmove = 'r4H'
			# 	self.statematrix[7][3].update(pieceId='') 
			# 	self.statematrix[3][7].update(pieceId='bqueen')
			# 	self.hasmoved = "Y"
			# 	self.sec = True
			# 	self.third = False
			# elif not self.third:
			# 	self.compchoice = 'bqueen'
			# 	self.compremove = 'wpawn8'
			# 	self.compmove = 'r1H'
			# 	self.statematrix[3][7].update(pieceId='') 
			# 	self.statematrix[1][7].update(pieceId='bqueen')	
			# 	self.hasremoved = "Y"
			# 	self.hasmoved = "Y"	
			# 	self.third = True
			# 	self.fourth = False
			# elif not self.fourth:
			# 	self.compchoice = 'bqueen'
			# 	self.compmove = 'r4F'
			# 	self.compremove = 'wpawn6'
			# 	self.statematrix[1][7].update(pieceId='') 
			# 	self.statematrix[3][5].update(pieceId='bqueen')	
			# 	self.hasmoved = "Y"	
			# 	self.hasremoved = "Y"			
			# 	self.fourth = True
			# 	self.fifth = False
			# elif not self.fifth:
			# 	self.compchoice = 'bqueen'
			# 	self.compremove = 'wbishop2'
			# 	self.compmove = 'r1F'
			# 	self.statematrix[3][5].update(pieceId='') 
			# 	self.statematrix[0][5].update(pieceId='bqueen')	
			# 	self.hasremoved = "Y"
			# 	self.hasmoved = "Y"
			# 	self.fifth = True
			# 	self.move6 = False
			# elif not self.move6:
			# 	self.compchoice = 'brook1'
			# 	self.compmove = 'r6A'
			# 	self.statematrix[7][0].update(pieceId='') 
			# 	self.statematrix[5][0].update(pieceId='brook1')
			# 	self.hasmoved = "Y"
			# 	self.move6 = True
			# 	self.move7 = False
			#elif not self.move7:
				# self.compchoice = 'bpawn7'
				# self.compmove = 'r5G'
				# self.statematrix[6][6].update(pieceId='') 
				# self.statematrix[4][6].update(pieceId='bpawn7')
				# self.hasmoved = "Y"
				# self.move7 = True
				# self.move8 = False
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

	def setExtraInfo(self, kmvd, r1mvd, r2mvd, pwnarr, rmvdlist):
		self.kingHasMoved = kmvd
		self.rook1HasMoved = r1mvd
		self.rook2HasMoved = r2mvd
		self.pawnIdArray = pwnarr
		self.piecesRemovedList = rmvdlist

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

	def getRemove(self):
		return self.compremove

	def getChoice(self):
		return self.compchoice

	def getHasMoved(self):
		return self.hasmoved
	
	def getHasRemoved(self):
		return self.hasremoved

	def getCheckMate(self):
		return self.checkmate

	def getFreeMove(self):
		return self.freemove

	def getPiecesRemoved(self):
		return self.piecesRemovedList

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

	def getPawnArray(self):
		return self.pawnIdArray

	def getKingHasMoved(self):
		return self.kingHasMoved

	def getRook1HasMoved(self):
		return self.rook1HasMoved

	def getRook2HasMoved(self):
		return self.rook2HasMoved