from cryptography.fernet import Fernet 
key = Fernet.generate_key()
fernet = Fernet(key)
passwd = "HASsan@4r"
encMessage = fernet.encrypt(passwd.encode())
print("original string: ", passwd)
print("encrypted string: ", encMessage)
decMessage = fernet.decrypt(encMessage).decode()
print("decrypted string: ", decMessage)