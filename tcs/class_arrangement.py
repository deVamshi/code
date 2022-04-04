
valueOfS = input()

def solvingFunction(valueOfS):
	nValue = len(valueOfS)
	gValue = 0
	bValue = 0
	for i in range(nValue):
		if (valueOfS[i] == 'G'): gValue += 1
		else: bValue += 1
	if (gValue > bValue + 1 or bValue > gValue + 1): return -1
	if (nValue % 2):
		num = (nValue + 1) / 2
		evenGValue = 0
		evenBValue = 0
		for i in range(nValue):
			if (i % 2 == 0):
				if (valueOfS[i] == 'G'):
					evenGValue+=1
				else:
					evenBValue+=1
		if (gValue > bValue): return int(num - evenGValue)
		else: return int(num - evenBValue)
	else:
		oddGValue = 0
		evenGValue = 0
		for i in range(nValue):
			if (valueOfS[i] == 'G'):
				if (i % 2): 
					oddGValue+=1
				else: 
					evenGValue+=1
		return min(nValue // 2 - oddGValue, nValue // 2 - evenGValue)

ans = solvingFunction(valueOfS)
print(ans)