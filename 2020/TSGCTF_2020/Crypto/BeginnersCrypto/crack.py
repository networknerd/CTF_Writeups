from gmpy2 import invert

n = pow(5,175)

p = 1002773875431658367671665822006771085816631054109509173556585546508965236428620487083647585179992085437922318783218149808537210712780660412301729655917441546549321914516504576

y = p // pow(2,175)

assert y * pow(2,175) == p

k = pow(2, 9825, n)

kinv = int(invert(k, n))

f = (y * kinv) % n

matcher = "5453474354467b"
if matcher in hex(f):
    print("Found: ", hex(f))
    print("Flag: ", str(f.to_bytes(50, byteorder='big')))