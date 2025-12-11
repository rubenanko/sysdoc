
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

def format_syscall(syscall):
    header = f'arch\tNR\tname\t{REGISTERS[syscall["arch"]]["code"]}\n'

    args = ""
    i = 0
    while i < 6 and syscall[f"arg{i}"] != "":
        args += "\n" + REGISTERS[syscall["arch"]][f"arg{i}"] + "\t" + syscall[f"arg{i}"]
        i += 1

    return f'{header}{syscall["arch"]}\t{syscall["nr"]}\t{syscall["name"]}\t{hex(syscall["nr"])}\n{args}'