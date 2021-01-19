from h5_instructional import H5
import sys, select, getpass, os, time, getopt

key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

msg = "ABC"

h5 = H5()

c = h5.encrypt(msg, key)
print("Ciphertext", c)

p = h5.decrypt(msg, key)
print("Plaintext", p)
