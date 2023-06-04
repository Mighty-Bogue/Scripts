import socket

def send_hexadecimal(ip, port, hexadecimal):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the target server
        client_socket.connect((ip, port))

        # Convert the hexadecimal string to bytes
        hex_bytes = bytes.fromhex(hexadecimal)

        # Send the hexadecimal bytes
        client_socket.sendall(hex_bytes)
        print("Hexadecimal data sent successfully.")
        client_socket.settimeout(5)
        a=client_socket.recv(100)
        print(a)

    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running and the provided IP and port are correct.")

# Set target's IP, Port and data you want to send
ip_address = "10.10.10.10"  # Replace with the IP address of the server
port_number = 4444  # Replace with the port number of the server
hex_data = "00 00 00 47 c2" # Replace with hex
