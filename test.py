import time

try:
    from raspythoncar.wr_lib2wd import WR2WD
except:
    from raspythoncar.em_lib2wd import WR2WD_emulator as WR2WD

wr = WR2WD()

velocity = 13.15 # cm/s
wr.led.red()
wr.mc.front()

time.sleep(55/velocity)

wr.led.green()
wr.mc.turn_right()
time.sleep(0.7)
wr.mc.front()
time.sleep(15/velocity)
#wr.mc.brake()

wr.led.blue()
while True:
    #print(wr.ps.right())
    #print(f'left: {wr.ps.left()}')
    time.sleep(0.005)

    if wr.ps.left() and wr.ps.right():
        wr.mc.front()
    elif wr.ps.left():
        wr.mc.front_tr()
    elif wr.ps.right():
        wr.mc.front_tl()
    else:
        wr.mc.front()
    if not wr.ps.bottom():
        break

wr.led.green()
wr.mc.front_tr()
time.sleep(0.5)
wr.led.red()
wr.mc.front()
time.sleep(1)
wr.led.blue()
wr.mc.turn_right()
while True:
    time.sleep(0.001)
    if wr.ps.front():
        break
wr.led.red()
wr.mc.front()
time.sleep(0.9)
wr.led.green()
wr.mc.turn_right()
time.sleep(1)
wr.led.red()
wr.mc.front()
time.sleep(3.1)

wr.mc.brake()
wr.led.off()
