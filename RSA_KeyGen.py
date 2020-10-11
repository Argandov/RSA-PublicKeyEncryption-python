from Crypto.PublicKey import RSA

# Generating and writing a public Key to a file:
key = RSA.generate(2048)
f = open('mykey.pem','wb')
f.write(key.export_key('PEM'))
f.close()
f = open('mykey.pem','r')
key = RSA.import_key(f.read())
