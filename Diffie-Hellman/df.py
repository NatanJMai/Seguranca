from random import randint

primoComum = 101
baseComum = 3

aSecreto = randint(0,100)
bSecreto = randint(0,100)

aEnvia = ((baseComum**aSecreto)%primoComum)
print ("Chave enviada de a para b por um caminho nao seguro:")
print (aEnvia)

bEnvia = ((baseComum**bSecreto)%primoComum)
print ("Chave enviada de b para a por um caminho nao seguro:")
print (bEnvia)

print("#--------------------------------------------------#")

aRecebe = ((bEnvia**aSecreto)%primoComum)
print ("Chave secreta compartilhada calculada em a:")
print (aRecebe)

bRecebe = ((aEnvia**bSecreto)%primoComum)
print ("Chave secreta compartilhada calculada em b:")
print (bRecebe)