# Author: Hexadoo - hexadoo1@gmail.com
# Created: 2021-07-25 10:59
# Project: Thermistor driver, MicroPython, ESP32
# Description: 

from machine import Pin, ADC
import time
import math

class pThermistor:
    def __init__(self,pin,series_resistor,nominal_resistance,nominal_temperature,b_coefficient,high_side=True):
        self.pin = ADC(Pin(pin))
        self.pin.atten(ADC.ATTN_11DB)   # 11DB Set 3.3V Range
        self.pin.width(ADC.WIDTH_12BIT) # 12BIT set reading range to 4095
        self.Vin = 3849 #change Vout if change the ADC.WIDTH_xxBit value (at 95% for 3.1V)
        self.series_resistor = series_resistor # Resistance used in the circuit
                
        self.nominal_resistance = nominal_resistance # Thermistor nominal resistance
        self.nominal_temperature = nominal_temperature # Thermistor nominal temperatur at nominal resistance
        self.b_coefficient = b_coefficient
        self.high_side = high_side
        

    def temperature(self):
        """Temp in Celsius"""
        self.Vout = self.pin.read() 
        
        if self.high_side:
            # Thermistor connected from 3.3V to ADC (mid point: ADC, Thermisor & resistor).
            a=5
        else:
            # Thermistor conected from ADC to ground.
            #Rt=(Vout*R0)/(Vin - Vout)  use basic voltage divider formula to find the resistance of termistor
            reading = (self.Vout * self.series_resistor) / (self.Vin - self.Vout )
            #reading = (2047 * self.series_resistor) / (self.Vin - 2047 )
      
        steinhart = math.log(reading / self.nominal_resistance) / self.b_coefficient      # log(R/Rn) / beta
        steinhart += 1.0 / (self.nominal_temperature + 273.15)         # log(R/Rn) / beta + 1/To
        steinhart = (1.0 / steinhart) - 273.15   # Invert, convert to C

        return steinhart
    
    
    
    def pinvalue(self):
        
        return self.pin.read()

