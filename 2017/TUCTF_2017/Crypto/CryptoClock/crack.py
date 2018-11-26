import random
import arrow
import sys
def prin(st):
    sys.stdout.write(st)
from pwn import *
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
N = 142592923782837889588057810280074407737423643916040668869726059762141765501708356840348112967723017380491537652089235085114921790608646587431612689308433796755742900776477504777927984318043841155548537514797656674327871309567995961808817111092091178333559727506289043092271411929507972666960139142195351097141
big_1=44125640252420890531874960299151489144331823129767199713521591380666658119888039423611193245874268914543544757701212460841500066756559202618153643704131510144412854121922874915334989288095965983299150884589072558175944926880089918837606946144787884895502736057098445881755704071137014578861355153558L
big_2=66696868460135246134548422790675846019514082280010222055190431834695902320690870624800896599876321653748703472303898494328735060007496463688173184134683195070014971393479052888965363156438222430598115999221042866547813179681064777805881205219874282594291769479529691352248899548787766385840180279125343043041L

r = remote("cryptoclock.tuctf.com",1230)
print r.recv(200)
r.sendline("1")
prin(r.recvline())
prin(r.recvline())
enctimestamp = int(r.recvline())
origtimestamp = arrow.utcnow().timestamp
print enctimestamp
enctimestamp1 = enctimestamp
while enctimestamp1 == enctimestamp:
    print r.recv(200)
    r.sendline("1")
    prin(r.recvline())
    prin(r.recvline())
    origtimestamp1 = arrow.utcnow().timestamp
    enctimestamp1 = int(r.recvline())
    print enctimestamp1
print (origtimestamp1 - origtimestamp)
assert (origtimestamp1 - origtimestamp) == 1
c1 = enctimestamp
c2 = enctimestamp1
nume = (c2 + 2*c1 - 1) % N
deno = (c2 - c1 + 2) % N
tsplusoffset = (nume * modinv(deno,N)) % N
offset = tsplusoffset - origtimestamp
print offset
prin(r.recv(200))
r.sendline("2")
prin(r.recv(200))
time = arrow.utcnow().timestamp + offset
random.seed(time)
guessing_int = random.randint(0,999999999999)
r.sendline(str(guessing_int))
print r.recv(300)
