#tool for calculation of required games to desired stage of marathon

def marathon(stageExpList):
	sumExp=0
	for stageExp in stageExpList:
		sumExp+=stageExp

	return sumExp

renegadeExp=[0,0,0,0,0,0,0,0,0,0]
renegadeExp[0]=3000
renegadeExp[1]=5000
renegadeExp[2]=9000
renegadeExp[3]=17000
renegadeExp[4]=30000
renegadeExp[5]=30000
renegadeExp[6]=32000
renegadeExp[7]=35000
renegadeExp[8]=40000
renegadeExp[9]=50000

bourrasqueExp=[0,0,0,0,0,0,0,0,0,0]
bourrasqueExp[0]=2000
bourrasqueExp[1]=5000
bourrasqueExp[2]=8000
bourrasqueExp[3]=17000
bourrasqueExp[4]=28000
bourrasqueExp[5]=30000
bourrasqueExp[6]=30000
bourrasqueExp[7]=35000
bourrasqueExp[8]=40000
bourrasqueExp[9]=50000

#print(marathon(renegadeExp))
#print(marathon(bourrasqueExp))
#print(marathon(bourrasqueExp)/(marathon(renegadeExp)))

def minimumGamesRequired(currentStage, currentStageExp, targetStage, stageExpList):
	currentStage-=1
	targetStage-=1
	sumCurrentExp=currentStageExp
	sumRequiredExp=0
	for stageExp in range(0,len(stageExpList)):
		if currentStage>=stageExp:
			sumCurrentExp+=stageExpList[stageExp]
		if targetStage>=stageExp:
			sumRequiredExp+=stageExpList[stageExp]
	return((sumRequiredExp-sumCurrentExp)/550)

#print(minimumGamesRequired(2,500,6,bourrasqueExp))

def minimumGamesRequiredPerDay(currentStage, currentStageExp, targetStage, daysLeft, stageExpList):
	currentStage-=1
	targetStage-=1
	sumCurrentExp=currentStageExp
	sumRequiredExp=0
	for stageExp in range(0,len(stageExpList)):
		if currentStage>=stageExp:
			sumCurrentExp+=stageExpList[stageExp]
		if targetStage>=stageExp:
			sumRequiredExp+=stageExpList[stageExp]
	return((sumRequiredExp-sumCurrentExp)/550/daysLeft)

#print(minimumGamesRequiredPerDay(2,500,6,7,bourrasqueExp))


def minimumGamesRequiredPerDayInteractive(stageExpList):
	# while True:
	# 	currentStage=input("Current stage: ")
	# 	try:
	# 		currentStage=int(currentStage)
	# 	except ValueError:
	# 		print("Put in a valid number.")
	# 	else:
	# 		break
	currentStage=inputCheckInt("Current stage: ")
	currentStageExp=inputCheckInt("XP on current stage: ")
	targetStage=inputCheckInt("Target stage: ")
	daysLeft=inputCheckInt("Days left: ")
	averageExp=inputCheckInt("Average XP per game: ")
	currentStage-=1
	targetStage-=1
	sumCurrentExp=currentStageExp
	sumRequiredExp=0
	for stageExp in range(0,len(stageExpList)):
		if currentStage>stageExp:
			sumCurrentExp+=stageExpList[stageExp]
		if targetStage>=stageExp:
			sumRequiredExp+=stageExpList[stageExp]
	minimumGamesLeft=(sumRequiredExp-sumCurrentExp)/averageExp
	minimumGamesLeft=round(minimumGamesLeft)
	averageGamesPerDay=minimumGamesLeft/daysLeft
	averageGamesPerDay=round(averageGamesPerDay)
	print("Minimum number of games required: "+str(minimumGamesLeft))
	print("Average number of games required per day: "+str(averageGamesPerDay))


def inputCheckInt(message):
	while True:
		var=input(message)
		try:
			var=int(var)
		except ValueError:
			print("Put in a valid number.")
		else:
			return var
			break


#Es ist moeglich der Funktion den Datentyp fuer das Typecasting als Argument zu uebergeben.
def inputCheckDatatype(message, type):
	while True:
		var=input(message)
		try:
			var=type(var)
		except ValueError:
			print("Input has to be "+str(type)+"!")
		else:
			return var
			break



minimumGamesRequiredPerDayInteractive(bourrasqueExp)





