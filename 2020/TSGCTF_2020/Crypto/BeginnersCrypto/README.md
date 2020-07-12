# Beginner's Crypto

![Challenge Description](BeginnersCrypto.png)

Let's checkout the contents of the given file [beginner.py](beginner.py).

```python
assert(len(open('flag.txt', 'rb').read()) <= 50)
assert(str(int.from_bytes(open('flag.txt', 'rb').read(), byteorder='big') << 10000).endswith('1002773875431658367671665822006771085816631054109509173556585546508965236428620487083647585179992085437922318783218149808537210712780660412301729655917441546549321914516504576'))
```

## Understanding the assertions

We are provided with 2 conditions which are satisfied by the flag string. We need to figure out a string which satisfies both of these conditions.

The first condition states that the string should be of length 50 or less.

The second condition seems interesting.

Let's simplify it by assigning the number encoded using the from_bytes function to a variable.
The condition is simplified to

```python
str(f << 10000).endswith('1002773875431658367671665822006771085816631054109509173556585546508965236428620487083647585179992085437922318783218149808537210712780660412301729655917441546549321914516504576')
```

'<<' is a bitwise operator in python. More information can be found [here](https://wiki.python.org/moin/BitwiseOperators).

$x$ << $y$ is same as $x$ * $2^y$

Let the number in the endswith condition be p.

```python
p = 1002773875431658367671665822006771085816631054109509173556585546508965236428620487083647585179992085437922318783218149808537210712780660412301729655917441546549321914516504576
```

Since $f$ << 10000 (i.e $f$ * $2^{10000}$) ends with p, that means the remainder obtained when dividing ($f$ << 10000) by $10^{175}$ should be equal to $p$(The divisor would be $10^{175}$ because $p$ is a 175 digit number).

Now lets represent this mathematically

$p$ $\equiv$ $f$ * $2^{10000}$ $\bmod$($10^{175}$)

But we cannot use modular inverse directly to find $f$ since $2^{10000}$ and $10^{175}$ are not relatively prime.

Lets convert this congruence into a linear equation.

$f$ * $2^{10000}$ = $x$ * $10^{175}$ + $p$

Let's try to prime factorise $p$ to see if that helps.

Upon querying factordb for the factorization of p, we get

```python
p = (2**175) * 61 * 343260582281778161791406870624564462499469137380445678942263498245279735080935957616380366178857319377077244490078139487
```

Assuming $y$ = $p$ // $2^{175}$,

$f$ * $2^{10000}$ = $x$ * $10^{175}$ + $2^{175}$ * $y$

This translates to $f$ * $2^{9825}$ = $x$ * $5^{175}$ + $y$

By converting this back into a congruence, we get $y$ $\equiv$ $f$ * $2^{9825}$ $\bmod$($5^{175}$)

=> $y$ * ($2^{9825}$)<sup>-1</sup> $\equiv$ $f$$\bmod$($5^{175}$)

We can find the modular inverse using gmpy2.

Solving this equation and decoding the integer using to_bytes function gives us the flag.

Here is the [script](crack.py) to crack this.

```python
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
```
