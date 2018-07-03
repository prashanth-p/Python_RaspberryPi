import Adafruit_GPIO.I2C as i2c
import sys

def connectDeviceI2C(devAddress, regAddress, command, writeVal=0x00):
    busNumber = i2c.get_default_bus()
    print "Bus Number: " + str(busNumber)
    print "Device Address: " + hex(devAddress)
    print "Register Address: " + hex(regAddress)
    print "Command: " + str(command)

    Device = i2c.get_i2c_device(devAddress)
    print ""

    if not(command):
        print "Write Val: " + hex(writeVal)
        write(Device, regAddress,writeVal) 
    else:
        print "Reading from Register with address: " + str(regAddress)
        read(Device, regAddress)


def write(Device,regAddress,writeVal):
    print "In function Write"
    print "Writing in Register with address: " + hex(regAddress)
    Device.write8(regAddress,writeVal)

def read(Device,regAddress):
    print "In function read"
    print "Check if same value is read after writing"
    test_val = hex(Device.readU8(regAddress))
    print "Test Value in Register: " + str(test_val)


if __name__ == "__main__":

    deviceAddress = (int(sys.argv[1],16))
    regAddress = (int(sys.argv[2],16))
    command = int(sys.argv[3])
    if not command:
        writeVal = (int(sys.argv[4],16))
        connectDeviceI2C(deviceAddress,regAddress,command,writeVal)

    else:
        connectDeviceI2C(deviceAddress,regAddress,command)
