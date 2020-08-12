# Purple Hand Cipher model N

class H5N:
    def keysetup(self, key, nonce):
        k = [0] * len(key)
        j = 0
        for c, byte in enumerate(key):
            k[c] = (k[c] + (ord(byte) - 65)) % 26
            j = (j + (ord(byte) - 65)) % 26
        for c, byte in enumerate(nonce):
            k[c] = (k[c] + (ord(byte) - 65)) % 26
        c = 0
        for r in range(256):
            j = k[j]
            k[j] = (k[j] + k[c]) % 26
            c = (c + 1) % 26
        return k, j

    def encrypt(self, chars, key, nonce):
        ctxt = []
        c = 0
        k, j = self.keysetup(key, nonce)
        for char in chars:
            j = k[j]
            k[j] = (k[j] + k[c]) % 26
            output = (k[j] + k[k[j]]) % 26
            sub = (output + (ord(char) - 65)) % 26
            ctxt.append(chr(sub + 65))
            c = (c + 1) % 26
        return "".join(ctxt)
    
    def decrypt(self, chars, key, nonce):
        ctxt = []
        c = 0
        k, j = self.keysetup(key, nonce)
        for char in chars:
            j = k[j]
            k[j] = (k[c] + k[j]) % 26
            output = (k[j] + k[k[j]]) % 26
            sub = ((ord(char) - 65) - output) % 26
            ctxt.append(chr(sub + 65))
            c = (c + 1) % 26
        return "".join(ctxt)

    def kdf(self, key, iterations=6666666):
        k = [0] * 26
        j = 0
        for c, byte in enumerate(key):
            k[c] = (k[c] + (ord(byte) - 65)) % 26
            j = (j + (ord(byte) - 65)) % 26
        c = 0
        for r in range(iterations):
            j = k[j]
            k[j] = (k[j] + k[c]) % 26
            c = (c + 1) % 26
        for x in range(len(k)):
            k[x] = chr(k[x] + 65)
        return "".join(k)
