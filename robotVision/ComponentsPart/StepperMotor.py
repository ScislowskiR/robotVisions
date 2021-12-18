import pyfirmata
import time
board=pyfirmata.Arduino('COM3')

board.digital[8].mode=pyfirmata.OUTPUT
board.digital[9].mode=pyfirmata.OUTPUT
board.digital[10].mode=pyfirmata.OUTPUT
board.digital[11].mode=pyfirmata.OUTPUT
while True:
    board.digital[11].write( 1 )
    board.digital[10].write( 0 )
    time.sleep(1)
    board.digital[11].write( 0 )
    board.digital[10].write( 0 )
    time.sleep(1)
    board.digital[8].write( 1 )
    board.digital[9].write( 0 )
    time.sleep(1)
    board.digital[8].write( 0 )
    board.digital[9].write( 0 )
    time.sleep(1)

    """
    board.digital[8].write( 1 )
    board.digital[9].write( 1 )
    time.sleep(500)
    board.digital[10].write( 1 )
    board.digital[11].write( 0 )
    time.sleep(500)
    board.digital[10].write( 1 )
    board.digital[11].write( 1 )
    time.sleep(500)
    ##############################
    board.digital[8].write( 0 )
    board.digital[9].write( 1 )
    time.sleep(500)
    board.digital[8].write( 1 )
    board.digital[9].write( 1 )
    time.sleep(500)
    board.digital[10].write( 0 )
    board.digital[11].write( 1 )
    time.sleep(500)
    board.digital[10].write( 1 )
    board.digital[11].write( 1 )
    time.sleep(500)
"""