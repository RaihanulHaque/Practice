
def FillText(plain) :
	if len(plain) > 4 and len(plain) < 9 :
		empty = 9 - len(plain)
		for i in range(0,empty) :
			plain.append("0")
	
	elif len(plain) > 9 and len(plain) < 16 :
		empty = 16 - len(plain)
		for i in range(0,empty) :
			plain.append("0")
	
	elif len(plain) > 16 and len(plain) < 25 :
		empty = 25 - len(plain)
		for i in range(0,empty) :
			plain.append("0")
			
	elif len(plain) > 25 and len(plain) < 36 :
		empty = 36 - len(plain)
		for i in range(0,empty) :
			plain.append("0")
			
	else:
		print("Enter between 4 - 36")
	return plain

#plain = list("ALLAH MUHAMMAD PARENTS AURORA SOFTWARE PROGRAMMING CODE PYTHON IRONMAN TECHNOLOGY QURAN ROLLS ROYCE AUDI MERCEDES BENZ AI GENETICS COMPUTER CERN PARTICLE VIBRANIUM ASTROPHYSICS QUANTUM ARC REACTOR NANOTECHNOLOGY JAEGER LE COULTRE OMEGA LINUX CPP INFINITY STONE STORMBREAKER WARM HOLE PHYSICS WAKANDA DOCTOR STRANGE NUCLEAR MACBOOK GOOGLE APPLE STARTUP JAVASCRIPT SQL JARVIS SPACEX MOVIES MACHINE LEARNING WEB DEVELOPMENT HADITH EDITH AUGMENTED REALITY WEAPONS SERVER AMD THREAD RIPPER EPYC STARK INDUSTRIES PALLADIUM URANIUM SUPERMAN KRYPTON HULK BLUSTER ENERGY DNA GALAXY HAREM SAITAMA RIMURU VALI AKIHIKO KAYABA ANOS ANIME LIGHT DEUSOLBERT BERCOULI ALICE KIRITO GENOS RIAS AKENO ALBION  SAIRAORG SHION GABIRU BENIMARU MILIM PLATINUM SENKU DR STONE CAUTIOUS HERO SHIELD HERO ISSEKAI BALANCE BREAK VIXUR UL SHASTA VELDORA CALTECH HARVARD CS50 DJANGO OPENCV MIT ACPC")
plain = list("RAIHANUL")
asciiList = []
hex = []
if len(plain) == 4 or len(plain) == 9 or len(plain) == 16 or len(plain) == 25 or len(plain) == 36 :
	filledText = plain
else :
	filledText = FillText(plain)
	
for i in range(0,len(filledText)) :
	asciiList.append(ord(filledText[i]) + 82)
	
#for i in range(0,len(asciiList)) :
	#hex.append(format(ord(asciiList[i]),"x"))
	
print(asciiList)
#print(hex)