import sys

def usage():
    print("Como usar:")
    print("python "+__file__+" <caminho para o arquivo>")
    sys.exit()

try:
    arq_name = sys.argv[1]
except:
    usage()

arq_name = open("words.txt", "r")
words = arq_name.read().split('\n')

pattDic = {}

for w in words:
	count = 0
	patt = ''
	wordPatt = {}

	for c in w:
		if count == 0:
			wordPatt.update({c: count})
			patt += str(count)
			count += 1
		else:
			if wordPatt.get(c) == None:
				wordPatt.update({c: count})
				patt += str(count)
				count += 1
			else:
				patt += str(wordPatt.get(c))
	
	pattDic.update({w: patt})

for k,v in pattDic.items():
	print (k,": ",v)