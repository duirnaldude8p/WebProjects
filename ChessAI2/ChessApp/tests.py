# from django.test import TestCase

# import Roboto

# brain = Roboto.Brain()

# trainstate = brain.getTrainState()


# #gameplay 2.0

# trainstate[1][3].update(pieceId = "")
# trainstate[1][4].update(pieceId = "")
# trainstate[2][3].update(pieceId = "wpawn4")
# trainstate[2][4].update(pieceId = "wpawn5")
# trainstate[0][1].update(pieceId = "")
# trainstate[2][2].update(pieceId = "whorse1")
# trainstate[7][2].update(pieceId = "")
# trainstate[5][0].update(pieceId = "bbishop1")
# trainstate[6][4].update(pieceId = "")
# trainstate[5][4].update(pieceId = "bpawn5")
# trainstate[6][1].update(pieceId = "")
# trainstate[5][1].update(pieceId = "bpawn2")
# trainstate[1][5].update(pieceId = "")
# trainstate[3][5].update(pieceId = "wpawn6")



# recieved = brain.processState(trainstate)

# print("recieved: %s"%recieved)


# # #castling 2.0

# # # brain.movesdict = [
# # # 					{"id": "wpawn1", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn2", "moves": [], "pos": None, "in_check": False}, 
# # # 					{"id": "wpawn3", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn4", "moves": [], "pos": None, "in_check": False}, 
# # # 					{"id": "wpawn5", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn6", "moves": [], "pos": None, "in_check": False},
# # # 					{"id": "wpawn7", "moves": [], "pos": None, "in_check": False}, {"id": "wpawn8", "moves": [], "pos": None, "in_check": False}, 
# # # 					{"id": "bpawn1", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn2", "moves": [], "pos": None, "in_check": False},
# # # 					{"id": "bpawn3", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn4", "moves": [], "pos": None, "in_check": False}, 
# # # 					{"id": "bpawn5", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn6", "moves": [], "pos": None, "in_check": False},
# # # 					{"id": "bpawn7", "moves": [], "pos": None, "in_check": False}, {"id": "bpawn8", "moves": [], "pos": None, "in_check": False},
# # # 					{"id": "wrook1", "moves": [], "pos": None, "in_check": False}, {"id": "wrook2", "moves": [], "pos": None, "in_check": False},
# # # 					{"id": "brook1", "moves": [], "pos": None, "in_check": False}, {"id": "brook2", "moves": [], "pos": None, "in_check": False}, 
# # # 					{"id": "wbishop1", "moves": [], "pos": None, "in_check": False}, {"id": "wbishop2", "moves": [], "pos": None, "in_check": False},
# # # 					{"id": "bbishop1", "moves": [], "pos": None, "in_check": False}, {"id": "bbishop2", "moves": [], "pos": None, "in_check": False},
# # # 					{"id": "whorse1", "moves": [], "pos": None, "in_check": False}, {"id": "whorse2", "moves": [], "pos": None, "in_check": False},
# # # 					{"id": "bhorse1", "moves": [], "pos": None, "in_check": False}, {"id": "bhorse2", "moves": [], "pos": None, "in_check": False},
# # # 					{"id": "wking", "moves": [], "can_castle": False, "r_castle_rook": None, "l_castle_rook": None, "end_king": None, "end_rook": None, "pos": None, "in_check": False},
# # # 					{"id": "bking", "moves": [], "can_castle": False, "r_castle_rook": None, "l_castle_rook": None, "end_king": None, "end_rook": None, "pos": None, "in_check": False},
# # # 					{"id": "wqueen", "moves": [], "pos": None, "in_check": False}, {"id": "bqueen", "moves": [], "pos": None, "in_check": False}
# # # 				]

# # # trainstate[5][1].update(pieceId = "wpawn1")
# # # # trainstate[1][0].update(pieceId = "")

# # # firsts = brain.getFirsts()
# # # movesdic = brain.getMovesDict()
# # # pieces = brain.getPieces(trainstate, "black")
# # # c_state = brain.toQueen(trainstate, pieces, "black", brain.pawnEnds, movesdic, firsts)	
# # # is_rem = False		

# # # newstate = c_state['state']
# # # newdict = c_state['dict']
# # # if newstate is not None and newdict is not None:
# # # 	trainstate = newstate
# # # 	newpieces = brain.getPieces(newstate, "black")

# # # 	moves = brain.getMoves(newstate, firsts, "black", newpieces, newdict, brain.pawnEnds)
# # # 	mov_dict = brain.dictToList(moves, "black")
# # # 	recieved = brain.evaluate(newstate, mov_dict, "black", firsts)
# # # 	dictlen = len(newdict)
# # # 	# rint("--------in %s - %s - %s - %s"%( recieved, newdict[dictlen-1], self.statematrix[0][0], self.pawnEnds[8]))
				
# # # else:
# # # 	moves = brain.getMoves(trainstate, firsts, "black", pieces, movesdic, brain.pawnEnds)
# # # 	mov_dict = brain.dictToList(moves, "black")
# # # 	recieved = brain.evaluate(trainstate, mov_dict, "black", firsts)
# # # 	# print("--------in %s - %s - %s"%( recieved, self.statematrix[0][0], self.pawnEnds[8]))


# # # print("recieved: %s"%recieved)

# # # trainstate[7][1].update(pieceId = "")
# # # trainstate[7][2].update(pieceId = "")
# # # trainstate[7][3].update(pieceId = "")
# # # # trainstate[7][5].update(pieceId = "")
# # # # trainstate[7][6].update(pieceId = "")
# # # # trainstate[1][6].update(pieceId = "")
# # # # trainstate[2][6].update(pieceId = "brook1")

# # # # recieved = brain.getLeftCastle(0, 4, trainstate, "white")

# # # recieved = brain.processState(trainstate)

# # # print("recieved: %s"%recieved)

# # #game play
# # # trainstate[6][0].update(pieceId = "")
# # # trainstate[5][0].update(pieceId = "")
# # # # trainstate[4][0].update(pieceId = "bpawn1")
# # # trainstate[1][4].update(pieceId = "")
# # # # trainstate[2][4].update(pieceId = "wpawn5")
# # # trainstate[1][3].update(pieceId = "")
# # # trainstate[2][3].update(pieceId = "wpawn4")
# # # # trainstate[0][3].update(pieceId = "")
# # # # trainstate[4][7].update(pieceId = "wqueen")
# # # # trainstate[3][7].update(pieceId = "wrook1")
# # # # trainstate[0][3].update(pieceId = "")
# # # # trainstate[2][5].update(pieceId = "bqueen")
# # # recieved = brain.processState(trainstate)

# # # print("recieved: %s"%recieved)

# # #horse checker
# # # trainstate[5][4].update(pieceId = "whorse1")

# # # recieved_horse = brain.horseChecker(7, 3, trainstate, "black")

# # # print("recieved horse: %s"%recieved_horse)

# # #rook checker
# # # trainstate[4][4].update(pieceId = "bking")
# # # trainstate[1][4].update(pieceId = "")
# # # trainstate[4][7].update(pieceId = "wrook1")

# # # recieved_horse = brain.rookChecker(4, 4, trainstate, "black")

# # # print("recieved horse: %s"%recieved_horse)

# # #bishop checker
# # # trainstate[4][4].update(pieceId = "bking")
# # # trainstate[5][5].update(pieceId = "wbishop1")
# # # # trainstate[4][7].update(pieceId = "wrook1")

# # # recieved_horse = brain.bishopChecker(4, 4, trainstate, "black")

# # # print("recieved horse: %s"%recieved_horse)

# # #queen checker
# # # trainstate[4][4].update(pieceId = "wking")
# # # trainstate[1][1].update(pieceId = "")
# # # trainstate[0][0].update(pieceId = "bqueen")
# # # # trainstate[4][7].update(pieceId = "wrook1")

# # # recieved = brain.queenChecker(4, 4, trainstate, "white")

# # # print("recieved: %s"%recieved)

# # #pawn checker
# # # trainstate[4][5].update(pieceId = "bpawn1")
# # # # trainstate[1][1].update(pieceId = "")
# # # trainstate[3][5].update(pieceId = "wking")

# # # trainstate[4][4].update(pieceId = "bking")
# # # # trainstate[1][1].update(pieceId = "")
# # # trainstate[3][5].update(pieceId = "wrook1")
# # # # trainstate[4][7].update(pieceId = "wrook1")

# # # recieved = brain.pawnChecker(4, 4, trainstate, "black", True) 

# # # print("recieved: %s"%recieved)

# # #rook king checker
# # # trainstate[4][4].update(pieceId = "wrook")
# # # # trainstate[1][1].update(pieceId = "")
# # # trainstate[1][4].update(pieceId = "wking")
# # # # # trainstate[4][7].update(pieceId = "wrook1")

# # # recieved = brain.rookKingChecker(4, 4, trainstate, "white")

# # # print("recieved: %s"%recieved)

# # #rook check path
# # # trainstate[4][4].update(pieceId = "bking")
# # # trainstate[1][4].update(pieceId = "")
# # # trainstate[4][7].update(pieceId = "wrook1")
# # # my_state = trainstate[4][7]

# # # recieved = brain.getRookCheckPath(3, 4, trainstate, my_state)

# # # print("recieved horse: %s"%recieved)

# # #bishop check path
# # # trainstate[4][4].update(pieceId = "bking")
# # # # trainstate[1][4].update(pieceId = "")
# # # trainstate[6][5].update(pieceId = "wbishop1")
# # # my_state = trainstate[6][5]

# # # recieved = brain.getBishopCheckPath(4, 7, trainstate, my_state)

# # # print("recieved: %s"%recieved)

# # #in guard dir and in guard
# # # trainstate[6][4].update(pieceId = "wbishop")
# # # # trainstate[1][4].update(pieceId = "")
# # # trainstate[4][4].update(pieceId = "bpawn1")
# # # trainstate[0][3].update(pieceId = "")
# # # trainstate[1][1].update(pieceId = "")
# # # trainstate[0][0].update(pieceId = "wking")
# # # trainstate[3][3].update(pieceId = "wbishop1")
# # # trainstate[5][5].update(pieceId = "wbishop2")
# # # my_state = trainstate[0][0]

# # # direction = brain.getInGuardDir(3, 3, trainstate, my_state, "bishop")

# # # recieved = brain.isInGuard(3, 3, trainstate, "white", direction)

# # # print("recieveds: %s - %s"%(recieved, direction))

# # #in check
# # # trainstate[6][2].update(pieceId = "wqueen")
# # # # # trainstate[1][4].update(pieceId = "")
# # # trainstate[4][4].update(pieceId = "bpawn1")
# # # # my_state = trainstate[1][4]

# # # recieved = brain.inCheck(4, 4, trainstate, False, "black")
# # # print("recieved: %s"%recieved)

# # # #get pieces
# # # recieved = brain.getPieces(trainstate, "white")

# # # print("recieved: %s"%recieved)

# # #find king
# # # trainstate[0][3].update(pieceId = "")
# # # trainstate[5][7].update(pieceId = "wking")
# # # recieved = brain.findKing(trainstate, "white")
# # # print("recieved: %s"%recieved)

# # #get item place
# # # my_dict = brain.getFirsts()
# # # my_dict2 = brain.getMovesDict()
# # # recieved = brain.getItemPlace(my_dict2, "brook2")
# # # print("recieved: %s"%recieved)

# # #get restricted places
# # # my_moves = brain.basicRookMovement(1, 0, trainstate, "white")
# # # my_moves2 = brain.basicRookMovement(4, 4, trainstate, "white")

# # # recieved = brain.getRestrictedPlaces(my_moves2, my_moves)
# # # print("recieved: %s"%recieved)#

# # #is first time
# # # my_dict = brain.getFirsts()

# # # recieved = brain.isFirst(my_dict, "wbishop1")
# # # print("recieved: %s"%recieved)

# # #right castle
# # # trainstate[0][1].update(pieceId = "")
# # # trainstate[0][2].update(pieceId = "")
# # # trainstate[0][3].update(pieceId = "")
# # # trainstate[7][5].update(pieceId = "")
# # # trainstate[7][6].update(pieceId = "")
# # # trainstate[1][6].update(pieceId = "")
# # # trainstate[2][6].update(pieceId = "brook1")

# # # recieved = brain.getRightCastle(7, 4, trainstate, "black")
# # # print("recieved: %s"%recieved)

# # #left castle
# # # trainstate[7][1].update(pieceId = "")
# # # trainstate[7][2].update(pieceId = "")
# # # trainstate[7][3].update(pieceId = "")
# # # trainstate[1][3].update(pieceId = "")
# # # # trainstate[3][3].update(pieceId = "brook1")

# # # recieved = brain.getLeftCastle(7, 4, trainstate, "black")
# # # print("recieved: %s"%recieved)

# # #MOVE GEN!
# # # trainstate[0][3].update(pieceId = "")
# # # trainstate[1][4].update(pieceId = "")
# # # trainstate[0][2].update(pieceId = "")
# # # trainstate[0][5].update(pieceId = "")
# # # trainstate[0][4].update(pieceId = "wking")
# # # trainstate[3][4].update(pieceId = "wbishop2")
# # # trainstate[5][4].update(pieceId = "brook1")
# # # my_state = trainstate[0][4]

# # # direction = brain.getInGuardDir(3, 4, trainstate, my_state, "bishop")

# # # recieved = brain.isInGuard(3, 4, trainstate, "white", direction)

# # # # trainstate[0][1].update(pieceId = "")
# # # # trainstate[0][2].update(pieceId = "")
# # # trainstate[6][5].update(pieceId = "")
# # # # trainstate[7][1].update(pieceId = "")
# # # # trainstate[7][2].update(pieceId = "")
# # # # trainstate[0][5].update(pieceId = "")
# # # # trainstate[0][6].update(pieceId = "")
# # # trainstate[7][4].update(pieceId = "")
# # # trainstate[7][5].update(pieceId = "")
# # # trainstate[7][6].update(pieceId = "")
# # # # trainstate[0][3].update(pieceId = "wking")
# # # trainstate[3][5].update(pieceId = "wrook2")
# # # # trainstate[5][4].update(pieceId = "brook1")

# # # trainstate[1][3].update(pieceId = "")
# # # trainstate[4][3].update(pieceId = "brook1")
# # # trainstate[2][1].update(pieceId = "wrook1")




# # # pieces = brain.getPieces(trainstate, "white")
# # # moves = brain.getMovesDict()
# # # firsts = brain.getFirsts()

# # # recieved = brain.getMoves(trainstate, firsts, "white", pieces, moves)
# # # # recieved = brain.basicPawnMovement(1, 2, trainstate, True, "white")
# # # print("recieved: %s"%recieved)
# # # print("recieveds: %s - %s"%(recieved, direction))

# # #evaluate
# # # trainstate[6][0].update(pieceId = "")
# # # trainstate[5][0].update(pieceId = "")
# # # trainstate[4][0].update(pieceId = "bpawn1")
# # # trainstate[6][1].update(pieceId = "")
# # # trainstate[6][2].update(pieceId = "")
# # # trainstate[5][1].update(pieceId = "bpawn2")
# # # trainstate[4][2].update(pieceId = "bpawn3")
# # # trainstate[1][2].update(pieceId = "")
# # # trainstate[2][2].update(pieceId = "wpawn3")
# # # # trainstate[1][1].update(pieceId = "")
# # # # trainstate[2][1].update(pieceId = "wpawn2")
# # # # trainstate[2][0].update(pieceId = "bbishop1")

# # # pieces = brain.getPieces(trainstate, "white")
# # # movesdic = brain.getMovesDict()
# # # firsts = brain.getFirsts()

# # # moves = brain.getMoves(trainstate, firsts, "white", pieces, movesdic)
# # # mov_dict = brain.dictToList(moves, "white")
# # # recieved = brain.evaluate(trainstate, mov_dict, "white", firsts)
# # # # recieved = brain.getType("")
# # # print("recieved: %s"%recieved)





