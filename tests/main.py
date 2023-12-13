import os
from kdna.encrypt import encrypt


def gen_file_structure_bin(nb_files: int = 10):
    os.chdir("tests/data")
    os.mkdir("test")
    os.mkdir("test_encrypted")
    os.mkdir("test_decrypted")
    for k in range(0, nb_files):
        with open(f"test/test{k}.txt", "w") as test_file:
            test_file.write(f"Hello World : {k}!")
    os.chdir("../../")


def delete_file_structure(nb_files: int = 10):
    os.chdir("tests/data")
    for k in range(0, nb_files):
        os.remove(f"test/test{k}.txt")
    for k in range(0, nb_files):
        os.remove(f"test_encrypted/test{k}.txt")
    for k in range(0, nb_files):
        os.remove(f"test_decrypted/test{k}.txt")
    os.rmdir("test")
    os.rmdir("test_encrypted")
    os.rmdir("test_decrypted")


def test_encryption_folder():
    gen_file_structure_bin()
    encrypt.cypher_folder("tests/data/test", "tests/data/test_encrypted")
    encrypt.decypher_folder("tests/data/test_encrypted",
                            "tests/data/test_decrypted")
    delete_file_structure()
