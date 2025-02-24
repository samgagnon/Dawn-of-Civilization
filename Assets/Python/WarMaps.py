from Core import *
from Files import *
from Periods import *
from Events import handler


def applyMap(iCivilization, iPeriod=-1):
	# TODO: do not overwrite existing values with values from the map
	# TODO: set default values for all plots to 5
	for p in plots.all().land():
		p.setWarValue(iCivilization, 0)

	for (x, y), iValue in FileMap.read("War/%s.csv" % civ_name(iCivilization)):
		if iValue and not plot(x, y).isWater():
			plot(x, y).setWarValue(iCivilization, iValue)
	
	if iPeriod != -1:
		for (x, y), iValue in FileMap.read("War/Period/%s.csv" % dPeriodNames[iPeriod], bIgnoreMissing=True):
			if not plot(x, y).isWater():
				plot(x, y).setWarValue(iCivilization, iValue)
			
def init():
	for iCivilization in lBirthOrder:
		applyMap(iCivilization)

# NOTE warmaps are updated when civs are assigned and when the period changes

@handler("playerCivAssigned")
def activate(iPlayer, iCivilization):
	if iCivilization in lBirthOrder:
		applyMap(iCivilization)

@handler("periodChange")
def updateMapOnPeriodChange(iCivilization, iPeriod):
	applyMap(iCivilization, iPeriod)
