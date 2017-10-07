class vigenere():
    # Uses equations from the Wikipedia entry
    def __init__(self):
        self.abet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def encrypt(self,key,txt):
        key = key*(int(len(txt)/len(key)))+key[:len(txt)%len(key)]
        out = ""
        for i in range(len(txt)):
            val = self.abet.index(txt[i].upper()) + self.abet.index(key[i].upper())
            while val > len(self.abet):
                val -= 26
            out += self.abet[val]
        return(out)
    def decrypt(self,key,txt):
        key = key*(int(len(txt)/len(key)))+key[:len(txt)%len(key)]
        out = ""
        for i in range(len(txt)):
            val = self.abet.index(txt[i].upper()) - self.abet.index(key[i].upper())
            while val < 0:
                val += 26
            out += self.abet[val]
        return(out)
