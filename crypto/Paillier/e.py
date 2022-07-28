from pwn import *

io = remote("207.180.197.198", 1338)
_, _, n = io.recvline().decode().strip().partition("= ")
encflag = int(io.recvlines(2)[1].decode().strip(), 16)

n = int(n)

print(f"n = {n}")
print(f"eflag = {encflag}")

tosend = encflag * pow(n+1, 2, n**2)


io.sendlineafter(b"Option:", b"B")
io.sendlineafter(b"Ciphertext:", b"0" * (len(hex(tosend)) % 2) + hex(tosend)[2:].encode())

flag = int(io.recvline().decode().strip(), 16)-2

print(bytes.fromhex(hex(flag)[2:]))
