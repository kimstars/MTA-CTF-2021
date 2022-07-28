from pwn import *
r = process("./ez_solve")

while(1):
    r.recvuntil("Guess a number:\n")
    p = process("./guess")
    guess = p.recv()
    print(guess)
    r.send(guess)
    sleep(1)
    print (r.recvline())

r.interactive()