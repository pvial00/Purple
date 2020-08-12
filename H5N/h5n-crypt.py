from h5n import H5N
import sys, select, getpass, os, time, getopt

try:
    mode = sys.argv[1]
except IndexError as ier:
    print("Error: Did you forget encrypt/decrypt?")
    sys.exit(1)

input_filename = sys.argv[2]
output_filename = sys.argv[3]

try:
    infile = open(input_filename, "r")
except IOError as ier:
    print("Input file not found.")
    sys.exit(1)

try:
    outfile = open(output_filename, "w")
except IOError as ier:
    print("Output file not found.")
    sys.exit(1)

try:
    key = sys.argv[4]
except IndexError as ier:
    key = getpass.getpass("Enter key: ")

try:
    nonce = sys.argv[5]
except IndexError as ier:
    nonce = input("Enter nonce: ")

h5n = H5N()
key = h5n.kdf(key)
print(key)

start = time.time()
data = infile.read()
infile.close()

if mode == "encrypt":
    c = h5n.encrypt(data, key, nonce)
    outfile.write(c)
elif mode == "decrypt":
    plain_text = h5n.decrypt(data, key, nonce)
    outfile.write(plain_text)
outfile.close()

end = time.time() - start
bps = len(data) / end
sys.stdout.write("Completed in "+str(end)+" seconds\n")
sys.stdout.write(str(bps)+" bytes per second.\n")
