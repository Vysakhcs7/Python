import serial

# Configuration
PORT = 'COM8'  # Replace with your serial port
BAUDRATE = 115200  # Replace with your baud rate
TIMEOUT = 1  # Timeout for read operations in seconds
CHUNK_SIZE = 2048  # Size of data chunks to send

def send_file(filename):
    # Open the binary file for reading
    with open(filename, 'rb') as file:
        # Open the serial port with specified configuration
        ser = serial.Serial(PORT, BAUDRATE, timeout=TIMEOUT)

        # Send the length of the file first
        file.seek(0, 2)  # Move to the end of the file to get length
        length = file.tell()  # Get the length of the file
        file.seek(0)  # Move back to the start of the file
        ser.write(length.to_bytes(4, 'little'))  # Send length as 4 bytes

        # Send the file data in chunks
        while True:
            chunk = file.read(CHUNK_SIZE)  # Read a chunk of data
            if not chunk:  # If no more data, break the loop
                break
            ser.write(chunk)  # Send the chunk over UART

        # Close the serial port
        ser.close()

def main():
    send_file(r"D:\Python\USER_APP_2.bin")  # Replace with your binary file

if __name__ == '__main__':
    main()



# import serial
# import time

# def send_firmware(serial_port, baud_rate, firmware_path):
#     # Open the serial port
#     with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
#         # Read the firmware binary file
#         with open(firmware_path, 'rb') as firmware_file:
#             firmware_data = firmware_file.read()

#         # Send the firmware data in chunks
#         chunk_size = 1024  # Adjust chunk size if necessary
#         for i in range(0, len(firmware_data), chunk_size):
#             chunk = firmware_data[i:i+chunk_size]
#             ser.write(chunk)
#             time.sleep(0.01)  # Small delay between chunks to prevent overflow
#             print(f"Sent {i + len(chunk)} / {len(firmware_data)} bytes")

#     print("Firmware transmission completed.")

# # Example usage
# if __name__ == "__main__":
#     serial_port = 'COM8'  # Replace with your serial port (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux)
#     baud_rate = 115200  # Set the baud rate to match your STM32 configuration
#     firmware_path = 'path_to_your_firmware.bin'  # Replace with the path to your .bin file

#     send_firmware(serial_port, baud_rate, firmware_path)

