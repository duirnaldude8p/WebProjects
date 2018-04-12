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
# # # trainstate[1][4].update(pieceId = "")
# trainstate[4][4].update(pieceId = "bpawn1")
# my_state = trainstate[1][4]

# direction = brain.getInGuardDir(4, 4, trainstate, my_state)

# recieved = brain.isInGuard(1, 4, trainstate, "black", direction)

# print("recieved: %s - %s"%(recieved, direction))

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





