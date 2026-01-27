import argparse
import sys
def main():
    parser = argparse.ArgumentParser(
        description="Sogit - A simple git clone tool"
    )
    subparsers= parser.add_subparsers(
        dest="command",
        help="Available commands"
    )

    #init
    init_parser = subparsers.add_parser(
        "init",
        help="Initialize a new repository"
    )
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return
    try:
        pass
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

main()