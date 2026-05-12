from pymodbus.clent import ModbusTcpClient

client = ModbusTcpClient('192.168.0.3', port=502)

logo_connected = client.connect()

print(f'Connected: {logo_connected}')