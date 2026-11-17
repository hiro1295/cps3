import time

try:
    from raspythoncar.wr_lib2wd import WR2WD
except:
    from raspythoncar.em_lib2wd import WR2WD_emulator as WR2WD

wr = WR2WD()

velocity = 13.15 # cm/s
wr.led.red()

#wr.mc.turn_right()
while True:
    print(wr.ps.front())

    #if wr.ps.front():
        #break
#print(f'left: {wr.ps.left()}')
    time.sleep(0.1)
    #continue
    #if wr.ps.left():
    #    wr.mc.front_tr()
    #elif wr.ps.right():
    #    wr.mc.front_tl()
    #else:
    #    wr.mc.front()

wr.mc.brake()
wr.led.off()
