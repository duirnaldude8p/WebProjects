from django.test import TestCase

import Roboto

brain = Roboto.Brain()

# colour = brain.getColour("bpawn8")

# my_type = brain.getType("bpawn8")

# print("colour: %s type: %s"%(colour, my_type))

trainstate = brain.getTrainState()

# print("train state: %s"%trainstate)
#4f 4d
# trainstate[1][3].update(pieceId='') 
# trainstate[5][3].update(pieceId='wpawn4')

# trainstate[6][4].update(pieceId='') 
# trainstate[2][4].update(pieceId='bpawn5')

# trainstate[6][4].update(pieceId='') 
# trainstate[2][4].update(pieceId='bpawn5')

# trainstate[0][1].update(pieceId='') 
# trainstate[5][1].update(pieceId='whorse')
trainstate[0][3].update(pieceId='') 
trainstate[5][3].update(pieceId='wking')
# print("changed train state: %s"%trainstate)
my_piece = trainstate[5][3]['pieceId']
my_piece_colour = brain.getColour(my_piece)
print("val: %s"%my_piece_colour)
# my_places = brain.basicRookMovement(3, 5, trainstate, my_piece_colour)
# my_places = brain.basicBishopMovement(3, 5, trainstate, my_piece_colour)
# my_places = brain.basicPawnMovement(2, 4, trainstate, False ,my_piece_colour)
# my_places = brain.basicHorseMovement(0, 1, trainstate, my_piece_colour)
my_places = brain.basicKingMovement(5, 3, trainstate, my_piece_colour)
# brain.setTrainState(trainstate)
# trainstate2 = brain.getTrainState()
# print("set train state: %s"%trainstate2)
print("places: %s"%my_places)