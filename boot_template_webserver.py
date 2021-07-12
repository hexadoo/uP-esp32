# 

def no_debug():
    import esp
    esp.osdebug(None)
    

def connect():
    try:
      import usocket as socket
    except:
      import socket

    import network
    import gc
    gc.collect()
    
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<YOUR WIFI SSID>', '<YOUR WIFI PASS>')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

