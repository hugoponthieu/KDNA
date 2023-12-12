import kdnaFileConf
from kdnaFileConf import Server
from kdnaFileConf import Backup
from kdnaFileConf import Frequency


def main():
    kdnaFileConf.create()
    mon_serveur = Server("S1", "bplanche@10.163.53.40", 5432)
    mon_serveur2 = Server("S2", "bplanche@10.163.53.33", 5422)
    mon_serveur3 = Server("S3", "bplanche@10.163.53.40", 5432)
    mon_serveur4 = Server("S4", "bplanche@10.163.53.40", 5432)
    auto_backup = Backup("B1", Frequency.daily, "sauvegarde jounaliere", 43, mon_serveur.id_server)
    auto_backup2 = Backup("B2", Frequency.minute, "sauvegarde chaque heure", 23, mon_serveur4.id_server)
    auto_backup3 = Backup("B3", Frequency.hour, "sauvegarde chaque minute", 9, mon_serveur2.id_server)
    mon_serveur.add("serveur1")
    auto_backup.add("/tmp/backup/serveur/1/")
    kdnaFileConf.read()
    mon_serveur.delete()
    mon_serveur.add("serveur1")
    mon_serveur2.add("serveur2")
    auto_backup3.add("/tmp/backup/serveur/2/")
    mon_serveur3.add("serveur3")
    mon_serveur4.add("serveur4")
    mon_serveur3.delete()
    auto_backup2.add("/tmp/backup/serveur/4/")
    kdnaFileConf.read()


if __name__ == "__main__":
    main()
