from encrypt.encrypt import encrypt_archive, decrypt_archive


def main():
    encrypt_archive('data/secret.txt')
    decrypt_archive('data/secret.txt')


if __name__ == "__main__":
    main()
