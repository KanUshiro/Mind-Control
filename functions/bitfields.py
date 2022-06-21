ButtonPressListOE = ["Unknown8","Unknown7","Unknown6","Unknown5","D-Pad Right","D-Pad Left","D-Pad Down","D-Pad Up","L2","R2", "R1", "L1", "Cross", "Circle", "Triangle", "Square"]

def bitfield(num):
	bitfieldlist = [1 if num & (1 << (7-n)) else 0 for n in range(8)]
	if len(bitfieldlist) < 8:
		append = 8 - len(bitfieldlist)
		x = 0
		while x < append:
			bitfieldlist.append(0)
			x = x + 1
	return bitfieldlist
	
def bitfieldListMask(bitfield, List):
	curstring = ""
	x = 0
	while x < len(List):
		if bitfield[x] == 1:
			if curstring == "":
				curstring = List[x]
			else:
				curstring = curstring + "," + List[x]
		x = x + 1
	return curstring

def iterateStringstoBits(Bitlist, Bitstringlist):
	StringList = Bitstringlist.split(",")
	Newbitlist = []
	x = 0
	while x < len(Bitlist):
		bitvalue = 0
		y = 0
		while y < len(StringList):
			if StringList[y].lower() == Bitlist[x].lower(): bitvalue = 1
			y = y + 1
		Newbitlist.append(bitvalue)
		x = x + 1
	return Newbitlist    

    
def bitlistToInteger(Bitlist):
	return int("".join(str(x) for x in Bitlist), 2)