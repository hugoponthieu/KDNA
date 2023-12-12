#!/usr/bin/env python3

# Necessite pip install fabric
# Tout ce qui est dessous fonctionne

# note : Fabric has facilities for loading SSH config files
# melomys est une machine dont la config ssh est définie dans mon .ssh/config :
# Host melomys
# Hostname 162.38.111.241 
# User user_sur_melomys

from fabric import Connection
from dotenv import load_dotenv
import os

load_dotenv()
host = os.getenv('HOST')

# Lancer une commande à distance et récupérer son résultat :
result = Connection(host).run('tree', hide=True)
msg = "\n{0.stdout}"
print(msg.format(result))

# Lancer une commande sans s'intéresser à son résutlat :
#with Connection('melomys') as c:
#	c.run('touch tmp/test_from_fabric')
# la connexion est automatiquement fermée avec cette syntaxe du "with"

# Copier des fichiers sur une machine distante : 
#with Connection('melomys') as c:
#	c.put('file_sent_by_fabric.txt',remote='tmp/')
# la connexion est automatiquement fermée avec cette syntaxe du "with"

def print_tag_from_project(project):
    """
    Print tous les tags lié au projet.

    Arguments: projet (str) 
    """
    try:
        result = Connection(host).run(f'cd {project} && ls -dl */', hide=True)
        msg = "\n{0.stdout}"
        print(msg.format(result))
    except:
        print("An error as occured")
        return None

def print_tag_content(project, tag):
    """
    Print le contenu d'un tag d'un projet.

    Arguments: projet (str), tag (str) 
    """
    try:
        result = Connection(host).run(f'cd {project}/{tag} && ls -l', hide=True)
        msg = "\n{0.stdout}"
        print(msg.format(result))
    except:
        print("An error as occured")
        return None

def print_projects():
    """
    Print tous les projets.

    Arguments: none
    """
    result = Connection(host).run('ls -dl */', hide=True)
    msg = "\n{0.stdout}"
    print(msg.format(result))

print("---------------Projets-----------------")
print_projects()

print("---------------Tags-----------------")
print_tag_from_project("test")

print("---------------Zips-----------------")
print_tag_content("test", "v0.0.1")