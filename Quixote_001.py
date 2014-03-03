import re

def Findsimilars(set1, list):

	for strWord in set1:

		dblCoincidences = list.count(strWord)

	return dblCoincidences

strFilename = 'F:\\003_CODE\\Git\\Qixote\\2donq10_mod.txt'
strWords = set(['verde'])

f = open(strFilename,'r')
strF = f.read()
#data  = set(f.read().split(', -	'))
#data =re.findall(r"\w+|[^\w\s]", f, re.UNICODE)

data = set(re.findall(r"[\w']+|[.,!?;]", strF))

setIntersect = strWords.intersection(data)

dblCoinc = Findsimilars(strWords,strF)

print setIntersect
print 'Different words: ' + str(len(data))
print 'Number of coincidences: ' + str(dblCoinc)


