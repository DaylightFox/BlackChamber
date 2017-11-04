class rot():
    def __init__(self):
        self.abet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.out = ""
    def encrypt(self,txt,num):
        for i in txt:
            if i.isalpha() == False:
                self.out += i
            else:
                shift = self.abet.index(i.upper())+num
                while shift > 25:
                    shift -= 26
                self.out += self.abet[shift]
        return(self.out)
    def decrypt(self,txt,num):
        for i in txt:
            if i.isalpha() == False:
                self.out += i
            else:
                shift = self.abet.index(i.upper())-num
                while shift < 0:
                    shift += 26
                self.out += self.abet[shift]
        return(self.out)
