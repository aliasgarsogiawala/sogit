import argparse
import sys
from pathlib import Path
import json

class Repository:
    def __init__(self, path="."):
        self.path = Path(path).resolve() #git init
        self.git_dir = self.path / ".sogit"
        #.git/objects
        self.objects_dir= self.git_dir / "objects"
        # .git/refs
        self.ref_dir= self.git_dir / "refs"
        self.heads_dir= self.ref_dir / "refs"
        #HEAD FIle
        self.head_file= self.git_dir/"HEAD"

        #.git/index
        self.index_file= self.git_dir / "index"
    def init(self) -> bool:

        #create directories
        self.git_dir.mkdir()
        self.objects_dir.mkdir()
        self.ref_dir.mkdir()

        #HEAD file pointing to a default branch
        self.heads_dir.mkdir()
        self.head_file.write_text("ref: refs/heads/main\n")
        self.index_file.write_text(json.dumps({},indent=2))
        print(f"Initialised empty repository in {self.path}")



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
    add_parser = subparsers.add_parser(
        "add",
        help="Add files to the repository"
    )
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return
    try:
        if args.command == "init":
            pass
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

main()