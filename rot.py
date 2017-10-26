def rot(num,txt):
    abet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = ""
    for i in txt:
        if i == " ":
            out += " "
        else:
            shift = abet.index(i)+num
            while shift > 25:
                shift -= 26
            out += abet[shift]
    return(out)
