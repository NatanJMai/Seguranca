import sys
from math import ceil

def encrypt(content, key):
	t = bytes()
	for i in range(0, key):
		t += content[i::key]
	return t
	
def decrypt(enc_content, key):
	t = bytes()
	deckey = ceil(len(enc_content)/key)
	for i in range(0, deckey):
		t += enc_content[i::deckey]
	return t

def usage():
	print("Como usar:")
	print("python "+__file__+" <caminho para o arquivo> <chave>")
	sys.exit()

try:
	arq_name = sys.argv[1]
	chave = sys.argv[2]
except:
	usage()

arq = open(arq_name, 'rb')
arq_content = arq.read()
arq.close()

##Completar com # os espacos vazios da matriz
adicionar = b"#"*(-len(arq_content)%int(chave))
arq_content += adicionar

enc_content = encrypt(arq_content, int(chave))
enc_arq = open("c-transp-"+str(chave), 'wb')
enc_arq.write(enc_content)
enc_arq.close()
print ("Arquivo criptografado salvo!")
dec_content = decrypt(enc_content, int(chave))
dec_arq = open("d-transp-"+str(chave), 'wb')
dec_arq.write(dec_content)
dec_arq.close()
print ("Arquivo decriptografado salvo!")
