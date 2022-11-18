from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64
import os

def encryptFile(og_file,pub_key):
    with open(pub_key, "rb") as key_file:

        public_key = serialization.load_pem_public_key(

            key_file.read()

        )

    if not os.path.isfile(og_file):
        print("File does not exist")
        exit(2)

    f = open(og_file,'r')

    message = f.read().encode('utf-8')

    f.close()

    ciphertext = public_key.encrypt(

        message,

        padding.PKCS1v15()

    )

    return base64.b64encode(ciphertext)



def encryptString(str,pub_key):
    with open(pub_key, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read()
        )
    message = str.encode('utf-8')
    ciphertext = public_key.encrypt(
        message,
        padding.PKCS1v15()
    )
    return base64.b64encode(ciphertext)


def decryptFile(og_file, pw, priv_key):

    with open(priv_key, "rb") as key_file:

        private_key = serialization.load_pem_private_key(

            key_file.read(),

            password=base64.b64decode(pw),

        )

    if not os.path.isfile(og_file):
        print("File does not exist")
        exit(2)

    f = open(og_file,'rb')
    ciphertext = base64.b64decode(f.read())

    plaintext = private_key.decrypt(

        ciphertext,

        padding.PKCS1v15()

        )

    txt = plaintext.decode('utf-8')

    return txt


def decryptBytes(str, password, priv_key):

    with open(priv_key, "rb") as key_file:

        private_key = serialization.load_pem_private_key(

            key_file.read(),

            password=base64.b64decode(password+password+password+password),

        )

    ciphertext = base64.b64decode(str)

    plaintext = private_key.decrypt(

        ciphertext,

        padding.PKCS1v15()

        )

    txt = plaintext.decode('utf-8')

    return txt

def generateKeys(password,output_file):
    if os.path.exists("cryptoKeys/" + output_file + "_privK.pem") != True:
        print("GENERATING KEYS")
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(base64.b64decode(password+password+password+password))
        )
        privK = "cryptoKeys/" + output_file + "_privK.pem"
        f = open(privK, "wb")
        f.write(pem)
        f.close()
        public_key = private_key.public_key()
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        pubK = "cryptoKeys/" + output_file + "_pubK.pem"
        f = open(pubK, "wb")
        f.write(pem)
        f.close()