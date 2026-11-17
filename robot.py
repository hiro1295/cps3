import os
from raspythoncar.wr_lib2wd import WR2WD

def read_all( wr ):
    pos = ['front', 'left', 'right', 'bottom']
    results = {}

    for p in pos:
        gpio.output(wr.ps.PIN_LED[p], 1)
    time.sleep(wr.ps.delay)

    for p in pos:
        results[p] = ( gpio.input(wr.ps.PIN_SENS[p]) == 0 )
        gpio.output(wr.ps.PIN_LED[pos], 0)

    return results

wr = WR2WD()


