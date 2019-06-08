import hashlib
import string
import itertools
i = 0
prefix = "0e"
while 1:
	if i%1000000 == 0:
		 print prefix + str(i)
	hash1 = hashlib.new("md4", prefix + str(i)).hexdigest()
	if hash1[:2] == "0e" and  hash1[2:].isdigit():
		print prefix + str(i)
		print hash1
		exit()
	i += 1

