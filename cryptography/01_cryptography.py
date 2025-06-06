from cryptography.fernet import Fernet
key=Fernet.generate_key()
print("generated key",key)


cipher=Fernet(key)
#encrypyt
msg="secret msg".encode()
encrypted=cipher.encrypt(msg)

#decrypt
decrypted=cipher.decrypt(encrypted)
print(decrypted.decode())
