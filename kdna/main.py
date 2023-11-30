from Backup import Backup
from Server import Server
from ConfUtils import ConfUtils


def main():
    ConfUtils.initialize_config_file()

    backup = Backup("9", "monthly", "okay", "2021-01-01", "3", "/home/backup")
    backup.add()

    server = Server("18", "credentials", "22", "hello")
    server.add()

    Backup.delete("9")
    Backup.delete("2")

    Server.delete("4")
    Server.delete("alisas", by_alias=True)

    Server.update("test", new_port="25",
                  new_credentials="test", new_alias="ahahah")
    Backup.update("5", new_frequency="daily",
                  new_timestamp="2021-01-02", new_path="/home/backup")

    ConfUtils.readAll()


if __name__ == "__main__":
    main()
