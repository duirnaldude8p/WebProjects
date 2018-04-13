from django.test import TestCase

import Roboto

brain = Roboto.Brain()

trainstate = brain.getTrainState()

#horse checker
# trainstate[5][4].update(pieceId = "whorse1")

# recieved_horse = brain.horseChecker(7, 3, trainstate, "black")

# print("recieved horse: %s"%recieved_horse)

#rook checker
# trainstate[4][4].update(pieceId = "bking")
# trainstate[1][4].update(pieceId = "")
# trainstate[4][7].update(pieceId = "wrook1")

# recieved_horse = brain.rookChecker(4, 4, trainstate, "black")

# print("recieved horse: %s"%recieved_horse)

#bishop checker
# trainstate[4][4].update(pieceId = "bking")
# trainstate[5][5].update(pieceId = "wbishop1")
# # trainstate[4][7].update(pieceId = "wrook1")

# recieved_horse = brain.bishopChecker(4, 4, trainstate, "black")

# print("recieved horse: %s"%recieved_horse)

#queen checker
# trainstate[4][4].update(pieceId = "wking")
# trainstate[1][1].update(pieceId = "")
# trainstate[0][0].update(pieceId = "bqueen")
# # trainstate[4][7].update(pieceId = "wrook1")

# recieved = brain.queenChecker(4, 4, trainstate, "white")

# print("recieved: %s"%recieved)

#pawn checker
# trainstate[4][5].update(pieceId = "bpawn1")
# # trainstate[1][1].update(pieceId = "")
# trainstate[3][5].update(pieceId = "wking")

# trainstate[4][4].update(pieceId = "bking")
# # trainstate[1][1].update(pieceId = "")
# trainstate[3][5].update(pieceId = "wrook1")
# # trainstate[4][7].update(pieceId = "wrook1")

# recieved = brain.pawnChecker(4, 4, trainstate, "black", True) 

# print("recieved: %s"%recieved)

#rook king checker
# trainstate[4][4].update(pieceId = "wrook")
# # trainstate[1][1].update(pieceId = "")
# trainstate[1][4].update(pieceId = "wking")
# # # trainstate[4][7].update(pieceId = "wrook1")

# recieved = brain.rookKingChecker(4, 4, trainstate, "white")

# print("recieved: %s"%recieved)

#rook check path
# trainstate[4][4].update(pieceId = "bking")
# trainstate[1][4].update(pieceId = "")
# trainstate[4][7].update(pieceId = "wrook1")
# my_state = trainstate[4][7]

# recieved = brain.getRookCheckPath(3, 4, trainstate, my_state)

# print("recieved horse: %s"%recieved)

#bishop check path
# trainstate[4][4].update(pieceId = "bking")
# # trainstate[1][4].update(pieceId = "")
# trainstate[6][5].update(pieceId = "wbishop1")
# my_state = trainstate[6][5]

# recieved = brain.getBishopCheckPath(4, 7, trainstate, my_state)

# print("recieved: %s"%recieved)

#in guard dir and in guard
# trainstate[6][4].update(pieceId = "wbishop")
# # trainstate[1][4].update(pieceId = "")
# trainstate[4][4].update(pieceId = "bpawn1")
# trainstate[0][3].update(pieceId = "")
# trainstate[1][1].update(pieceId = "")
# trainstate[0][0].update(pieceId = "wking")
# trainstate[3][3].update(pieceId = "wbishop1")
# trainstate[5][5].update(pieceId = "wbishop2")
# my_state = trainstate[0][0]

# direction = brain.getInGuardDir(3, 3, trainstate, my_state, "bishop")

# recieved = brain.isInGuard(3, 3, trainstate, "white", direction)

# print("recieveds: %s - %s"%(recieved, direction))

#in check
# trainstate[6][2].update(pieceId = "wqueen")
# # # trainstate[1][4].update(pieceId = "")
# trainstate[4][4].update(pieceId = "bpawn1")
# # my_state = trainstate[1][4]

# recieved = brain.inCheck(4, 4, trainstate, False, "black")
# print("recieved: %s"%recieved)

# #get pieces
# recieved = brain.getPieces(trainstate, "white")

# print("recieved: %s"%recieved)

#find king
# trainstate[0][3].update(pieceId = "")
# trainstate[5][7].update(pieceId = "wking")
# recieved = brain.findKing(trainstate, "white")
# print("recieved: %s"%recieved)

#get item place
# my_dict = brain.getFirsts()
# my_dict2 = brain.getMovesDict()
# recieved = brain.getItemPlace(my_dict2, "brook2")
# print("recieved: %s"%recieved)

#get restricted places
# my_moves = brain.basicRookMovement(1, 0, trainstate, "white")
# my_moves2 = brain.basicRookMovement(4, 4, trainstate, "white")

# recieved = brain.getRestrictedPlaces(my_moves2, my_moves)
# print("recieved: %s"%recieved)#

#is first time
# my_dict = brain.getFirsts()

# recieved = brain.isFirst(my_dict, "wbishop1")
# print("recieved: %s"%recieved)

#right castle
# trainstate[0][1].update(pieceId = "")
# trainstate[0][2].update(pieceId = "")
# trainstate[0][3].update(pieceId = "")
# trainstate[7][5].update(pieceId = "")
# trainstate[7][6].update(pieceId = "")
# trainstate[1][6].update(pieceId = "")
# trainstate[2][6].update(pieceId = "brook1")

# recieved = brain.getRightCastle(7, 4, trainstate, "black")
# print("recieved: %s"%recieved)

#left castle
# trainstate[7][1].update(pieceId = "")
# trainstate[7][2].update(pieceId = "")
# trainstate[7][3].update(pieceId = "")
# trainstate[1][3].update(pieceId = "")
# # trainstate[3][3].update(pieceId = "brook1")

# recieved = brain.getLeftCastle(7, 4, trainstate, "black")
# print("recieved: %s"%recieved)

#MOVE GEN!
# trainstate[0][3].update(pieceId = "")
# trainstate[1][4].update(pieceId = "")
# trainstate[0][2].update(pieceId = "")
# trainstate[0][5].update(pieceId = "")
# trainstate[0][4].update(pieceId = "wking")
# trainstate[3][4].update(pieceId = "wbishop2")
# trainstate[5][4].update(pieceId = "brook1")
# my_state = trainstate[0][4]

# direction = brain.getInGuardDir(3, 4, trainstate, my_state, "bishop")

# recieved = brain.isInGuard(3, 4, trainstate, "white", direction)

# # trainstate[0][1].update(pieceId = "")
# # trainstate[0][2].update(pieceId = "")
# trainstate[6][5].update(pieceId = "")
# # trainstate[7][1].update(pieceId = "")
# # trainstate[7][2].update(pieceId = "")
# # trainstate[0][5].update(pieceId = "")
# # trainstate[0][6].update(pieceId = "")
# trainstate[7][4].update(pieceId = "")
# trainstate[7][5].update(pieceId = "")
# trainstate[7][6].update(pieceId = "")
# # trainstate[0][3].update(pieceId = "wking")
# trainstate[3][5].update(pieceId = "wrook2")
# # trainstate[5][4].update(pieceId = "brook1")

# trainstate[1][3].update(pieceId = "")
# trainstate[4][3].update(pieceId = "brook1")
# trainstate[2][1].update(pieceId = "wrook1")




# pieces = brain.getPieces(trainstate, "white")
# moves = brain.getMovesDict()
# firsts = brain.getFirsts()

# recieved = brain.getMoves(trainstate, firsts, "white", pieces, moves)
# # recieved = brain.basicPawnMovement(1, 2, trainstate, True, "white")
# print("recieved: %s"%recieved)
# print("recieveds: %s - %s"%(recieved, direction))

#evaluate
trainstate[6][3].update(pieceId = "")
trainstate[3][4].update(pieceId = "wrook1")
trainstate[5][5].update(pieceId = "bbishop2")

pieces = brain.getPieces(trainstate, "white")
movesdic = brain.getMovesDict()
firsts = brain.getFirsts()

moves = brain.getMoves(trainstate, firsts, "white", pieces, movesdic)

recieved = brain.evaluate(trainstate, moves, "white")
# recieved = brain.getType("")
print("recieved: %s"%recieved)





