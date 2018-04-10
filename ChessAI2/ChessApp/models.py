from django.db import models

# Create your models here.

class StateData(models.Model):
	StateMatrix = models.CharField(max_length=10000, null=True)
	CompChooses = models.CharField(max_length=100, null=True)
	CompMovesTo = models.CharField(max_length=100, null=True)
	CompRemoves = models.CharField(max_length=100, null=True)
	CompMadeMove = models.CharField(max_length=100, null=True)
	CompMadeRemove = models.CharField(max_length=100, null=True)
	RemovedPieces = models.CharField(max_length=1000, null=True)
	Section = models.CharField(max_length=100, null=True)
	CompInCheck = models.CharField(max_length=100, null=True)
	CompNWInCheck = models.CharField(max_length=100, null=True) 
	CompNEInCheck = models.CharField(max_length=100, null=True) 
	CompSWInCheck = models.CharField(max_length=100, null=True) 
	CompSEInCheck = models.CharField(max_length=100, null=True) 
	CompUpInCheck = models.CharField(max_length=100, null=True) 
	CompDownInCheck = models.CharField(max_length=100, null=True) 
	CompRightInCheck = models.CharField(max_length=100, null=True) 
	CompLeftInCheck = models.CharField(max_length=100, null=True)
	CheckMate = models.CharField(max_length=100, null=True)
	FreeMove = models.CharField(max_length=100, null=True)
	CurrentDirectionArray = models.CharField(max_length=1000, null=True)
	AttackerArray = models.CharField(max_length=1000, null=True)
	InGuard = models.CharField(max_length=100, null=True)
	PieceInGuard  = models.CharField(max_length=100, null=True)
	SpaceLength = models.CharField(max_length=100, null=True)
	CanSaveKing = models.CharField(max_length=100, null=True)
	Savers =  models.CharField(max_length=1000, null=True)
	Attackers = models.CharField(max_length=1000, null=True)
	PawnIDArray = models.CharField(max_length=1000, null=True)
	KingHasMoved = models.CharField(max_length=100, null=True)
	Rook1HasMoved = models.CharField(max_length=100, null=True)
	Rook2HasMoved = models.CharField(max_length=100, null=True)
	

