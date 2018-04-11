from django.test import TestCase

import Roboto

brain = Roboto.Brain()

# colour = brain.getColour("bpawn8")

# my_type = brain.getType("bpawn8")

# print("colour: %s type: %s"%(colour, my_type))

trainstate = brain.getTrainState()

# # print("train state: %s"%trainstate)
# #4f 4d
# trainstate[1][3].update(pieceId='') 
# trainstate[2][3].update(pieceId='wpawn4')

# # trainstate[1][4].update(pieceId='') 
# # trainstate[2][4].update(pieceId='bpawn5')
# trainstate[1][6].update(pieceId='') 
# trainstate[3][6].update(pieceId='bpawn5')
# trainstate[0][2].update(pieceId='') 
# trainstate[3][5].update(pieceId='bbishop1')

# # trainstate[0][1].update(pieceId='') 
# # trainstate[5][1].update(pieceId='whorse')
# # trainstate[0][3].update(pieceId='') 
# trainstate[1][0].update(pieceId='wking')
# trainstate[5][0].update(pieceId='brook1')
# trainstate[3][0].update(pieceId='wpawn3')
# # print("changed train state: %s"%trainstate)
# my_place = trainstate[1][0]
# my_piece = trainstate[3][0]['pieceId']
my_piece_colour = "white"
print("val: %s"%my_piece_colour)
# # my_places = brain.basicRookMovement(3, 5, trainstate, my_piece_colour)
# my_places = brain.basicBishopMovement(3, 5, trainstate, my_piece_colour)
# # my_places = brain.basicPawnMovement(2, 4, trainstate, False ,my_piece_colour)
# # my_places = brain.basicHorseMovement(0, 1, trainstate, my_piece_colour)
# # my_places = brain.basicKingMovement(5, 3, trainstate, my_piece_colour)
# my_places = brain.getRookCheckPath(3, 0, trainstate, my_place)
# my_places = brain.getBishopCheckPath(3, 5, trainstate, my_place)#
my_pieces = brain.getPieces(trainstate, my_piece_colour)
my_places = brain.getMoves(trainstate, True, my_piece_colour, my_pieces)
# direction = brain.getInGuardDir(3, 0, trainstate, my_place)
# isInGuard = brain.isInGuard(3, 0, trainstate, my_piece_colour, direction)
# # brain.setTrainState(trainstate)
# my_places = brain.smoothenArray(my_places, trainstate[3][5])
# # trainstate2 = brain.getTrainState()
# # print("set train state: %s"%trainstate2)
print("places: %s"%my_places)
# print("is in guard: %s"%isInGuard)

# my_coord = brain.getCoordinates("r1D")

# print("co-ord: %s - %s"%(my_coord["I"], my_coord["J"]))


