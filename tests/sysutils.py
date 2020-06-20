import psutil



def getIp():
    networks = psutil.net_if_addrs()
    ip = networks['wlan0'][0].address
    return ip

    
def getTemp():
    return psutil.sensors_temperatures(fahrenheit=False)['cpu-thermal'][0].current

    