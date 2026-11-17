import time

try:
    from raspythoncar.wr_lib2wd import WR2WD
except:
    from raspythoncar.em_lib2wd import WR2WD_emulator as WR2WD

wr = WR2WD()

velocity = 13.15 # cm/swr.led.red()

wr.mc.front()
while True:
    print(wr.ps.bottom())
    if not wr.ps.bottom():
        break
#print(f'left: {wr.ps.left()}')
    time.sleep(0.1)
    
wr.mc.brake()
wr.led.off()
