import argparse
def main():
    parser = argparse.ArgumentParser(
        description="Sogit - A simple git clone tool"
    )
    subparsers= argparse.add_subparsers(
        dest="command",
        help="Available commands"
    )

    #init
    init_parser = subparsers.add_parser(
        "init",
        help="Initialize a new repository"
    )
main()