import time

try:
    from raspythoncar.wr_lib2wd import WR2WD
except:
    from raspythoncar.em_lib2wd import WR2WD_emulator as WR2WD

wr = WR2WD()

i=0
wr.mc.front()
while( True ):

    if( i == 0 ):
        wr.led.off()
    elif( i == 1 ):
        wr.led.red()
    elif( i == 2 ):
        wr.led.blue()

    i = (i+1) % 2

    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        print( '\nbye')
        break

wr.led.off()
