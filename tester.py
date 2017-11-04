from vigenere import vigenere
from rot import rot

def main():
    choice = int(input("===== Choose module to test =====\n\
1. Vignere Cipher\n\
2. Rot Cipher\n\
9. Quit\n\
Choice (1-9): "))
    if choice == 1:
        msg = str(input("Message: "))
        key = str(input("Key: "))
        v = vigenere().encrypt(msg,key)
        print("Ecnrypted text: {}".format(v))
        print("Decrypted text: {}".format(vigenere().decrypt(v,key)))
        main()
    elif choice == 2:
        msg = str(input("Message: "))
        key = int(input("Key: "))
        r = rot().encrypt(msg,key)
        print("Ecnrypted text: {}".format(r))
        print("Decrypted text: {}".format(rot().decrypt(r,key)))
        main()
    elif choice == 9:
        exit()
    else:
        print("Invalid choice")
        main()
main()
