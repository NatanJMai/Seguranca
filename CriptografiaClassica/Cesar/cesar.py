import sys

def encrypt(content, key):
	return (bytes((i + key) % 256 for i in content))

def decrypt(enc_content, key):
	return (bytes((i - key) % 256 for i in enc_content))

def usage():
	print("Como usar:")
	print("python "+__file__+" <caminho para o arquivo> <chave>")
	sys.exit()

try:
	arq_name = sys.argv[1]
	chave = int(sys.argv[2])
except:
	usage()

arq = open(arq_name, 'rb')
arq_content = arq.read()
arq.close()

enc_content = encrypt(arq_content, chave)
enc_arq = open("c-cesar"+str(chave), 'wb')
enc_arq.write(enc_content)
enc_arq.close()

dec_content = decrypt(enc_content, chave)
dec_arq = open("d-cesar"+str(chave), 'wb')
dec_arq.write(dec_content)
dec_arq.close()

print ("Arquivo criptografado salvo!")
print ("Arquivo decriptografado salvo!")
