from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(4096, random_generator)

public_key = key.publickey()

enc_data = public_key.encrypt(b'Um texto qualquer', 32)
print ("Texto criptografado:")
print (enc_data)

dec_data = key.decrypt(enc_data)
print ("Texto decriptografado:")
print (dec_data.decode('utf-8'))


