from bluetooth.ble import DiscoveryService
import bluetooth
print("Searching for nearby devices...")
service = DiscoveryService()
devices = service.discover(2)
for address, name in devices.items():
	print("name: {},adress: {}".format(name,address))
if not devices:
    print("No Devices found")
