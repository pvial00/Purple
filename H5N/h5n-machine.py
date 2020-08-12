from h5n import H5N
import sys, select, getpass, os, time, getopt

h5n = H5N()

mode = sys.argv[1]

text = input("Enter message: ")
key = input("Enter key: ")
nonce = input("Enter nonce: ")

if mode == "e":
    c = h5n.encrypt(text, key, nonce)
    print(c)
elif mode == "d":
    c = h5n.decrypt(text, key, nonce)
    print(c)
