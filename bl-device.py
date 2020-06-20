import bluetooth

def scan():
    print("Searching for nearby devices...")
    devices = bluetooth.discover_devices() 
    for addr in devices: 
        print(addr+" : "+bluetooth.lookup_name(addr))
    if not devices:
        print("No Devices found")
        
def connect(addr):
    hostMACAddress = addr # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
    port = 3
    backlog = 1
    size = 1024
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.bind((hostMACAddress, port))
    s.listen(backlog)
    try:
        client, clientInfo = s.accept()
        while 1:
            data = client.recv(size)
            if data:
                print(data)
                client.send(data) # Echo back to client
    except: 
        print("Closing socket")
        client.close()
        s.close()


connect('70:48:F7:45:7B:4E')
