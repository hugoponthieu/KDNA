"""Main entry point for kdna"""

from Backup import Backup
from Server import Server
from ConfUtils import ConfUtils


def main():
    """Main"""
    # ConfUtils.initialize_config_file()

    # server = Server("18", "credentials", "22", "hello")
    # server.add()

    # backup = Backup("9", "monthly", "okay", "2021-01-01","18", "/home/backup")
    # backup.add()
    
    # Server.update("hello", new_port="25", new_credentials="newcredentials", new_alias="test")
    
    # Backup.update("9", new_frequency="daily", new_timestamp="2021-01-02", new_path="/home/backup/first")

    # Backup.delete("9")

    # Server.delete("18")
    
    # server = Server("18", "credentials", "22", "hello")
    # server.add()
    
    # Server.delete("hello", by_alias=True)

    # ConfUtils.readAll()


if __name__ == "__main__":
    main()
