# Cybersecurity Encrypter Program
import time
import random

def Encrypter(decrypted_txt, password):
    while password != 1000011:
        int(input("\nAccess denied. Enter again: "))
    print("\nAccess granted. Encrypting", end="")
    time.sleep(1)
    for i in range (1, 6):
        print(".", end="")
        time.sleep(1)
    encrypted_txt = ""
    for j in range (1, len(decrypted_txt) + 1):
        encrypted_txt = encrypted_txt + random.choice(['*', '%', '$', '#'])
    print("\n\n=========================================")
    print(f"ENCRYPTED STRING: {encrypted_txt}")
    print("=========================================")

print("=====ENCRYPTER=====")
decrypted = input("\nEnter decrypted text: ")
assert decrypted != " ", "ERROR, DECRYPTED TEXT CANNOT BE EMPTY."
password = int(input("\nEnter binary password for encryption: "))
Encrypter(decrypted, password)