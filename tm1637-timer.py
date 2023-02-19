import tm1637
from time import sleep
tm = tm1637.TM1637(clk=23, dio=24)

start = 59
stop = -1
step = -1

#for i in range(start, stop, step):
#    tm.numbers(0, i)
#    sleep(1)

# all LEDS on "88:88"
#tm.write([127, 255, 127, 127])

# all LEDS off
#tm.write([0, 0, 0, 0])

# show "0123"
#tm.write([63, 6, 91, 79])

# show "COOL"
#tm.write([0b00111001, 0b00111111, 0b00111111, 0b00111000])

# show "HELP"
#tm.show('help')

# display "dEAd", "bEEF"
#tm.hex(0xdead)
#tm.hex(0xbeef)

# show "12:59"
tm.numbers(00,00)

# show "-123"
#tm.number(-123)

# show temperature '24*C'
#tm.temperature(24)