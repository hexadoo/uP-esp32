from machine import Pin,ADC
import time
import math 
import uThermistor

t = uThermistor.pThermistor(34,5000,2500,25,3950,False)
#pin,series_resistor,nominal_resistance,nominal_temperature,b_coefficient,high_side=True
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

#Seting
Vin=3.1
R0=5000


while True:
    Vout=adc.read() * 0.000805
    Rt=(Vout*R0)/(Vin - Vout)
    
    print('Pin Val: {}'.format(t.pinvalue()))
    print('T_Class: {}'.format(t.temperature()))
    print('---Vout: {}'.format(Vout))
    print('-----Rt: {}'.format(Rt))
    time.sleep(1)
