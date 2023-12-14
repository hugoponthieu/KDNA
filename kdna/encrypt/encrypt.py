from cryptography.fernet import Fernet
import os


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
    with open(path, "rb") as f:
        data = f.read()

    encrypted = fer.encrypt(data)
    print(encrypted)
    with open(out, "w") as f:
        f.write(encrypted.decode())
    return encrypted


def walk_path(path: str):
    """
        Description: this function walks through the subdirectories from the given path and outputs a list of paths to every subdirectory (including the given path), every subdirectories and every files with full paths.
        Inputs:
            path: string
        Outputs:
            full_filenames : list ; a list of strings, full paths (from the given path) to each file in every subdirectory (including the directory from the given path).
    """
    dirpath, dirnames, filenames = [], [], []
    for triplet in os.walk(path):
        dirpath.append(triplet[0])
        dirnames.append(triplet[1])
        filenames.append(triplet[2])
    
    full_filenames = list()
    for i in range(len(dirpath)):
        for j in range(len(filenames[i])):
            full_filenames.append(os.path.join(dirpath[i], filenames[i][j]))
    
    return full_filenames



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
    with open(path, "r") as f:
        data = f.read()
    decrypted = fer.decrypt(data.encode())
    with open(out, "wb") as f:
        f.write(decrypted)
