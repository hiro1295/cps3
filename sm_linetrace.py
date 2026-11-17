import time
import argparse

try:
    from raspythoncar.wr_lib2wd import WR2WD
except:
    pass

from raspythoncar.em_lib2wd import WR2WD_emulator, Field
from WDT import PerfTimer

from transitions import Machine

# https://github.com/pytransitions/transitions
###### EDIT HERE #################################
class robot:
    def __init__(self, wr):
        self.wr = wr
        self.watch_dog = PerfTimer()

        states = ['READY', 'WHITE', 'BLACK', 'END' ]
        T='trigger'; S='source'; D='dest'; A='after'; B='before'; C='conditions';
        transitions = [
            { T: 't_bottom_white', S: ['READY', 'BLACK'], D: 'WHITE', A: 'state_action' },
            { T: 't_bottom_black', S: ['READY', 'WHITE'], D: 'BLACK', A: 'state_action' },
            { T: 't_timeout',      S: ['WHTIE', 'BLACK'], D: 'END',   A: 'state_action' },
        ]
        self.machine = Machine(model=self,
                               initial='READY',
                               states=states,
                               transitions=transitions,
                               auto_transitions=False,
                               ignore_invalid_triggers=True)
        self.state_action()

    def state_action(self):
        if( self.state == 'READY' ):
            self.wr.mc.stop()
            self.wr.led.white()

        elif( self.state == 'WHITE' ):
            self.wr.mc.front_tl()
            self.wr.led.red()
            self.watch_dog.restart()

        elif( self.state == 'BLACK' ):
            self.wr.mc.front_tr()
            self.wr.led.blue()
            self.watch_dog.restart()

        elif( self.state == 'END' ):
            self.wr.mc.stop()
            self.wr.led.green()

    def check_timeout(self):
        return self.watch_dog.get_time() > 2

    def loop(self):

        # inovke triggers
        if( self.wr.ps.bottom() ): # white
            self.t_bottom_white()
        else: # black
            self.t_bottom_black()

        if( self.check_timeout() ):
            self.t_timeout()

        return self.state != 'END'

##################################################

def main(emulator, field):
    if( emulator ):
        wr = WR2WD_emulator(field=Field(field))
    else:
        wr = WR2WD()

    rb = robot(wr)

    ret = True
    while( ret ):
        try:
            ret = rb.loop()
        except KeyboardInterrupt:
            print( '\nbye')
            break

    if( emulator ):
        wr.disp_state()

if( __name__ == '__main__' ):
    parser = argparse.ArgumentParser(description='Line trace')

    parser.add_argument('-e', '--emulator', action='store_true', default=False)
    parser.add_argument('-f', '--field', default='black_white')

    args = parser.parse_args()
    main( **vars( args ) )

