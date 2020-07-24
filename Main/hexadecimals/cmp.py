from Main.hexadecimals import hexconvs
from Main.Objects import flags


class comp:
    def hexcmp(self,acc,regm):
        v = hexconvs.hex2int(acc.reg)
        v1 = hexconvs.hex2int(regm.reg)
        if v > v1:
            flags.flag['CY'] = 0
            flags.flag['Z'] = 0
        elif v == v1:
            flags.flag['CY'] = 0
            flags.flag['Z'] = 1
        else:
            flags.flag['CY'] = 1
            flags.flag['Z'] = 0
        return
