# Purple Hand Cipher (Instructional)

class H5:
    def keysetup(self, key):
        k = [0] * len(key)
        j = 0
        for c, byte in enumerate(key):
            k[c] = (k[c] + (ord(byte) - 65)) % 26
            j = (j + (ord(byte) - 65)) % 26
        return k, j

    def encrypt(self, chars, key):
        ctxt = []
        c = 0
        k, j = self.keysetup(key)
        for char in chars:
            j = k[j]
            print(j)
            print(k[c], k[j])
            k[j] = (k[j] + k[c]) % 26
            print(k[j])
            print(k[j], k[k[j]])
            output = (k[j] + k[k[j]]) % 26
            print(output)
            sub = (output + (ord(char) - 65)) % 26
            print(output, (ord(char) - 65))
            print(sub)
            print(k)
            ctxt.append(chr(sub + 65))
            c = (c + 1) % 26
        return "".join(ctxt)
    
    def decrypt(self, chars, key):
        ctxt = []
        c = 0
        k, j = self.keysetup(key)
        for char in chars:
            j = k[j]
            print(j)
            print(k[c], k[j])
            k[j] = (k[c] + k[j]) % 26
            print(k[j], k[k[j]])
            output = (k[j] + k[k[j]]) % 26
            print(output)
            sub = ((ord(char) - 65) - output) % 26
            print(output, (ord(char) - 65))
            print(sub)
            print(k)
            ctxt.append(chr(sub + 65))
            c = (c + 1) % 26
        return "".join(ctxt)
