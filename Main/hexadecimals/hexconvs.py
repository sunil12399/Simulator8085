from Main.Objects import flags
def int2hex(n):
    if n<10:
        return str(n)
    else:
        val={
            10:"A",
            11:"B",
            12:"C",
            13:"D",
            14:"E",
            15:"F"
            }
        return val.get(n)


def hex2int(n):
    num, k = 0, 0

    for x in n:
        if x.isdigit():
            if int(x) < 10:
                p = int(x)
        else:
            val = {
                    "A": 10,
                    "B": 11,
                    "C": 12,
                    "D": 13,
                    "E": 14,
                    "F": 15
                    }
            p = val.get(x)
        num = num * pow(16, k) + p
        k += 1
    return num


def int2hexstr(n):
    if n < 16:
        #print(str1)
        return str(0)+int2hex(n)
    else:
        str1 = hex(n)
        l = len(str1)
        str1 = str1[l-2:]
        return str1.upper()

