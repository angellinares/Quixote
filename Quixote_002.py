import re

def Findsimilars(set1, list):
	dblCoincidences = []
	for strWord in set1:

		dblCoincidences.append(list.count(strWord))

	return dblCoincidences

def PrintSearch(dblNumb, setKeys):
	count = 0

	for key in setKeys:

		print 'Number of coincidences for the key "' + key.upper() + '": ' + str(dblNumb[count])
		count += 1

def Getkeys ():

	boolCheck = True

	while boolCheck:

		strNewkey = raw_input('Type a new keyword to search')
		if strNewkey == '':
			print 'Upps!, Sorry that is not a valid key.'

strFilename = 'F:\\003_CODE\\Git\\Qixote\\2donq10_mod.txt'
strWords = set(['verde','rojo','amarillo','azul','naranja','magenta','gris','blanco','negro'])

f = open(strFilename,'r')
strF = f.read()
#data  = set(f.read().split(', -	'))
#data =re.findall(r"\w+|[^\w\s]", f, re.UNICODE)

data = set(re.findall(r"[\w']+|[.,!?;]", strF))
for word in data: word.lower()

setIntersect = strWords.intersection(data)

dblCoinc = Findsimilars(strWords,strF)

print setIntersect
print 'Different words: ' + str(len(data))
#print 'Number of coincidences: ' + str(dblCoinc)
PrintSearch(dblCoinc,strWords)


