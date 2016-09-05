import sys
from random import shuffle

def encrypt(content, key):
	t = ""
	for i in content:
		t+=chr(key[ord(i)])
	return t

def decrypt(enc_content, key):
	t = ""
	for i in enc_content:
		t+=chr(key[ord(i)])
	return t

def usage():
	print("Como usar:")
	print("python "+__file__+" <caminho para o arquivo>")
	sys.exit()

try:
	arq_name = sys.argv[1]
except:
	usage()

chave = list(range(256))
shuffle(chave)
chave = dict(enumerate(chave))

arq = open(arq_name, 'rb')
arq_content = arq.read()
arq.close()

enc_content = encrypt(arq_content, chave)
enc_arq = open("c-subs", 'wb')
enc_arq.write(enc_content)
enc_arq.close()

dec_content = decrypt(enc_content, {v: k for k, v in chave.items()})
dec_arq = open("d-subs", 'wb')
dec_arq.write(dec_content)
dec_arq.close()

print ("Arquivo criptografado salvo!")
print ("Arquivo decriptografado salvo!")
