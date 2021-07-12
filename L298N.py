# L298 code Inspired by: Olivier Lenoir - olivier.len02@gmail.com

# Author: Hexadoo - hexadoo1@gmail.com
# Created: 2021-07-04 11:08
# Project: L298 Dual H-bridge, MicroPython, ESP32
# Description: Set_Speed is from 0-100% 

from machine import Pin, PWM
from utime import sleep

class L298(object):
    def __init__(self, en, in1, in2, freq=1000):
        self.freq = freq
        self.speed = 0
        self.p_en = PWM(Pin(en), freq=self.freq, duty=self.speed)
        self.p_in1 = Pin(in1, Pin.OUT)
        self.p_in2 = Pin(in2, Pin.OUT)
        self.p_in1(0)
        self.p_in2(0)

    def stop(self):
        self.p_en.duty(0)
        self.p_in1(0)
        self.p_in2(0)

    def forward(self):
        self.p_in2(0)
        self.p_en.duty(self.speed)
        self.p_in1(1)

    def reverse(self):
        self.p_in1(0)
        self.p_en.duty(self.speed)
        self.p_in2(1)

    def set_speed(self, speed):
        speed = int(speed * 1024 / 100)
        self.speed = min(1023, max(0, speed))
    
    # direction 1 = foward 0 = reverse
    def move_to_stop(self,direction,speed,time):
        self.set_speed(speed)
        if direction == 1:
            self.forward()
        elif direstion == 0:
            self.reverse()
        else:
            self.stop()
        
        sleep(time)
        self.stop()