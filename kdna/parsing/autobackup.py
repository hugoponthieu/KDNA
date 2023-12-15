class AutoBackup:
    '''Classe definissant un backup automatique
    id_backup: str
    frequency: int
    alias: str
    timestamp: int
    id_server: str
    path: str
      '''
    def __init__(self, id_backup: str,frequency: int, alias: str, timestamp: int, id_server: str, path: str  ):
        '''Constructeur de la classe'''
        self.id_backup = id_backup
        self.frequency = frequency
        self.alias = alias
        self.timestamp = timestamp
        self.id_server = id_server
        self.path = path


    def __str__(self):
        '''Methode d'affichage de la classe'''
        return f"AutoBackup: {self.id_backup} {self.frequency} {self.alias} {self.timestamp} {self.id_server} {self.path}"

class ParseAutoBackup:
    '''Classe permettant de parser un backup automatique
    line: str
    '''
    def __init__(self, line: str):
        '''Constructeur de la classe'''
        self.line = line

    def parse(self) -> AutoBackup:
        '''Methode permettant de parser un backup automatique'''
        values = self.line.strip().split(', ')
        id_backup, frequency, alias, timestamp, id_server, path = values
        return AutoBackup(id_backup, frequency, alias, timestamp, id_server, path)