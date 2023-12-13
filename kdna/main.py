"""Main entry point for kdna"""""
from kdna.read_backups import agent


def main():
    """Main entry point for kdna"""""
    print("Hello DO")
    print("---------------Projets-----------------")
    agent.print_projects()

    print("---------------Tags-----------------")
    agent.print_tags_from_project("test")

    print("---------------Zips-----------------")
    agent.print_tag_content("test", "v0.0.1")



if __name__ == '__main__':
    main()

