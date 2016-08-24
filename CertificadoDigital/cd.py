#Para sha256
import hashlib
#Para RSA
from Crypto.PublicKey import RSA
from Crypto import Random

def calculate_sha256(arq):
	##Quantidade de bytes lida por vez
	BUF_SIZE = 65536
	sha256 = hashlib.sha256()
	with open(arq, 'rb') as f:
	    while True:
	        data = f.read(BUF_SIZE)
	        if not data:
	            break
	        sha256.update(data)
	return sha256.hexdigest()
random_generator = Random.new().read
key = RSA.generate(2048, random_generator)

public_key = key.publickey()

##Criando o hash do arquivo e encriptando o hash
file_hash = calculate_sha256("arquivo.txt")
enc_file_hash = public_key.encrypt(file_hash, 32)

print (raw_input('Pausa para modificar o arquivo - Tecle enter para continuar'))

##Decriptando o hash e verificando se ele bate com o arquivo
dec_file_hash = key.decrypt(enc_file_hash)
file_hash = calculate_sha256("arquivo.txt")
if(dec_file_hash == file_hash):
	print ("O arquivo esta integro!")
else:
	print ("O arquivo foi modificado!")