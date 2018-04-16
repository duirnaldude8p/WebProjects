import json

class Brain(object):
	data = open('ChessApp\static\json\playing_data.json')
	dictdata = json.load(data)
	statematrix = dictdata['StateData']['StateMatrix']
	data2 = open('ChessApp\static\json\playing_data2.json')
	dictdata2 = json.load(data2)
	trainstatemat = dictdata2['StateData']['StateMatrix']
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
	firsttimes = [
					{"id": "wpawn1", "is_first": True}, {"id": "wpawn2", "is_first": True}, {"id": "wpawn3", "is_first": True},
					{"id": "wpawn4", "is_first": True}, {"id": "wpawn5", "is_first": True}, {"id": "wpawn6", "is_first": True},
					{"id": "wpawn7", "is_first": True}, {"id": "wpawn8", "is_first": True}, {"id": "bpawn1", "is_first": True}, 
					{"id": "bpawn2", "is_first": True}, {"id": "bpawn3", "is_first": True}, {"id": "bpawn4", "is_first": True}, 
					{"id": "bpawn5", "is_first": True}, {"id": "bpawn6", "is_first": True}, {"id": "bpawn7", "is_first": True}, 
					{"id": "bpawn8", "is_first": True}, {"id": "wrook1", "is_first": True}, {"id": "wrook2", "is_first": True},
					{"id": "brook1", "is_first": True}, {"id": "brook2", "is_first": True}, 
					{"id": "wbishop1", "is_first": True}, {"id": "wbishop2", "is_first": True},
					{"id": "bbishop1", "is_first": True}, {"id": "bbishop2", "is_first": True},
					{"id": "whorse1", "is_first": True}, {"id": "whorse2", "is_first": True},
					{"id": "bhorse1", "is_first": True}, {"id": "bhorse2", "is_first": True},
					{"id": "wking", "is_first": True}, {"id": "bking", "is_first": True},
					{"id": "wqueen", "is_first": True}, {"id": "bqueen", "is_first": True}
				]
	
	movesdict = [
					{"id": "wpawn1", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn2", "moves": [], "pos": None, "in_check": False}, 
					{"id": "wpawn3", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn4", "moves": [], "pos": None, "in_check": False}, 
					{"id": "wpawn5", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn6", "moves": [], "pos": None, "in_check": False},
					{"id": "wpawn7", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn8", "moves": [], "pos": None, "in_check": False}, 
					{"id": "bpawn1", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn2", "moves": [], "pos": None, "in_check": False},
					{"id": "bpawn3", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn4", "moves": [], "pos": None, "in_check": False}, 
					{"id": "bpawn5", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn6", "moves": [], "pos": None, "in_check": False},
					{"id": "bpawn7", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn8", "moves": [], "pos": None, "in_check": False},
					{"id": "wrook1", "moves": [], "pos": None, "in_check": False}, {"id": "wrook2", "moves": [], "pos": None, "in_check": False},
					{"id": "brook1", "moves": [], "pos": None, "in_check": False}, {"id": "brook2", "moves": [], "pos": None, "in_check": False}, 
					{"id": "wbishop1", "moves": [], "pos": None, "in_check": False}, {"id": "wbishop2", "moves": [], "pos": None, "in_check": False},
					{"id": "bbishop1", "moves": [], "pos": None, "in_check": False}, {"id": "bbishop2", "moves": [], "pos": None, "in_check": False},
					{"id": "whorse1", "moves": [], "pos": None, "in_check": False}, {"id": "whorse2", "moves": [], "pos": None, "in_check": False},
					{"id": "bhorse1", "moves": [], "pos": None, "in_check": False}, {"id": "bhorse2", "moves": [], "pos": None, "in_check": False},
					{"id": "wking", "moves": [], "can_castle": False, "r_castle_rook": None, "l_castle_rook": None, "pos": None, "in_check": False},
					{"id": "bking", "moves": [], "can_castle": False, "r_castle_rook": None, "l_castle_rook": None, "pos": None, "in_check": False},
					{"id": "wqueen", "moves": [], "pos": None, "in_check": False}, {"id": "bqueen", "moves": [], "pos": None, "in_check": False}
				]


	def _init_(self):
		data = open('ChessApp\static\json\playing_data.json')
		dictdata = json.load(data)
		self.statematrix = dictdata['StateData']['StateMatrix']
		data2 = open('ChessApp\static\json\playing_data2.json')
		dictdata2 = json.load(data2)
		self.trainstatemat = dictdata2['StateData']['StateMatrix']
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
		self.spaceLength = 0
		self.canSaveKing = ''
		self.kingHasMoved = 'N'
		self.rook1HasMoved = 'N'
		self.rook2HasMoved = 'N'
		self.savers = []
		self.attackers = []
		self.pawnIdArray = []
		self.brainpiececolour = ''
		self.brainpiecetype = ''
		self.firsttimes = [
					{"id": "wpawn1", "is_first": True}, {"id": "wpawn2", "is_first": True}, {"id": "wpawn3", "is_first": True},
					{"id": "wpawn4", "is_first": True}, {"id": "wpawn5", "is_first": True}, {"id": "wpawn6", "is_first": True},
					{"id": "wpawn7", "is_first": True}, {"id": "wpawn8", "is_first": True}, {"id": "bpawn1", "is_first": True}, 
					{"id": "bpawn2", "is_first": True}, {"id": "bpawn3", "is_first": True}, {"id": "bpawn4", "is_first": True}, 
					{"id": "bpawn5", "is_first": True}, {"id": "bpawn6", "is_first": True}, {"id": "bpawn7", "is_first": True}, 
					{"id": "bpawn8", "is_first": True}, {"id": "wrook1", "is_first": True}, {"id": "wrook2", "is_first": True},
					{"id": "brook1", "is_first": True}, {"id": "brook2", "is_first": True}, 
					{"id": "wbishop1", "is_first": True}, {"id": "wbishop2", "is_first": True},
					{"id": "bbishop1", "is_first": True}, {"id": "bbishop2", "is_first": True},
					{"id": "whorse1", "is_first": True}, {"id": "whorse2", "is_first": True},
					{"id": "bhorse1", "is_first": True}, {"id": "bhorse2", "is_first": True},
					{"id": "wking", "is_first": True}, {"id": "bking", "is_first": True},
					{"id": "wqueen", "is_first": True}, {"id": "bqueen", "is_first": True}
				]
		self.movesdict = [
					{"id": "wpawn1", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn2", "moves": [], "pos": None, "in_check": False}, 
					{"id": "wpawn3", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn4", "moves": [], "pos": None, "in_check": False}, 
					{"id": "wpawn5", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn6", "moves": [], "pos": None, "in_check": False},
					{"id": "wpawn7", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn8", "moves": [], "pos": None, "in_check": False}, 
					{"id": "bpawn1", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn2", "moves": [], "pos": None, "in_check": False},
					{"id": "bpawn3", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn4", "moves": [], "pos": None, "in_check": False}, 
					{"id": "bpawn5", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn6", "moves": [], "pos": None, "in_check": False},
					{"id": "bpawn7", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn8", "moves": [], "pos": None, "in_check": False},
					{"id": "wrook1", "moves": [], "pos": None, "in_check": False}, {"id": "wrook2", "moves": [], "pos": None, "in_check": False},
					{"id": "brook1", "moves": [], "pos": None, "in_check": False}, {"id": "brook2", "moves": [], "pos": None, "in_check": False}, 
					{"id": "wbishop1", "moves": [], "pos": None, "in_check": False}, {"id": "wbishop2", "moves": [], "pos": None, "in_check": False},
					{"id": "bbishop1", "moves": [], "pos": None, "in_check": False}, {"id": "bbishop2", "moves": [], "pos": None, "in_check": False},
					{"id": "whorse1", "moves": [], "pos": None, "in_check": False}, {"id": "whorse2", "moves": [], "pos": None, "in_check": False},
					{"id": "bhorse1", "moves": [], "pos": None, "in_check": False}, {"id": "bhorse2", "moves": [], "pos": None, "in_check": False},
					{"id": "wking", "moves": [], "can_castle": False, "r_castle_rook": None, "l_castle_rook": None, "pos": None, "in_check": False},
					{"id": "bking", "moves": [], "can_castle": False, "r_castle_rook": None, "l_castle_rook": None, "pos": None, "in_check": False},
					{"id": "wqueen", "moves": [], "pos": None, "in_check": False}, {"id": "bqueen", "moves": [], "pos": None, "in_check": False}
				]
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
			return ""

	def getType(self, pieceId):
		my_type = pieceId[1:-1]
		if my_type in "king" and my_type != "":
			my_type = "king"
		elif my_type in "queen" and my_type != "":
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
					# print("npl: %s"%nextpiece)
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
		is_infront = False
		
		if firsttime:
			if up+1 < 8 and up+1 >= 0:
				nextval = state[up+1][j]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					if nextpiece == '':
						places.append(nextval)
					elif nextpiece != '':
						is_infront = True
			
			if up+2 < 8 and up+2 >= 0:
				nextval = state[up+2][j]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					if nextpiece == '' and not is_infront:
						places.append(nextval)
			
			if trright < 8 and trright >= 0 and trup < 8 and trup >= 0:
				nextval = state[trup][trright]
				# print("pawn value: %s"%nextval)
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
		is_infront = False
		
		if firsttime:
			if up-1 < 8 and up-1 >= 0:
				nextval = state[up-1][j]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					if nextpiece == '':
						places.append(nextval)
					elif nextpiece != '':
						is_infront = True
			
			if up-2 < 8 and up-2 >= 0:
				nextval = state[up-2][j]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					if nextpiece == '' and not is_infront:
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
		# print("col: %s"%colour)
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

	def smoothenArray(self, input_arr, input_val):
		# length = len(input_arr)
		# print("length: %s"%length)

		return [val for val in input_arr if val != input_val]

	def horseChecker(self, i, j, state, col):
		places = []

		places = self.basicHorseMovement(i, j, state, col)
		my_type = ''
		my_colour = ''
		
		for item in places:
			my_type = self.getType(item['pieceId'])
			my_colour = self.getColour(item['pieceId'])
			if my_type == "horse" and my_colour is not '' and col is not my_colour:
				return item
		
		return None


	def pawnChecker(self, i, j, state, col, firsttime):
		places = []

		places = self.basicPawnMovement(i, j, state, firsttime, col)
		# print("places: %s"%places)
		my_type = ''
		my_colour = ''
		
		for item in places:
			my_type = self.getType(item['pieceId'])
			my_colour = self.getColour(item['pieceId'])
			if my_type == "pawn"  and my_colour is not '' and col is not my_colour:
				return item
		
		return None

	def rookChecker(self, i, j, state, col):
		places = []

		places = self.basicRookMovement(i, j, state, col)
		my_type = ''
		my_colour = ''

		for item in places:
			my_type = self.getType(item['pieceId'])
			my_colour = self.getColour(item['pieceId'])
			if my_type == "rook" and my_colour is not '' and col is not my_colour:
				return item

		return None	

	def bishopChecker(self, i, j, state, col):
		places = []

		places = self.basicBishopMovement(i, j, state, col)
		my_type = ''
		my_colour = ''

		for item in places:
			my_type = self.getType(item['pieceId'])
			my_colour = self.getColour(item['pieceId'])
			if my_type == "bishop" and my_colour is not '' and col is not my_colour:
				return item

		return None	

	def queenChecker(self, i, j, state, col):
		places = []

		places = self.basicRookMovement(i, j, state, col)
		places2 = self.basicBishopMovement(i, j, state, col)
		places = places + places2
		my_type = ''
		my_colour = ''

		for item in places:
			my_type = self.getType(item['pieceId'])
			my_colour = self.getColour(item['pieceId'])
			if my_type == "queen" and my_colour is not '' and col is not my_colour:
				return item

		return None	

	def getCoordinates(self, posId):
		
		number = posId[1:-1]
		i = int(number) - 1
		
		
		letter = posId[2:]
		j = 0

		if letter is "A":
			j = 0
		elif letter is "B":
			j = 1
		elif letter is "C":
			j = 2
		elif letter is "D":
			j = 3
		elif letter is "E":
			j = 4
		elif letter is "F":
			j = 5
		elif letter is "G":
			j = 6
		elif letter is "H":
			j = 7

		return {"I": i, "J": j}

	def getRookCheckPath(self, i, j, state, place):
		end_id = place['placeId']
		places = []

		start_coord = {"I": i, "J": j}

		end_coord = self.getCoordinates(end_id)
		
		if start_coord['I'] == end_coord['I']:
			my_i = start_coord["I"]
			if start_coord['J'] < end_coord['J']:
				my_j = start_coord['J']
				my_end_j = end_coord['J']
				isfin = False
				while not isfin:
					if(my_j == my_end_j):
						isfin = True
					nextval = state[my_i][my_j]
					places.append(nextval)
					my_j = my_j + 1

			if start_coord['J'] > end_coord['J']:
				my_j = end_coord['J']
				my_end_j = start_coord['J']
				isfin = False
				while not isfin:
					if(my_j == my_end_j):
						isfin = True
					nextval = state[my_i][my_j]
					places.append(nextval)
					my_j = my_j + 1

		if start_coord['J'] == end_coord['J']:
			my_j = start_coord["J"]
			if start_coord['I'] < end_coord['I']:
				my_i = start_coord['I']
				my_end_i = end_coord['I']
				isfin = False
				while not isfin:
					if(my_i == my_end_i):
						isfin = True
					nextval = state[my_i][my_j]
					places.append(nextval)
					my_i = my_i + 1

			if start_coord['I'] > end_coord['I']:
				my_i = end_coord['I']
				my_end_i = start_coord['I']
				isfin = False
				while not isfin:
					if(my_i == my_end_i):
						isfin = True
					nextval = state[my_i][my_j]
					places.append(nextval)
					my_i = my_i + 1

		return places


	def getBishopCheckPath(self, i, j, state, place):
		end_id = place['placeId']
		places = []

		start_coord = {"I": i, "J": j}

		end_coord = self.getCoordinates(end_id)

		startI = start_coord['I']
		startJ = start_coord['J']

		i1 = startI + 1
		j1 = startJ + 1

		i2 = startI + 1
		j2 = startJ - 1

		i3 = startI - 1
		j3 = startJ + 1

		i4 = startI - 1
		j4 = startJ - 1

		endI = end_coord['I']
		endJ = end_coord['J']

		my_direction = ''

		
			
		for n in range(0, 8):
			if i1 < 8 and i1 >= 0 and j1 < 8 and j1 >= 0:
				if i1 == endI and j1 == endJ:
					my_direction = 'tr'
					break
				i1 = i1 + 1
				j1 = j1 + 1

		for n in range(0, 8):
			if i2 < 8 and i2 >= 0 and j2 < 8 and j2 >= 0:
				if i2 == endI and j2 == endJ:
					my_direction = 'tl'
					break
				i2 = i2 + 1
				j2 = j2 - 1

		for n in range(0, 8):
			if i3 < 8 and i3 >= 0 and j3 < 8 and j3 >= 0:
				if i3 == endI and j3 == endJ:
					my_direction = 'br'
					break
				i3 = i3 - 1
				j3 = j3 + 1

		for n in range(0, 8):
			if i4 < 8 and i4 >= 0 and j4 < 8 and j4 >= 0:
				if i4 == endI and j4 == endJ:
					my_direction = 'bl'
					break
				i4 = i4 - 1
				j4 = j4 - 1


		

		if my_direction is not '':
			for m in range(0, 8):
				if my_direction is 'tr':
					if startI < 8 and startI >= 0 and startJ < 8 and startJ >= 0:
						nextval = state[startI][startJ]
						places.append(nextval)
						if startI == endI and startJ == endJ:
							break
						startI = startI + 1
						startJ = startJ + 1

			for m in range(0, 8):
				if my_direction is 'tl':
					if startI < 8 and startI >= 0 and startJ < 8 and startJ >= 0:
						nextval = state[startI][startJ]
						places.append(nextval)
						if startI == endI and startJ == endJ:
							break
						startI = startI + 1
						startJ = startJ - 1

			for m in range(0, 8):
				if my_direction is 'br':
					if startI < 8 and startI >= 0 and startJ < 8 and startJ >= 0:
						nextval = state[startI][startJ]
						places.append(nextval)
						if startI == endI and startJ == endJ:
							break
						startI = startI - 1
						startJ = startJ + 1

			for m in range(0, 8):
				if my_direction is 'bl':
					if startI < 8 and startI >= 0 and startJ < 8 and startJ >= 0:
						nextval = state[startI][startJ]
						places.append(nextval)
						if startI == endI and startJ == endJ:
							break
						startI = startI - 1
						startJ = startJ - 1

		return places





	def getInGuardDir(self, i, j, state, king_place, p_type):

		end_id = king_place['placeId']
		places = []

		start_coord = {"I": i, "J": j}

		end_coord = self.getCoordinates(end_id)

		startI = start_coord['I']
		startJ = start_coord['J']

		i1 = startI + 1
		j1 = startJ + 1

		i2 = startI + 1
		j2 = startJ - 1

		i3 = startI - 1
		j3 = startJ + 1

		i4 = startI - 1
		j4 = startJ - 1

		i5 = startI + 1
		j5 = startJ

		i6 = startI - 1
		j6 = startJ 

		i7 = startI
		j7 = startJ + 1

		i8 = startI
		j8 = startJ - 1

		endI = end_coord['I']
		endJ = end_coord['J']
		# print("end %s - %s"%(endI, endJ))
		my_direction = ''

		
			# if startI < 8 and startI >= 0 and startJ < 8 and startJ >= 0 and endI < 8 and endI >= 0 and endJ < 8 and endJ >= 0:
		for n in range(0, 8):	
			if i1 < 8 and i1 >= 0 and j1 < 8 and j1 >= 0:
				if p_type == "bishop" or p_type == "queen" or p_type == "rook":
					if i1 == endI and j1 == endJ:
						my_direction = 'tr'
						break
					i1 = i1 + 1
					j1 = j1 + 1

		for n in range(0, 8):
			if i2 < 8 and i2 >= 0 and j2 < 8 and j2 >= 0:
				if p_type == "bishop" or p_type == "queen" or p_type == "rook":
					if i2 == endI and j2 == endJ:
						my_direction = 'tl'
						break
					i2 = i2 + 1
					j2 = j2 - 1

		for n in range(0, 8):
			if i3 < 8 and i3 >= 0 and j3 < 8 and j3 >= 0:
				if p_type == "bishop" or p_type == "queen" or p_type == "rook":
					if i3 == endI and j3 == endJ:
						my_direction = 'br'
						break
					i3 = i3 - 1
					j3 = j3 + 1

		for n in range(0, 8):
			if i4 < 8 and i4 >= 0 and j4 < 8 and j4 >= 0:
				if p_type == "bishop" or p_type == "queen" or p_type == "rook":
					if i4 == endI and j4 == endJ:
						my_direction = 'bl'
						break
					i4 = i4 - 1
					j4 = j4 - 1

		for n in range(0, 8):
			if i5 < 8 and i5 >= 0 and j5 < 8 and j5 >= 0:
				if p_type == "rook" or p_type == "queen" or p_type == "bishop":
					if i5 == endI and j5 == endJ:
						my_direction = 'up'
						break
					i5 = i5 + 1

		for n in range(0, 8):
			if i6 < 8 and i6 >= 0 and j6 < 8 and j6 >= 0:
				if p_type == "rook" or p_type == "queen" or p_type == "bishop":
					if i6 == endI and j6 == endJ:
						my_direction = 'down'
						break
					i6 = i6 - 1

		for n in range(0, 8):
			if i7 < 8 and i7 >= 0 and j7 < 8 and j7 >= 0:
				if p_type == "rook" or p_type == "queen" or p_type == "bishop":
					if i7 == endI and j7 == endJ:
						my_direction = 'right'
						break
					j7 = j7 + 1


			if i8 < 8 and i8 >= 0 and j8 < 8 and j8 >= 0:
				if p_type == "rook" or p_type == "queen" or p_type == "bishop":
					if i8 == endI and j8 == endJ:
						my_direction = 'left'
						break
					j8 = j8 - 1

		return my_direction





	def isInGuard(self, i, j, state, col, dirtn):

	

		start_coord = {"I": i, "J": j}

		startI = start_coord['I']
		startJ = start_coord['J']

		my_direction = dirtn

		in_guard = {"is_guard" : False, "value" : None}
        
		upstart = False
		downstart = False
		rightstart = False
		leftstart = False

		trstart = False
		tlstart = False
		brstart = False
		blstart = False

		for m in range(0, 8):
			if startI < 8 and startI >= 0 and startJ < 8 and startJ >= 0:

				if my_direction is not '':
					if my_direction is 'bl':
						nextval = state[startI][startJ]
						my_type = self.getType(nextval['pieceId'])
						my_colour = self.getColour(nextval['pieceId'])
						# print("val: %s - %s - %s"%(nextval, my_type, my_colour))
						if my_type == "queen" and my_colour !=  '' and col !=  my_colour or my_type == "bishop" and my_colour !=  '' and col !=  my_colour:
							in_guard = {"is_guard" : True, "value" : nextval}
							break
						elif my_colour != '' and col == my_colour and blstart:
							blstart = True
							break
						elif my_type != "queen" and my_colour !=  '' and col !=  my_colour and my_type != "bishop":
							blstart = True
							break
						startI = startI + 1
						startJ = startJ + 1

					if my_direction is 'br':
						nextval = state[startI][startJ]
						my_type = self.getType(nextval['pieceId'])
						my_colour = self.getColour(nextval['pieceId'])
						if my_type == "queen" and my_colour !=  '' and col !=  my_colour or my_type == "bishop" and my_colour !=  '' and col !=  my_colour:
							in_guard = {"is_guard" : True, "value" : nextval}
							break
						elif my_colour != '' and col == my_colour and brstart:
							brstart = True
							break
						elif my_type != "queen" and my_colour !=  '' and col !=  my_colour and my_type != "bishop":
							brstart = True
							break
						startI = startI + 1
						startJ = startJ - 1

					if my_direction is 'tl':
						nextval = state[startI][startJ]
						my_type = self.getType(nextval['pieceId'])
						my_colour = self.getColour(nextval['pieceId'])
						if my_type == "queen" and my_colour !=  '' and col !=  my_colour or my_type == "bishop" and my_colour !=  '' and col !=  my_colour:
							in_guard = {"is_guard" : True, "value" : nextval}
							break
						elif my_colour != '' and col == my_colour and tlstart:
							tlstart = True
							break
						elif my_type != "queen" and my_colour !=  '' and col !=  my_colour and my_type != "bishop":
							tlstart = True
							break
						startI = startI - 1
						startJ = startJ + 1

					if my_direction is 'tr':
						nextval = state[startI][startJ]
						my_type = self.getType(nextval['pieceId'])
						my_colour = self.getColour(nextval['pieceId'])
						if my_type == "queen" and my_colour !=  '' and col !=  my_colour or my_type == "bishop" and my_colour !=  '' and col !=  my_colour:
							in_guard = {"is_guard" : True, "value" : nextval}
							break
						elif my_colour != '' and col == my_colour and trstart:
							trstart = True
							break
						elif my_type != "queen" and my_colour !=  '' and col !=  my_colour and my_type != "bishop":
							trstart = True
							break
						startI = startI - 1
						startJ = startJ - 1

					if my_direction is 'up':
						nextval = state[startI][startJ]
						my_type = self.getType(nextval['pieceId'])
						my_colour = self.getColour(nextval['pieceId'])
						if my_type == "queen" and my_colour !=  '' and col !=  my_colour or my_type == "rook" and my_colour !=  '' and col !=  my_colour:
							in_guard = {"is_guard" : True, "value" : nextval}
							break
						elif my_colour != '' and col == my_colour and upstart:
							upstart = True
							break
						elif my_type != "queen" and my_colour !=  '' and col !=  my_colour and my_type != "rook":
							upstart = True
							break
						startI = startI - 1

					if my_direction is 'down':
						nextval = state[startI][startJ]
						# print("val: %s"%nextval['pieceId'])
						my_type = self.getType(nextval['pieceId'])
						my_colour = self.getColour(nextval['pieceId'])
						if my_type == "queen" and my_colour !=  '' and col !=  my_colour or my_type == "rook" and my_colour !=  '' and col !=  my_colour:
							# print("kinda working: %s - %s"%(nextval, places))
							in_guard = {"is_guard" : True, "value" : nextval}
							break
						elif my_colour != '' and col == my_colour and downstart:
							downstart = True
							break
						elif my_type != "queen" and my_colour !=  '' and col !=  my_colour and my_type != "rook":
							downstart = True
							break
						startI = startI + 1
			
					if my_direction is 'right':
						nextval = state[startI][startJ]
						my_type = self.getType(nextval['pieceId'])
						my_colour = self.getColour(nextval['pieceId'])
						if my_type == "queen" and my_colour !=  '' and col !=  my_colour or my_type == "rook" and my_colour !=  '' and col !=  my_colour:
							in_guard = {"is_guard" : True, "value" : nextval}
							break
						elif my_colour != '' and col == my_colour and rightstart:
							rightstart = True
							break
						elif my_type != "queen" and my_colour !=  '' and col !=  my_colour and my_type != "rook":
							rightstart = True
							break
						startJ = startJ - 1

					if my_direction is 'left':
						nextval = state[startI][startJ]
						my_type = self.getType(nextval['pieceId'])
						my_colour = self.getColour(nextval['pieceId'])
						if my_type == "queen" and my_colour !=  '' and col !=  my_colour or my_type == "rook" and my_colour !=  '' and col !=  my_colour:
							in_guard = {"is_guard" : True, "value" : nextval}
							break
						elif my_colour != '' and col == my_colour and leftstart:
							leftstart = True
							break
						elif my_type != "queen" and my_colour !=  '' and col !=  my_colour and my_type != "rook":
							leftstart = True
							break
						startJ = startJ + 1

		return in_guard

	def inCheck(self, i, j, state, firsttime, col):
		checker = None

		checker1 = self.rookChecker(i, j, state, col)
		checker2 = self.bishopChecker(i, j, state, col)
		checker3 = self.horseChecker(i, j, state, col)
		checker4 = self.queenChecker(i, j, state, col)
		checker5 = self.pawnChecker(i, j, state, col, firsttime)
		if checker1 is not None:
			return checker1
		
		elif checker2 is not None:
			return checker2 
		
		elif checker3 is not None:
			return checker3
		
		elif checker4 is not None:
			return checker4
		
		elif checker5 is not None:
			return checker5

		return None
	
	def getPieces(self, state, col):
		places = []

		for i in range(0, 8):
			for j in range (0, 8):
				nextval = state[i][j]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					if nextpiece is not '':
						my_colour = self.getColour(nextpiece)
						if my_colour is col:
							places.append(nextval)

		return places

	def findKing(self, state, col):
		king = None
		breaker = False
		for i in range(0, 8):
			for j in range (0, 8):
				nextval = state[i][j]
				if nextval is not None:
					nextpiece = nextval['pieceId']
					if nextpiece is not '':
						my_type = self.getType(nextpiece)
						my_colour = self.getColour(nextpiece)
						if my_colour is col and my_type is "king":
							king = nextval
							breaker = True
							break
			if breaker:
				break				


		return king


	def getItemPlace(self, dict_input, val_id):
		place = None
		counter = 0
		for item in dict_input:
			if item is not None:
				next_id = item['id']
				if next_id == val_id:
					return counter
				counter = counter + 1
					
		return 0

	def getRestrictedPlaces(self, open_in, restricted_in):

		return [val for val in open_in if val in restricted_in]

	def isFirst(self, firsts, input_id):

		for item in firsts:
			my_id = item['id']
			is_first = item['is_first']
			# print("is first loop %s - %s - %s"%(input_id, my_id, is_first))
			if my_id == input_id and is_first is True:
				# print("is first true found  %s"%my_id)
				return True
			elif my_id == input_id and is_first is False:
				# print("is first false found  %s"%my_id)
				return False

		return True

	def getRightCastle(self, i, j, state, col):

		start_coord = {"I": i, "J": j}

		startI = start_coord['I']
		startJ = start_coord['J']
		
		w_right = startJ + 1
		b_right = startJ + 1

		castle = {"is_castle" : False, "king_pos" : None, "rook_pos": None, "rook": None}

		w_pos = []
		b_pos = []

		for m in range(0, 8):
			if w_right < 8 and w_right >= 0 and b_right < 8 and b_right >= 0:

				if col == 'white':
					rightval = state[i][w_right]
					rightpiece = rightval['pieceId']
					rightplace = rightval['placeId']
					w_type = self.getType(rightpiece)
					w_colour = self.getColour(rightpiece)
					# print("r val %s"%rightval)
					if rightpiece == '':
						w_right = w_right + 1
						# print("r emp val %s"%rightval)
					elif w_type == "rook" and w_colour == col:
						given_co = self.getCoordinates(rightplace)
						# print("r place %s - %s"%(given_co['I'], given_co['J']))
						if given_co['I'] == 0 and given_co['J'] == 7:
							king_check = self.inCheck(0, 5, state, True, col)
							rook_check = self.inCheck(0, 4, state, True, col)
							# print("check %s - %s"%(king_check, rook_check))
							if not king_check and not rook_check:
								castle = {"is_castle" : True, "king_pos" : state[0][5], "rook_pos": state[0][4], "rook": rightval}
							break
						else:
							break
					else:
						break

				elif col == "black":
					rightval = state[i][b_right]
					rightpiece = rightval['pieceId']
					rightplace = rightval['placeId']
					b_type = self.getType(rightpiece)
					b_colour = self.getColour(rightpiece)
					if rightpiece == '':
						b_right = b_right + 1
					elif b_type == "rook" and b_colour == col:
						given_co = self.getCoordinates(rightplace)
						if given_co['I'] == 7 and given_co['J'] == 7:
							king_check = self.inCheck(7, 5, state, True, col)
							rook_check = self.inCheck(7, 4, state, True, col)
							if not king_check and not rook_check:
								castle = {"is_castle" : True, "king_pos" : state[7][5], "rook_pos": state[7][4], "rook": rightval}
							break
						else:
							break
					else:
						break
					

				
		return castle

	def getLeftCastle(self, i, j, state, col):

		start_coord = {"I": i, "J": j}

		startI = start_coord['I']
		startJ = start_coord['J']
		
		w_left = startJ - 1
		b_left = startJ - 1
	

		castle = {"is_castle" : False, "king_pos" : None, "rook_pos": None, "rook": None}

		w_pos = []
		b_pos = []

		for m in range(0, 8):
			if w_left < 8 and w_left >= 0 and  b_left < 8 and b_left >= 0:

				if col == 'white':
					leftval = state[i][w_left]
					leftpiece = leftval['pieceId']
					leftplace = leftval['placeId']
					w_type = self.getType(leftpiece)
					w_colour = self.getColour(leftpiece)
					if leftpiece == '':
						w_left = w_left - 1
					elif w_type == "rook" and w_colour == col:
						given_co = self.getCoordinates(leftplace)
						if given_co['I'] == 0 and given_co['J'] == 0:
							king_check = self.inCheck(0, 1, state, True, col)
							rook_check = self.inCheck(0, 2, state, True, col)
							if not king_check and not rook_check:
								castle = {"is_castle" : True, "king_pos" : state[0][1], "rook_pos": state[0][2], "rook": leftval}
							break
						else:
							break
					else:
						break

				elif col == "black":
					leftval = state[i][b_left]
					leftpiece = leftval['pieceId']
					leftplace = leftval['placeId']
					b_type = self.getType(leftpiece)
					b_colour = self.getColour(leftpiece)
					if leftpiece == '':
						b_left = b_left - 1
					elif b_type == "rook" and b_colour == col:
						given_co = self.getCoordinates(leftplace)
						if given_co['I'] == 7 and given_co['J'] == 0:
							king_check = self.inCheck(7, 1, state, True, col)
							rook_check = self.inCheck(7, 2, state, True, col)
							if not king_check and not rook_check:
								castle = {"is_castle" : True, "king_pos" : state[7][1], "rook_pos": state[7][2], "rook": leftval}
							break
						else:
							break
					else:
						break
					

				
		return castle

	# def getMoves(self, state):


	def getMoves(self, state, firsts, col, vals, m_dict):
		in_check = False
		king = self.findKing(state, col)
		king_co = self.getCoordinates(king['placeId'])
		# print("col: %s"%col)
		in_check = False
		check = self.inCheck(king_co['I'], king_co['J'], state, True, col)
		if check is not None:
			in_check = True
		
		movements = []
		# print("king: %s"%king)
		if not in_check:
			for item in vals:
				item_id = item['pieceId']
				item_co = self.getCoordinates(item['placeId'])
				item_type = self.getType(item_id)
				
				in_guard_dir = self.getInGuardDir(item_co['I'], item_co['J'], state, king, item_type)
				in_guard = self.isInGuard(item_co['I'], item_co['J'], state, col, in_guard_dir)
				is_guard = in_guard['is_guard']
				in_g_v = in_guard['value']
				# print("g: %s"%in_g_v)
				is_first = self.isFirst(firsts, item_id)
				# item_in_check = self.inCheck(item_co['I'], item_co['J'], state, is_first, col)
				# item = {"pieceId": item['pieceId'], "placeId": item['placeId'], "inCheck": item_in_check}

				g_path = []
				if in_g_v:
					g_id = in_g_v['pieceId']

					g_r_path = self.getRookCheckPath(king_co['I'], king_co['J'], state, in_g_v)
					g_r_path = self.smoothenArray(g_r_path, king)
					g_b_path = self.getBishopCheckPath(king_co['I'], king_co['J'], state, in_g_v)
					g_b_path = self.smoothenArray(g_b_path, king)
					g_path = []
				
					if len(g_r_path) != 0 and len(g_b_path) == 0:
						g_path = g_r_path
					elif len(g_r_path) == 0 and len(g_b_path) != 0:
						g_path = g_b_path
					else:
						print("MULTIPLE PATH ERROR: %s - %s"%(len(g_r_path), len(g_b_path)))

				dict_place = self.getItemPlace(m_dict, item_id)
				# print("pos: %s"%dict_place)

				if item_type == "rook":
					movement = self.basicRookMovement(item_co['I'], item_co['J'], state, col)
					movement = self.smoothenArray(movement, item)
					# print("is guard %s"%is_guard)
					if is_guard:
						movement = self.getRestrictedPlaces(movement, g_path)
					# print("rook mov %s - %s"%(movement, item))
					# movements = movements + movement
					item_in_check = self.inCheck(item_co['I'], item_co['J'], state, is_first, col)
					m_dict[dict_place].update(moves = movement)
					m_dict[dict_place].update(pos = item)
					m_dict[dict_place].update(in_check = item_in_check)


				if item_type == "bishop":
					# print("bish: %s"%item)
					movement = self.basicBishopMovement(item_co['I'], item_co['J'], state, col)
					movement = self.smoothenArray(movement, item)
					if is_guard:
						movement = self.getRestrictedPlaces(movement, g_path)
					item_in_check = self.inCheck(item_co['I'], item_co['J'], state, is_first, col)
					m_dict[dict_place].update(moves = movement)
					m_dict[dict_place].update(pos = item)
					m_dict[dict_place].update(in_check = item_in_check)

				if item_type == "horse":
					movement = self.basicHorseMovement(item_co['I'], item_co['J'], state, col)
					if is_guard:
						movement = self.getRestrictedPlaces(movement, g_path)
					# print("horse mov %s"%movement)
					# movements = movements + movement
					item_in_check = self.inCheck(item_co['I'], item_co['J'], state, is_first, col)
					m_dict[dict_place].update(moves = movement)
					m_dict[dict_place].update(pos = item)
					m_dict[dict_place].update(in_check = item_in_check)

				if item_type == "pawn":
					movement = self.basicPawnMovement(item_co['I'], item_co['J'], state, is_first , col)
					if is_guard:
						movement = self.getRestrictedPlaces(movement, g_path)
					# print("pawn mov %s  %s"% (item, movement))
					item_in_check = self.inCheck(item_co['I'], item_co['J'], state, is_first, col)
					m_dict[dict_place].update(moves = movement)
					m_dict[dict_place].update(pos = item)
					m_dict[dict_place].update(in_check = item_in_check)

				if item_type == "queen":
					movement1 = self.basicRookMovement(item_co['I'], item_co['J'], state, col)
					movement1 = self.smoothenArray(movement1, item)
					movement2 = self.basicBishopMovement(item_co['I'], item_co['J'], state, col)
					movement2 = self.smoothenArray(movement2, item)
					movement = movement1 + movement2
					# print("is guard %s"%is_guard)
					# print("queen: %s"%item)
					if is_guard:
						movement = self.getRestrictedPlaces(movement, g_path)
					# movements = movements + movement
					item_in_check = self.inCheck(item_co['I'], item_co['J'], state, is_first, col)
					m_dict[dict_place].update(moves = movement)
					m_dict[dict_place].update(pos = item)
					m_dict[dict_place].update(in_check = item_in_check)

				if item_type == "king":
					movement = self.basicKingMovement(item_co['I'], item_co['J'], state, col)
					# print("k mov: %s"%movement)
					moves = []
					r_moves = self.getRightCastle(item_co['I'], item_co['J'], state, col)
					l_moves = self.getLeftCastle(item_co['I'], item_co['J'], state, col)
					can_c = False
					can_r_castle = r_moves['is_castle']
					can_l_castle = l_moves['is_castle']
					r_castling_rook = None
					l_castling_rook = None
					if can_r_castle:
						moves.append(r_moves['king_pos'])
						moves.append(r_moves['rook_pos'])
						can_c = can_r_castle
						r_castling_rook = r_moves['rook']


					if can_l_castle:
						moves.append(l_moves['king_pos'])
						moves.append(l_moves['rook_pos'])
						# print("k m: %s - %s"%(l_moves['king_pos'], l_moves['rook_pos']))
						can_c = can_l_castle
						l_castling_rook = l_moves['rook']
					item_in_check = self.inCheck(item_co['I'], item_co['J'], state, is_first, col)
					# print("k moves: %s"%moves)
					movement = moves
					m_dict[dict_place].update(moves = movement)
					m_dict[dict_place].update(pos = item)
					m_dict[dict_place].update(can_castle = can_c)
					m_dict[dict_place].update(r_castle_rook = r_castling_rook)
					m_dict[dict_place].update(l_castle_rook = l_castling_rook)
					m_dict[dict_place].update(in_check = item_in_check)

					# movements = movements + movement
		else:	
			for item in vals:

				item_id = item['pieceId']
				item_co = self.getCoordinates(item['placeId'])
				item_type = self.getType(item_id)
				restr1 = self.getRookCheckPath(king_co['I'], king_co['J'], state, check)
				restr2 = self.getBishopCheckPath(king_co['I'], king_co['J'], state, check) 
				restr = restr1 + restr2
				dict_place = self.getItemPlace(m_dict, item_id)

				is_first = self.isFirst(firsts, item_id)
				# item_in_check = self.inCheck(item_co['I'], item_co['J'], state, is_first, col)
				# item = {"pieceId": item['pieceId'], "placeId": item['placeId'], "inCheck": item_in_check}
				

				if item_type == "rook":
					movement = self.basicRookMovement(item_co['I'], item_co['J'], state, col)
					movement = self.smoothenArray(movement, item)
					movement = self.getRestrictedPlaces(movement, restr)
					# print("rook mov %s - %s"%(movement, item))
					# movements = movements + movement
					item_in_check = self.inCheck(item_co['I'], item_co['J'], state, is_first, col)
					m_dict[dict_place].update(moves = movement)
					m_dict[dict_place].update(pos = item)
					m_dict[dict_place].update(in_check = item_in_check)

				if item_type == "bishop":
					movement = self.basicBishopMovement(item_co['I'], item_co['J'], state, col)
					movement = self.smoothenArray(movement, item)
					movement = self.getRestrictedPlaces(movement, restr)
					# movements = movements + movement
					item_in_check = self.inCheck(item_co['I'], item_co['J'], state, is_first, col)
					m_dict[dict_place].update(moves = movement)
					m_dict[dict_place].update(pos = item)
					m_dict[dict_place].update(in_check = item_in_check)

				if item_type == "horse":
					movement = self.basicHorseMovement(item_co['I'], item_co['J'], state, col)
					movement = self.getRestrictedPlaces(movement, restr)
					# print("horse mov %s"%movement)
					# movements = movements + movement
					item_in_check = self.inCheck(item_co['I'], item_co['J'], state, is_first, col)
					m_dict[dict_place].update(moves = movement)
					m_dict[dict_place].update(pos = item)
					m_dict[dict_place].update(in_check = item_in_check)

				if item_type == "pawn":
		
					movement = self.basicPawnMovement(item_co['I'], item_co['J'], state, is_first, col)
					movement = self.getRestrictedPlaces(movement, restr)
					# print("pawn mov %s"%movement)
					# movements = movements + movement
					item_in_check = self.inCheck(item_co['I'], item_co['J'], state, is_first, col)
					m_dict[dict_place].update(moves = movement)
					m_dict[dict_place].update(pos = item)
					m_dict[dict_place].update(in_check = item_in_check)

				if item_type == "queen":
					movement1 = self.basicRookMovement(item_co['I'], item_co['J'], state, col)
					movement1 = self.smoothenArray(movement1, item)
					movement2 = self.basicBishopMovement(item_co['I'], item_co['J'], state, col)
					movement2 = self.smoothenArray(movement2, item)
					movement = movement1 + movement2
					movement = self.getRestrictedPlaces(movement, restr)
					# movements = movements + movement
					item_in_check = self.inCheck(item_co['I'], item_co['J'], state, is_first, col)
					m_dict[dict_place].update(moves = movement)
					m_dict[dict_place].update(pos = item)
					m_dict[dict_place].update(in_check = item_in_check)

				if item_type == "king":
					movement = self.basicKingMovement(item_co['I'], item_co['J'], state, col)
					movement2 = []
					for val in movement:
						val_co = self.getCoordinates(val['placeId'])
						
						val_in_check = False
						val_check = self.inCheck(val_co['I'], val_co['J'], state, True, col)
						if val_check is not None:
							val_in_check = True
						
						if val_in_check:
							movement2.append(val)

					movement = self.getRestrictedPlaces(movement, movement2)
					item_in_check = self.inCheck(item_co['I'], item_co['J'], state, is_first, col)
					m_dict[dict_place].update(moves = movement)
					m_dict[dict_place].update(pos = item)
					m_dict[dict_place].update(in_check = item_in_check)
					# movements = movements + movement


		return m_dict

	def getAssignedVal(self, my_dict, col):
		# print("dict: %s"%my_dict)
		my_piece = my_dict['pieceId']

		my_colour = self.getColour(my_piece)
		my_type = self.getType(my_piece)

		if my_type == "pawn" and my_colour != col:
			return 10
		elif my_type == "pawn" and my_colour == col:
			return -10
		elif my_type == "horse" and my_colour != col:
			return 30
		elif my_type == "horse" and my_colour == col:
			return -30
		elif my_type == "bishop" and my_colour != col:
			return 30
		elif my_type == "bishop" and my_colour == col:
			return -30
		elif my_type == "rook" and my_colour != col:
			return 50
		elif my_type == "rook" and my_colour == col:
			return -50
		elif my_type == "queen" and my_colour != col:
			return 90
		elif my_type == "queen" and my_colour == col:
			return -90
		elif my_type == "king" and my_colour == col:
			return -900
	
		return 0

	# def getAssignedVal(self, my_type, col):
	# 	# print("dict: %s"%my_dict)
	# 	my_piece = my_dict['pieceId']

	# 	my_colour = self.getColour(my_piece)
	# 	my_type = self.getType(my_piece)

	# 	if my_type == "pawn" and my_colour != col:
	# 		return 10
	# 	elif my_type == "pawn" and my_colour == col:
	# 		return -10
	# 	elif my_type == "horse" and my_colour != col:
	# 		return 30
	# 	elif my_type == "horse" and my_colour == col:
	# 		return -30
	# 	elif my_type == "bishop" and my_colour != col:
	# 		return 30
	# 	elif my_type == "bishop" and my_colour == col:
	# 		return -30
	# 	elif my_type == "rook" and my_colour != col:
	# 		return 50
	# 	elif my_type == "rook" and my_colour == col:
	# 		return -50
	# 	elif my_type == "queen" and my_colour != col:
	# 		return 90
	# 	elif my_type == "queen" and my_colour == col:
	# 		return -90
	# 	elif my_type == "king" and my_colour == col:
	# 		return -900
	
	# 	return 0		

	def isCornerRookCheck(self, i, j, state, col, check_own):
		my_colour = col
		if not check_own:
			if col == "white":
				my_colour = "black"
			elif col == "black":
				my_colour = "white"

		my_val = state[i][j]
		my_bit = my_val['pieceId']
		if my_bit != '' or not check_own:
			king = self.findKing(state, my_colour)
			king_co = self.getCoordinates(king['placeId'])
			king_piece = king['pieceId']

			start_coord = {"I": i, "J": j}

			end_coord = king_co
			# print("start: %s end: %s"%(start_coord, end_coord))
			if start_coord['I'] == end_coord['I']:
				my_i = start_coord["I"]
				if start_coord['J'] < end_coord['J']:
					my_j = start_coord['J']
					my_end_j = end_coord['J']
					isfin = False
					while not isfin:
						nextval = state[my_i][my_j]
						if my_j == my_end_j:
							isfin = True
							return True
						elif nextval['pieceId'] != '' and nextval['pieceId'] != king_piece:
							return False
						my_j = my_j + 1

				if start_coord['J'] > end_coord['J']:
					my_j = end_coord['J']
					my_end_j = start_coord['J']
					isfin = False
					while not isfin:
						nextval = state[my_i][my_j]
						if my_j == my_end_j:
							isfin = True
							return True
						elif nextval['pieceId'] != '' and nextval['pieceId'] != king_piece:
							return False
						my_j = my_j + 1

			if start_coord['J'] == end_coord['J']:
				my_j = start_coord["J"]
				if start_coord['I'] < end_coord['I']:
					my_i = start_coord['I']
					my_end_i = end_coord['I']
					isfin = False
					while not isfin:
						nextval = state[my_i][my_j]
						if my_i == my_end_i:
							isfin = True
							return True
						elif nextval['pieceId'] != '' and nextval['pieceId'] != king_piece:
							return False
						my_i = my_i + 1

				if start_coord['I'] > end_coord['I']:
					my_i = end_coord['I']
					my_end_i = start_coord['I']
					isfin = False
					while not isfin:
						nextval = state[my_i][my_j]
						if my_i == my_end_i:
							isfin = True
							return True
						elif nextval['pieceId'] != '' and nextval['pieceId'] != king_piece:
							return False
						my_i = my_i + 1

		return False


	def isCornerBishopCheck(self, i, j, state, col, check_own):
		my_colour = col
		if not check_own:
			if col == "white":
				my_colour = "black"
			elif col == "black":
				my_colour = "white"

		my_val = state[i][j]
		# print("val: %s"%my_val)
		my_bit = my_val['pieceId']
		if my_bit != '' or not check_own:
			king = self.findKing(state, my_colour)
			king_co = self.getCoordinates(king['placeId'])
			king_piece = king['pieceId']
			# print("king: %s"%king_piece)
			start_coord = {"I": i, "J": j}

			end_coord = king_co

			startI = start_coord['I']
			startJ = start_coord['J']

			i1 = startI + 1
			j1 = startJ + 1

			i2 = startI + 1
			j2 = startJ - 1

			i3 = startI - 1
			j3 = startJ + 1

			i4 = startI - 1
			j4 = startJ - 1

			endI = end_coord['I']
			endJ = end_coord['J']

			my_direction = ''

			
				
				# if startI < 8 and startI >= 0 and startJ < 8 and startJ >= 0 and endI < 8 and endI >= 0 and endJ < 8 and endJ >= 0:
			for n in range(0, 8):	
				# print("loop: ")
				if i1 < 8 and i1 >= 0 and j1 < 8 and j1 >= 0:
					nextval = state[i1][j1]
					# print("values: %s - %s"%(my_val, nextval))
					# print("next: %s - %s"%(king_piece, nextval['pieceId']))
					if i1 == endI and j1 == endJ:
						return True
					elif nextval['pieceId'] != '' and nextval['pieceId'] != king_piece:
						return False
					i1 = i1 + 1
					j1 = j1 + 1

			for n in range(0, 8):
				if i2 < 8 and i2 >= 0 and j2 < 8 and j2 >= 0:
					nextval = state[i2][j2]
					if i2 == endI and j2 == endJ:
						return True
					elif nextval['pieceId'] != '' and nextval['pieceId'] != king_piece:
						return False
					i2 = i2 + 1
					j2 = j2 - 1
				

			for n in range(0, 8):
				if i3 < 8 and i3 >= 0 and j3 < 8 and j3 >= 0:
					nextval = state[i3][j3]
					if i3 == endI and j3 == endJ:
						return True
					elif nextval['pieceId'] == '' and nextval['pieceId'] != king_piece:
						return False
					i3 = i3 - 1
					j3 = j3 + 1

			for n in range(0, 8):
				if i4 < 8 and i4 >= 0 and j4 < 8 and j4 >= 0:
					nextval = state[i4][j4]
					if i4 == endI and j4 == endJ:
						return True
					elif nextval['pieceId'] != '' and nextval['pieceId'] != king_piece:
						return False
					i4 = i4 - 1
					j4 = j4 - 1

		return False

	def isCornerHorseChecker(self, i, j, state, col, check_own):
	
		places = self.basicHorseMovement(i, j, state, col)
		my_type = ''
		my_colour = ''
		
		for item in places:
			my_type = self.getType(item['pieceId'])
			my_colour = self.getColour(item['pieceId'])
			if not check_own:
				if my_type == "king" and my_colour != '' and col != my_colour:
					return True
			else:
				if my_type == "king" and my_colour != '' and col == my_colour:
					return True
		
		return False

	def isCornerPawnChecker(self, i, j, state, col, firsttime, check_own):

		places = self.basicPawnMovement(i, j, state, firsttime, col)
		# print("places: %s"%places)
		my_type = ''
		my_colour = ''
		
		for item in places:
			my_type = self.getType(item['pieceId'])
			my_colour = self.getColour(item['pieceId'])
			if not check_own:
				if my_type == "king" and my_colour != '' and col != my_colour:
					return True
			else:
				if my_type == "king" and my_colour != '' and col == my_colour:
					return True
		
		return False

	def dictToList(self, m_dict, col):
		m_list = []
		
		for value in m_dict:
			# print("val: %s"%value)
			my_moves = value['moves']
			pos = value['pos']	
			in_check = value['in_check']	
			if pos:
				pos_id = pos['pieceId']
				if pos_id:
					pos_type = self.getType(pos_id)
					for item in my_moves:
						m_list.append({"pos":pos, "item":item, "in_check": in_check})

		return m_list

	def evaluate(self, state, m_list, col, firsts):
		bestmove = None
		bestval = -9999

		king = self.findKing(state, col)
		king_co = self.getCoordinates(king['placeId'])

		counter = 0

		
		for value in m_list:
			print("value: %s"%value)
			item = value['item']
			item_id = item['pieceId']
			pos = value['pos']
			pos_id = pos['pieceId']
			pos_type = self.getType(pos_id)
			current_c_e = self.getAssignedVal(pos, col)
			if counter == 0:
				bestmove = {"pos": pos, "item": item}
			init_e = 0
			check_e = 0
			pos_in_check = value['in_check']
			if pos_in_check and pos_type != "king":
				init_e = -self.getAssignedVal(pos, col)
			init_e = init_e + self.getAssignedVal(item, col)
			item_co = self.getCoordinates(item['placeId'])
			is_first = self.isFirst(firsts, item_id)
			reach_king = False
			if pos_type == "rook" or pos_type == "queen":
				reach_king = self.isCornerRookCheck(item_co['I'], item_co['J'], state, col, False)
				if not reach_king:
					reach_king = self.isCornerRookCheck(item_co['I'], item_co['J'], state, col, True)
			elif pos_type == "bishop" or pos_type == "queen":
				reach_king = self.isCornerBishopCheck(item_co['I'], item_co['J'], state, col, False)
				if not reach_king:
					reach_king = self.isCornerBishopCheck(item_co['I'], item_co['J'], state, col, True)
				# print("bishop reach king: %s - %s"%(reach_king, item))
			elif pos_type == "horse":
				reach_king = self.isCornerHorseChecker(item_co['I'], item_co['J'], state, col, False)
				if not reach_king:
					reach_king = self.isCornerHorseChecker(item_co['I'], item_co['J'], state, col, True)
			elif pos_type == "pawn":
				reach_king = self.isCornerPawnChecker(item_co['I'], item_co['J'], state, col, is_first, False)
				if not reach_king:
					reach_king = self.isCornerPawnChecker(item_co['I'], item_co['J'], state, col, is_first, True)
			if reach_king:
				init_e = init_e + 900
			check = self.inCheck(item_co['I'], item_co['J'], state , is_first ,col)
			# print("pos %s isfirst: %s incheck: %s"%(pos_id, is_first, check))
			if check:
				check_e = current_c_e
					
			# print("items: %s pos %s init_e: %s check_e %s"%(item, pos, init_e, check_e))
			nextval = init_e + check_e
			if nextval > bestval:
				bestval = nextval
				bestmove = {"pos": pos, "item": item}
			
			counter = counter + 1			
		
		return bestmove

			

	def isRemove(self, dict_input):
		piece = dict_input['pieceId']
		
		if piece != '':
			return True

		return False


	
	def inputFirst(self, firsts, input_id):

		for item in firsts:
			my_id = item['id']
			if my_id == input_id:
				item.update(is_first = False)
			
		return firsts
	


	def processState(self, currentState):
		self.movesdict = [
					{"id": "wpawn1", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn2", "moves": [], "pos": None, "in_check": False}, 
					{"id": "wpawn3", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn4", "moves": [], "pos": None, "in_check": False}, 
					{"id": "wpawn5", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn6", "moves": [], "pos": None, "in_check": False},
					{"id": "wpawn7", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn8", "moves": [], "pos": None, "in_check": False}, 
					{"id": "bpawn1", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn2", "moves": [], "pos": None, "in_check": False},
					{"id": "bpawn3", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn4", "moves": [], "pos": None, "in_check": False}, 
					{"id": "bpawn5", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn6", "moves": [], "pos": None, "in_check": False},
					{"id": "bpawn7", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn8", "moves": [], "pos": None, "in_check": False},
					{"id": "wrook1", "moves": [], "pos": None, "in_check": False}, {"id": "wrook2", "moves": [], "pos": None, "in_check": False},
					{"id": "brook1", "moves": [], "pos": None, "in_check": False}, {"id": "brook2", "moves": [], "pos": None, "in_check": False}, 
					{"id": "wbishop1", "moves": [], "pos": None, "in_check": False}, {"id": "wbishop2", "moves": [], "pos": None, "in_check": False},
					{"id": "bbishop1", "moves": [], "pos": None, "in_check": False}, {"id": "bbishop2", "moves": [], "pos": None, "in_check": False},
					{"id": "whorse1", "moves": [], "pos": None, "in_check": False}, {"id": "whorse2", "moves": [], "pos": None, "in_check": False},
					{"id": "bhorse1", "moves": [], "pos": None, "in_check": False}, {"id": "bhorse2", "moves": [], "pos": None, "in_check": False},
					{"id": "wking", "moves": [], "can_castle": False, "r_castle_rook": None, "l_castle_rook": None, "pos": None, "in_check": False},
					{"id": "bking", "moves": [], "can_castle": False, "r_castle_rook": None, "l_castle_rook": None, "pos": None, "in_check": False},
					{"id": "wqueen", "moves": [], "pos": None, "in_check": False}, {"id": "bqueen", "moves": [], "pos": None, "in_check": False}
				]
		
		self.hasmoved = "N"
		self.hasremoved = "N"
		print("--------out %s"%(currentState != self.statematrix))
		if currentState != self.statematrix:
			self.statematrix = currentState
			
			pieces = self.getPieces(self.statematrix, "black")
			movesdic = self.getMovesDict()
			firsts = self.getFirsts()

			moves = self.getMoves(self.statematrix, firsts, "black", pieces, movesdic)
			mov_dict = self.dictToList(moves, "black")
			recieved = self.evaluate(self.statematrix, mov_dict, "black", firsts)
			# print("------ recieved: %s"%recieved)
			to_pos = recieved['item']
			curr_pos = recieved['pos'] 
			is_rem = self.isRemove(to_pos)

			p_id = to_pos['pieceId']
			pl_id = to_pos['placeId']
			p_co = self.getCoordinates(pl_id)
			c_p_id = curr_pos['pieceId']
			c_pl_id = curr_pos['placeId']
			c_p_co = self.getCoordinates(c_pl_id)
			self.inputFirst(firsts, c_p_id)
			print("--------in %s - %s"%(c_p_id, recieved))

			if is_rem:
				self.compchoice = c_p_id
				self.compremove = p_id
				self.compmove = pl_id
				self.statematrix[c_p_co['I']][c_p_co['J']].update(pieceId='') 
				self.statematrix[p_co['I']][p_co['J']].update(pieceId=c_p_id)	
				self.hasremoved = "Y"
				self.hasmoved = "Y"	
			else:
				self.compchoice = c_p_id
				self.compmove = pl_id
				self.statematrix[c_p_co['I']][c_p_co['J']].update(pieceId='') 
				self.statematrix[p_co['I']][p_co['J']].update(pieceId=c_p_id)	
				self.hasmoved = "Y"

			return to_pos

	# def processState(self, currentState):
		
	# 	self.hasmoved = "N"
	# 	self.hasremoved = "N"

	# 	# self.first = False
	# 	# self.sec = True
	# 	# self.third = True
	# 	# self.fourth = True
	# 	# self.fifth = True
	# 	# self.move7 = True
	# 	# self.move8 = True
	# 	# self.move9 = True
	# 	# self.move10 = True
	# 	# self.move11 = True
	# 	# self.move12 = True
		
	# 	if currentState != self.statematrix:
	# 		self.statematrix = currentState
			
	# 		if not self.first:
	# 			self.compchoice = c_p_id
	# 			self.compremove = p_id
	# 			self.compmove = pl_id
	# 			self.statematrix[c_p_co['I']][c_p_co['J']].update(pieceId='') 
	# 			self.statematrix[p_co['I']][p_co['J']].update(pieceId=c_p_id)	
	# 			self.hasremoved = "Y"
	# 			self.hasmoved = "Y"	
	# 			self.first = True
	# 			self.sec = False
	# 		elif not self.sec:
	# 			self.compchoice = c_p_id
	# 			self.compmove = pl_id
	# 			self.statematrix[c_p_co['I']][c_p_co['J']].update(pieceId='') 
	# 			self.statematrix[p_co['I']][p_co['J']].update(pieceId=c_p_id)	
	# 			self.hasmoved = "Y"
	# 			self.sec = True
	# 			self.third = False	
	# 		elif not self.third:
	# 			self.third = True
	# 			self.fourth = False
	# 		elif not self.fourth:
	# 			self.fourth = True
	# 			self.fifth = False
	# 		elif not self.fifth:
	# 			self.fifth = True
	# 			self.move7 = False
	# 		elif not self.move7:
	# 			self.move7 = True
	# 			self.move8 = False
	# 		elif not self.move8:
	# 			self.move8 = True
	# 			self.move9 = False




		
		
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
		# print("hello robot ne: %s"%self.compNEInCheck)

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
		# if len(curdir)>=2:
			# print("curDir array: %s"%curdir[1])

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

	def getFirsts(self):
		return self.firsttimes

	def getMovesDict(self):
		return self.movesdict
