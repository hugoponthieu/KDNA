from encrypt import encrypt


def main():
    encrypt.cypher_folder("./data", "./out")
    encrypt.decypher_folder("./out", "./out_cypher")


if __name__ == "__main__":
    main()
