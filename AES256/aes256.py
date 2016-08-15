from Crypto.Cipher import AES
from Crypto import Random
import random
import string

#16key-AES128# #24key-AES192# #32key-AES256#
##Gerando uma string de 32 bits para usar como chave da criptografia AES256
chave = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])

texto = "Um texto qualquer"

##Vetor de inicializacao que garante a randomicidade
IV  = Random.new().read(AES.block_size)

def encrypt(text):
	cifra  = AES.new(chave, AES.MODE_CFB, IV)
	return cifra.encrypt(text)

def decrypt(enc):
	cifra = AES.new(chave, AES.MODE_CFB, IV)
	texto = cifra.decrypt(enc)
	return texto.decode('utf-8')

texto_criptografado = encrypt(texto)
print ("Texto criptografado:")
print (texto_criptografado)

texto_decriptografado = decrypt(texto_criptografado)
print ("Texto decriptografado:")
print (texto_decriptografado)