from pwn import *
import string
charset = "?" + string.digits + string.letters + "{}_"
r = remote("crypto.hsctf.com", 8111)

st = r.recvline_contains("super secret message")
encflag = st.split(" ")[6]
print encflag
r.sendline()
#flag = "hsctf{h0w_d3d_y3u_de3cryP4_th3_s1p3R_s3cuR3_m355a9e}"
flag = ""
while flag[-1:] != "}":
    for i in charset:
        print r.recvline_contains("encrypt:")
        r.sendline(flag + i)
        print flag + i
        r.recvline_contains("Encrypted")
        s = r.recvline_contains("Encrypted")
        r.sendline()
        print s
        encflag1 = s.split(" ")[1]
        if encflag1 == encflag[:len(encflag1)]:
            flag = flag + i
            break
    print flag
r.close()
