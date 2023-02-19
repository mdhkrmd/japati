import tm1637
from time import sleep
from gpiozero import Button
from signal import pause

tm = tm1637.TM1637(clk=23, dio=24)
button = Button(22)

def countdown(start, stop, step):
    for i in range(start, stop, step):
        tm.numbers(0, i)
        sleep(1)

while True:
    a = int(input("Masukan banyak orang = "))
    if a < 1 :
        button.wait_for_press()
        print("Tak ada orang")
    elif a <= 3 :
        start = 5
        stop = -1
        step = -1
        button.wait_for_press()
        countdown(start, stop, step)
    elif a > 3 :
        start = 10
        stop = -1
        step = -1
        button.wait_for_press()
        countdown(start, stop, step)
