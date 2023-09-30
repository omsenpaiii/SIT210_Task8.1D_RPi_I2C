import smbus
import time

light_sensor = 0x23

low_power = 0x00
high_power = 0x01
Reset = 0x07
ONE_TIME_HIGH_RES_MODE = 0X23 

bus = smbus.SMBus(1)

def Light_intensity(address):
    result = ((address[1] + (256 *address[0]))/1.2)
    return result

def light():
    address = bus.read_i2c_block_data(light_sensor,ONE_TIME_HIGH_RES_MODE)
    value = Light_intensity(address)
    return value
 
def  main():
    while True:
        lux = light()
        print (lux)

        if(lux >= 1200):
            print("Too bright")
        elif(lux >= 700 and lux < 1199):
            print("Bright")
        elif(lux >= 300 and lux < 699):
            print("Medium")    
        elif(lux < 50 and lux > 299):
            print("Dark")
        elif(lux < 49):
            print("Two Dark")
        
        time.sleep(0.5)
main ()