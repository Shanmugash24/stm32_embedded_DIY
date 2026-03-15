from pymodbus.client import ModbusSerialClient
import struct

PORT = "/dev/ttyUSB0"
SLAVE_ID = 3

client = ModbusSerialClient(
    port=PORT,
    baudrate= 115200,
    bytesize=8,
    parity="N",
    stopbits=1,
    timeout=3
)


def read_float(address):

    result = client.read_holding_registers(
        address=address,
        count=2,
        device_id=SLAVE_ID
    )

    if result.isError():
        print("Read error at", address)
        return None

    regs = result.registers

    # Convert two 16-bit registers → 32-bit float
    raw = struct.pack(">HH", regs[0], regs[1])
    value = struct.unpack(">f", raw)[0]

    return value


if client.connect():

    print("FCU In:", read_float(0))
    print("Condenser Out:", read_float(2))
    print("Evaporator Out:", read_float(4))
    print("FCU Out:", read_float(6))
    print("Evaporator In:", read_float(8))
    print("Geyser Out:", read_float(10))
    print("LP Pressure:", read_float(12))
    print("HP Pressure:", read_float(14))
    print("Water Pressure:", read_float(16))
    print("Condenser In:", read_float(18))
    print("Geyser In:", read_float(20))
    print("Air Chamber Temp:", read_float(22))
    print("Cooler Cut ON:", read_float(24))
    print("Heater Cut ON:", read_float(26))
    print("Evaporator Setpoint:", read_float(28))
    print("Cooler Mode Temp:", read_float(30))
    print("Heater Mode Temp:", read_float(32))
    print("Room Temp:", read_float(34))
    print("Heater Actuator %:", read_float(36))
    print("Chillwater Actuator %:", read_float(38))
    print("Supply Actuator %:", read_float(40))

    client.close()

else:
    print("Connection failed")