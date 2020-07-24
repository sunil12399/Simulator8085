flag = {
    'S': 0,
    'Z': 0,
    'D5': 0,
    'AC': 0,
    'D3': 0,
    'P': 0,
    'D1': 0,
    'CY': 0
}


def setFlags(object):
    value_a = int(str(object), 16)
    bin_a = bin(value_a)[2:].zfill(8)

    if object.reg == '00':
        flag['Z'] = 1
    else:
        flag['Z'] = 0

    if bin_a[0] == '1':
        flag['S'] = 1
    else:
        flag['S'] = 0

    flag['P'] = 1 if(list(bin_a).count('1') % 2 == 0) else 0
