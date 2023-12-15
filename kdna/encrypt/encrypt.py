"""
This module contains encryption functions.

:author: RADULESCU Tristan-Mihai, TCHILINGUIRIAN Théo
:email: <placeholder>, theo.tchlx@gmail.com
:date: 2023-12-15
"""


import os
from cryptography.fernet import Fernet
from auxtools import auxtools


def generate_key():
    key = Fernet.generate_key()
    file = open('key.key', 'wb')
    file.write(key)
    file.close()


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


def cypher(path: str, out: str) -> bytes:
    """
    :param path: path to file to encrypt
    :param out: path to output file
    """
    key = load_key()
    fer = Fernet(key)
    with open(path, "rb") as f_in, open(out, "w") as f_out:
        data = f_in.read()

        encrypted = fer.encrypt(data)
        print(encrypted)
        
        f_out.write(encrypted.decode())
    return encrypted


def cypher_folder(path: str, out: str):
    print(os.listdir(path))
    for file in os.listdir(path):
        cypher(path + "/" + file, out + "/" + file)


def decypher_folder(path: str, out: str):
    print(os.listdir(path))
    for file in os.listdir(path):
        decypher(path + "/" + file, out + "/" + file)


def decypher(path: str, out: str):
    """
    :param path: path to file to decrypt
    :param out: path to output file
    """
    key = load_key()
    fer = Fernet(key)
    with open(path, "r") as f_in, open(out, "wb") as f_out:
        data = f_in.read()
        decrypted = fer.decrypt(data.encode())
        f_out.write(decrypted)
