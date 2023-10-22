# Import the smbus library for I2C communication and the time library
import smbus
import time

# Define the I2C address for the light sensor
light_sensor = 0x23

# Define constants for sensor configurations
low_power = 0x00
high_power = 0x01
Reset = 0x07
ONE_TIME_HIGH_RES_MODE = 0x23

# Initialize an SMBus object (I2C communication)
bus = smbus.SMBus(1)

# Function to calculate light intensity based on sensor readings
def Light_intensity(address):
    # Calculate the light intensity from the sensor readings and scale it
    result = ((address[1] + (256 * address[0])) / 1.2)
    return result

# Function to read light intensity from the sensor
def light():
    # Read sensor data for one-time high-resolution mode
    address = bus.read_i2c_block_data(light_sensor, ONE_TIME_HIGH_RES_MODE)
    # Calculate and return light intensity using the Light_intensity function
    value = Light_intensity(address)
    return value

# Main function to continuously read and print light intensity
def main():
    while True:
        # Read light intensity from the sensor
        lux = light()
        # Print the light intensity
        print(lux)

        # Evaluate the light intensity and print corresponding messages
        if lux >= 1200:
            print("Too bright")
        elif 700 <= lux < 1200:
            print("Bright")
        elif 300 <= lux < 700:
            print("Medium")
        elif 50 <= lux < 300:
            print("Dark")
        elif lux < 50:
            print("Too Dark")

        # Pause for 0.5 seconds before the next reading
        time.sleep(0.5)

# Call the main function to start reading and processing light data
main()
