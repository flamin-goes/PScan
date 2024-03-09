import socket

# Defining a function to scan the ports specified by the user
def scan_ports(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)

            if s.connect_ex((host, port)) == 0:
                print(f"Port {port} is open.")
            else:
                print(f"Port {port} is closed.")

def main():
    host = input("Enter the host IP: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    print("\nScanning ports...\n")
    scan_ports(host, start_port, end_port)

if __name__ == "__main__":
    main()