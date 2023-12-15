class Server:
    '''Classe definissant un serveur
    id_server: str
    credentials: str
    port: int
    alias: str
    '''
    def __init__(self, id_server: str, credentials: str, port: int, alias: str):
        '''Constructeur de la classe'''
        self.id_server = id_server
        self.credentials = credentials
        self.port = port
        self.alias = alias

    def __str__(self):
        '''Methode d'affichage de la classe'''
        return f"Server: {self.id_server} {self.credentials} {self.port} {self.alias}"


class ParseServer:
    '''Classe permettant de parser un serveur'''
    def __init__(self, line: str):
        '''Constructeur de la classe'''
        self.line = line

    def parse(self) -> Server:
        '''Methode permettant de parser un serveur'''
        id_server, credentials, port, alias = self.line.strip().split(', ')
        return Server(id_server, credentials, port, alias)