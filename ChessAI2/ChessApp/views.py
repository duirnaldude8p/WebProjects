from django.shortcuts import render

from django.http import JsonResponse

from django.template import loader

from django.http import HttpResponse

from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_protect

from django.core import serializers

import json

from ast import literal_eval

# Create your views here.

from .models import StateData

from . import Roboto


obj = {}
newdata = {}
brain = Roboto.Brain()
restart = False;
def main_page(request):
	page = 'chessboard.html'    
	return render(request, page)

def download_page(request):
	if request.method == "GET":
		data = open('ChessApp\static\json\playing_data.json')
		dictdata = json.load(data)

		global obj
		global newdata
		global brain
		global restart

		#restart = False;
		if not restart:
			brain = Roboto.Brain()

			#'''
			obj = {}
			newdata = {}

			StateData.objects.all().delete()
 			#'''

			#'''
			StateData.objects.create(
				StateMatrix = brain.getState(),
				CompChooses = brain.getChoice(),
				CompMovesTo = brain.getMove(),
				CompMadeMove = brain.getHasMoved(),
				CompInCheck = dictdata["StateData"]["CompInCheck"],
				CompNWInCheck = dictdata["StateData"]["CompNWInCheck"], 
				CompNEInCheck = dictdata["StateData"]["CompNEInCheck"], 
				CompSWInCheck = dictdata["StateData"]["CompSWInCheck"], 
				CompSEInCheck = dictdata["StateData"]["CompSEInCheck"], 
				CompUpInCheck = dictdata["StateData"]["CompUpInCheck"], 
				CompDownInCheck = dictdata["StateData"]["CompDownInCheck"], 
				CompRightInCheck = dictdata["StateData"]["CompRightInCheck"], 
				CompLeftInCheck = dictdata["StateData"]["CompLeftInCheck"],
				CheckMate = dictdata["StateData"]["CheckMate"],
				FreeMove = dictdata["StateData"]["FreeMove"],
				CurrentDirectionArray = dictdata["StateData"]["CurrentDirectionArray"],
				AttackerArray = dictdata["StateData"]["AttackerArray"],
				InGuard = dictdata["StateData"]["InGuard"],
				PieceInGuard  = dictdata["StateData"]["PieceInGuard"],
				SpaceLength = dictdata["StateData"]["SpaceLength"],
				CanSaveKing = dictdata["StateData"]["CanSaveKing"],
				Section = "StateData"
			)
			restart = True
			#print("hello restart")
			#'''

		#'''
		print('is StateData %s' %StateData.objects.get(Section="StateData"))
		#'''

		#'''
		val = ''
		if StateData.objects.all():
			val = StateData.objects.all()	
		#'''

		#'''
		if restart:	
			if val!='':	
				raw_data = serializers.serialize('python', val)
				actual_data = raw_data[0]['fields']
				output = json.dumps(actual_data)
				newdata = json.loads(output)
				obj.update(StateData=newdata)
		#'''

		return JsonResponse(obj, safe=False)
	else:
		return HttpResponse('no get', request)

def create_page(request):
	if request.method == "POST":
		#'''
		global obj
		global newdata
		global brain
		#'''
		
		#'''
		if restart:
			if request.POST.get('section') == "StateMatrix":
				statematrix = request.POST.get('statemat')
				statematrix = literal_eval(statematrix)
				cmpcheck = request.POST.get("incheck")
				cmpnwcheck = request.POST.get("nwcheck")
				cmpnecheck = request.POST.get("necheck")
				#print("view ne: %s"%cmpnecheck)
				cmpswcheck = request.POST.get("swcheck")
				cmpsecheck = request.POST.get("secheck")
				cmpupcheck = request.POST.get("upcheck")
				cmpdowncheck = request.POST.get("downcheck")
				cmprightcheck = request.POST.get("rightcheck")
				cmpleftcheck = request.POST.get("leftcheck")
				cmpmate = request.POST.get("checkmate")
				cmpfreemove = request.POST.get("freemove")
				cmpcurrdir = request.POST.get("currentdirarr")
				cmpcurrdir = literal_eval(cmpcurrdir)
				print("view: %s"%cmpcurrdir)
				cmpattarr = request.POST.get("attackerarray")
				#cmpattarr = literal_eval(cmpattarr)
				cmpingrd = request.POST.get("inguard")
				cmppingrd = request.POST.get("pieceinguard")
				cmpspclnght = request.POST.get("spacelength")
				cmpspclnght = int(cmpspclnght)
				cmpcsk = request.POST.get("cansaveking")
				cmpatkrs = request.POST.get("attackers")
				cmpatkrs = literal_eval(cmpatkrs)
				cmpsavers = request.POST.get("savers")
				cmpsavers = literal_eval(cmpsavers)
				brain.setCompInCheck(cmpcheck, cmpnwcheck, cmpnecheck, cmpswcheck, cmpsecheck, cmpupcheck, cmpdowncheck, cmprightcheck, cmpleftcheck )
				brain.setCheckInfo(cmpmate, cmpfreemove, cmpcurrdir, cmpattarr, cmpingrd, cmppingrd, cmpspclnght, cmpcsk, cmpsavers, cmpatkrs)
				brain.processState(statematrix)
				#print("compchoice: %s"%brain.getChoice())
				#print("compmove: %s"%brain.getMove())
				StateData.objects.all().delete()
				StateData.objects.create(
					StateMatrix = brain.getState(),
					CompChooses = brain.getChoice(),
					CompMovesTo = brain.getMove(),
					CompMadeMove = brain.getHasMoved(),
					CompInCheck = brain.getCompInCheck(),
					CompNWInCheck = brain.getCompNWInCheck(), 
					CompNEInCheck = brain.getCompNEInCheck(), 
					CompSWInCheck = brain.getCompSWInCheck(), 
					CompSEInCheck = brain.getCompSEInCheck(), 
					CompUpInCheck = brain.getCompUpInCheck(), 
					CompDownInCheck = brain.getCompDownInCheck(), 
					CompRightInCheck = brain.getCompRightInCheck(), 
					CompLeftInCheck = brain.getCompLeftInCheck(),
					CheckMate = brain.getCheckMate(),
					FreeMove = brain.getFreeMove(),
					CurrentDirectionArray = brain.getCurrentDirectionArray(),
					AttackerArray = brain.getAttackerArray(),
					InGuard = brain.getInGuard(),
					PieceInGuard  = brain.getPieceInGuard(),
					SpaceLength = brain.getSpaceLength(),
					CanSaveKing = brain.getCanSaveKing(),
					Savers = brain.getSavers(),
					Attackers = brain.getAttackers(),
					Section = "StateData"
				)


				val = ''
				if StateData.objects.all():
					val = StateData.objects.all()	

			
				if val!='':	
					raw_data = serializers.serialize('python', val)
					actual_data = raw_data[0]['fields']
					output = json.dumps(actual_data)
					newdata = json.loads(output)
					obj.update(StateData=newdata)
		#'''
			
		#print('post: %s'%request.POST[''])

		return HttpResponseRedirect('/ChessApp/download_page/')
	else:
		return HttpResponse('no create', request)

def setRestart(start):
	global restart
	restart = start

def restart():
	return restart




