
REGISTERS = {
    "x64" : {
                "code": "RAX",
                "arg0": "RDI",
                "arg1": "RSI",
                "arg2": "RDX",
                "arg3": "R10",
                "arg4": "R8",
                "arg5": "R9",
            }
}

# REGISTERS_COLOR_CODES = [208,172,136,100,64,28]
REGISTERS_COLOR_CODES = [202,166,220,100,64,28]

def format_syscall(syscall):
    header = f'\x1b[0;35march\x1b[0;0m\t\x1b[0;37mNR\x1b[0;0m\t\x1b[0;34mname\x1b[0;0m\n'

    args = f'\x1b[1;31m{REGISTERS[syscall["arch"]]["code"]}\x1b[0;0m\t\x1b[1;31m{hex(syscall["nr"])}'
    i = 0
    while i < 6 and syscall[f"arg{i}"] != "":
        argument = syscall[f"arg{i}"].split(" ")
        argument[0] = "\x1b[0;0m" + argument[0]
        argument[-1] = "\x1b[0;0m\x1b[1;37m" + argument[-1] + "\x1b[0;0m"
        args += f"\n\x1b[38;5;{REGISTERS_COLOR_CODES[i]}m" + REGISTERS[syscall["arch"]][f"arg{i}"] + "\x1b[0;0m\t" + " ".join(argument)
        i += 1

    if syscall["arch"] == "x64":
        link = f'\n\nhttps://man7.org/linux/man-pages/man2/{syscall["name"]}.2.html'

    return f'{header}\x1b[1;35m{syscall["arch"]}\x1b[0;0m\t\x1b[1;37m{syscall["nr"]}\x1b[0;0m\t\x1b[1;34m{syscall["name"]}\x1b[0;0m\n\n{args}{link}'