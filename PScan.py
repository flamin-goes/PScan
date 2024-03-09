import socket

def get_banner(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((host, port))
            banner = s.recv(1024).decode('utf-8').strip()
            return banner
    except:
        return ""

def scan_ports(host, start_port, end_port, version_detection):
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)

            if s.connect_ex((host, port)) == 0:
                if version_detection:
                    banner = get_banner(host, port)
                    result = f"{port}/tcp    open     {banner}"
                else:
                    result = f"{port}/tcp    open"

                print(result)
            else:
                print(f"{port}/tcp    closed")

def main():
    host = input("Enter the host IP: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    version_detection = input("Perform version detection? (y/n): ").lower() == 'y'

    print("\nScanning ports...\n")
    scan_ports(host, start_port, end_port, version_detection)

if name == "main":
    main()