from encrypt import encrypt


def main():
    encrypt.load_key()
    encrypt.cyper()
    encrypt.decypher()


if __name__ == "__main__":
    main()
