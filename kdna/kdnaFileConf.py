from enum import Enum


def read():
    with open('kdna.conf', 'r') as my_file:
        print(my_file.read())


def create():
    with open('kdna.conf', 'w') as my_file:
        my_file.write("[server]\n[auto-backup]\n")


def readLinesFiles():
    """
    Lit le fichier ligne par ligne et les ajoutes dans une liste
    :return: liste correspondant à chaque ligne du fichier de conf
    """
    with open('kdna.conf', 'r') as my_file:
        lines = my_file.readlines()
    return lines


def writeLinesFiles(lines):
    """
    Réécris le fichier ENTIEREMENT en utilisant la liste en paramète. Un argument de la liste pour une ligne
    :param lines: liste de chaque ligne de notre fichier de conf.
    """
    with open('kdna.conf', 'w') as my_file:
        my_file.writelines(lines)


class Entity:
    def delete(self):
        """
        Supprime la ligne du fichier de conf correspondant à cette element.
        """
        lines = readLinesFiles()
        lines = [line for line in lines if not line.startswith(f"{self}")]
        writeLinesFiles(lines)

    def add(self, name):
        pass

    def update(self, name):
        """
        Met à jour le nom la ligne du fichier de conf correspondant à cette element.
        :param name: L'alias qui sera donné à ce serveur
        """
        self.delete()
        self.add(name)

    def __str__(self):
        pass


class Server(Entity):
    def __init__(self, id_server, credentials, port):
        self.id_server = id_server
        self.credentials = credentials
        self.port = port

    def add(self, alias):
        """
        Ajoute une nouvelle ligne dans la partie [server] le fichier de conf.
        :param alias: L'alias qui sera donné à ce serveur
        :return: Toujours plus aussi
        """
        lines = readLinesFiles()
        lines.insert(1, f"{self}, {alias}\n")
        writeLinesFiles(lines)

    def __str__(self):
        return f"{self.id_server}, {self.credentials}, {self.port}"


class Frequency(Enum):
    minute = 1
    hour = 2
    daily = 3
    weekly = 4


class Backup(Entity):
    def __init__(self, id_backup, frequency: Frequency, name, timestamp, id_server):
        self.id_backup = id_backup
        self.frequency = frequency.name
        self.name = name
        self.timestamp = timestamp
        self.id_server = id_server

    def add(self, path):
        """
        Ajoute une nouvelle ligne dans la partie [auto-backup] le fichier de conf.
        :param path: Chemin absolu de destination de l'auto-backup
                    Valeur attendu : '/mon/repertoire/backup/'
        :return: Y'a pa wesh
        """
        lines = readLinesFiles()
        lines.append(f"{self}, {path}\n")
        writeLinesFiles(lines)

    def __str__(self):
        return f"{self.id_backup}, {self.frequency}, {self.name}, {self.timestamp}, {self.id_server}"
