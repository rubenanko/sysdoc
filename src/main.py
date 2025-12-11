from typing import List
import argparse
import json
import sys
import ui

with open("data.json","r") as f:
    raw_json = f.read()
    SYSCALLS = json.loads(raw_json)

def main(argv : List[str])->None:
    # init parser
    parser = argparse.ArgumentParser(
                        prog='sysdoc',
                        description='fetch syscalls documentations',
                        epilog="See 'omg --sysdoc' to get further help")

    # add arguments
    parser.add_argument("syscall_proxy",help="display the syscall's documentation",type=str,nargs='?',default=None)
    parser.add_argument("-a","--arch",help="filters the syscalls by arch",type=str)
    parser.add_argument("-n","--name",help="filters the syscalls by name",type=str)
    parser.add_argument("-d","--decimal",help="filters the syscalls by code, in a decimal format",action="store_true")
    parser.add_argument("-x","--hex",help="filters the syscalls by code, in a hexadecimal format",action="store_true")

    # parse argv
    args = parser.parse_args(argv)

    if args.syscall_proxy != None:
        if args.syscall_proxy.isalpha():
            for syscall in SYSCALLS:
                if syscall["name"] == args.syscall_proxy:
                    print(syscall)
        else:
            
    else:


if __name__ == "__main__":
    main(sys.argv[1:])