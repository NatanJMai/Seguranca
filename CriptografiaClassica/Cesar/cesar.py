def encrypt(text, key):
	t = ""
	for i in range(0, len(texto)):
		t += chr((ord(text[i])+key)%256)
	return t

def decrypt(text, key):
	t = ""
	for i in range(0, len(texto)):
		t += chr((ord(text[i])-key)%256)
	return t

chave = 7

texto = "Um texto qualquer"

texto_cript = encrypt(texto, chave)
print ("Texto criptografado:")
print (texto_cript)

testo_decript = decrypt(texto_cript, chave)
print ("Texto decriptografado:")
print (testo_decript)