from typing import List
import argparse
import json
import sys,os
import ui

with open(os.path.join(os.path.dirname((os.path.dirname(os.path.realpath(__file__)))),"data.json"),"r") as f:
    raw_json = f.read()
    SYSCALLS = json.loads(raw_json)

def main(argv : List[str])->None:
    # init parser
    parser = argparse.ArgumentParser(
                        prog='sysdoc',
                        description='fetch syscalls documentations',
                        epilog="Check 'https://man7.org/linux/man-pages/man2' to read more documentation")

    # add arguments
    parser.add_argument("syscall_proxy",help="display the syscall's documentation",type=str,nargs='?',default=None)
    parser.add_argument("-a","--arch",help="filters the syscalls by arch",type=str)
    parser.add_argument("-n","--name",help="filters the syscalls by name",type=str)
    parser.add_argument("-c","--code",help="filters the syscalls by code",type=str)

    # parse argv
    args = parser.parse_args(argv)

    if args.syscall_proxy != None:
        if args.syscall_proxy.isalpha():
            for syscall in SYSCALLS:
                if syscall["name"] == args.syscall_proxy:
                    print(ui.format_syscall(syscall))
        else:
            base = 16 if args.syscall_proxy[:2] == "0x" else 10
            syscall_proxy_int = int(args.syscall_proxy,base)
            for syscall in SYSCALLS:
                if syscall["nr"] == syscall_proxy_int:
                    print(ui.format_syscall(syscall))
    else:
        buffer = ""
        for syscall in SYSCALLS:
            filters = (not args.arch) or args.arch == syscall["arch"]
            filters = filters and ((not args.name) or args.name in syscall["name"])
            filters = filters and ((not args.code) or int(args.code) == syscall["nr"])
            if filters:
                buffer += ui.format_syscall(syscall) + "\n" + "-"*30 + "\n"
        print(buffer)

if __name__ == "__main__":
    main(sys.argv[1:])