from Crypto.Cipher import AES
from pwn import *

def get_padding_byte(r):
    for padding_byte in range(0x20, 0x7E):
        print padding_byte
        r.recvline()
        r.sendline("}" + chr(padding_byte) * 32)
        r.recvline()
        enc = r.recvline()
        print enc
        print enc[0:64]
        print enc[128:192]
        if(enc[:64] == enc[128:192]):
            print "FOUND PADDING BYTE " + chr(padding_byte)
            return chr(padding_byte)


r = remote("18.218.238.95",12345)

r.recv(1000)

r.sendline("}")

r.recvline()
r.recvline()

flaglen = 32
keylen = 32
flag = "}"

padding_byte = get_padding_byte(r)

for i in range(31):
    for flag_char in range(0x20, 0x7E):
        print flag_char
        testflag = chr(flag_char) + flag
        r.recvline()
        r.sendline(testflag + (padding_byte) * (32))
        r.recvline()
        enc = r.recvline()
        #print enc
        if(enc[:64] == enc[128:192]):
            print "FOUND FLAG BYTE " + chr(flag_char)
            flag = chr(flag_char)+ flag
            break

print flag

r.close()
