import socket
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from ttkthemes import ThemedStyle

KNOWN_PORTS = {
    20: "FTP data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    115: "SFTP",
    119: "NNTP",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    443: "HTTPS",
    465: "SMTPS",
    993: "IMAPS",
    995: "POP3S",
}

def get_service_name(port):
    return KNOWN_PORTS.get(port, "Unknown")

def get_banner(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((host, port))
            banner = s.recv(1024).decode('utf-8').strip()
            return banner
    except (socket.error, UnicodeDecodeError):
        return ""

def clear_output():
    text_area.delete(1.0, tk.END)

def scan_ports(host, custom_ports, show_close_ports, version_detection):
    clear_output()
    try:
        if not custom_ports:
            for port in range(1, 1025):
                port_scanner(host, port, show_close_ports, version_detection)
        else:
            if '-' in custom_ports:
                start_port, end_port = map(int, custom_ports.split('-'))

                for port in range(start_port, end_port + 1):
                    port_scanner(host, port, show_close_ports, version_detection)
            else:
                port = int(custom_ports)
                port_scanner(host, port, show_close_ports, version_detection)
    except KeyboardInterrupt:
        text_area.insert(tk.END, "Scan interrupted by the user.\n")

def port_scanner(host, port, show_close_ports=False, version_detection=False):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        if s.connect_ex((host, port)) == 0:
            if version_detection:
                banner = get_banner(host, port)
                service = get_service_name(port)
                result = f"{port}/tcp    open     {service:<15} {banner}"
                text_area.insert(tk.END, result + '\n')
            else:
                service = get_service_name(port)
                result = f"{port}/tcp    open     {service:<15}"
                text_area.insert(tk.END, result + '\n')
            root.update_idletasks()  # Update the GUI to display the output immediately
        elif show_close_ports:
            service = get_service_name(port)
            result = f"{port}/tcp    closed   {service:<15}"
            text_area.insert(tk.END, result + '\n')
            root.update_idletasks()  # Update the GUI to display the output immediately
    except socket.error as e:
        text_area.insert(tk.END, f"Error scanning port {port}: {e}\n")
        root.update_idletasks()  # Update the GUI to display the output immediately
    except KeyboardInterrupt:
        text_area.insert(tk.END, "Scan interrupted by the user.\n")
    finally:
        s.close()

def start_scan():
    clear_output()  # Clear the previous output
    host = host_entry.get()
    custom_ports = custom_ports_entry.get()
    show_close_ports = show_close_ports_var.get()
    version_detection = version_detection_var.get()

    scan_ports(host, custom_ports, show_close_ports, version_detection)

root = tk.Tk()
root.title("Port Scanner")

style = ThemedStyle(root)
style.set_theme("plastik")

main_frame = ttk.Frame(root, padding="20")
main_frame.pack()

host_label = ttk.Label(main_frame, text="Host IP")
host_label.grid(row=0, column=0, pady=5, sticky="w")
host_entry = ttk.Entry(main_frame)
host_entry.grid(row=0, column=1, pady=5)

custom_ports_label = ttk.Label(main_frame, text="Enter a custom port(s) (Enter for default):")
custom_ports_label.grid(row=1, column=0, pady=5, sticky="w")
custom_ports_entry = ttk.Entry(main_frame)
custom_ports_entry.grid(row=1, column=1, pady=5)

show_close_ports_var = tk.BooleanVar()
show_close_ports_checkbox = ttk.Checkbutton(main_frame, text="Display closed ports", variable=show_close_ports_var)
show_close_ports_checkbox.grid(row=2, columnspan=2, pady=5)

version_detection_var = tk.BooleanVar()
version_detection_checkbox = ttk.Checkbutton(main_frame, text="Perform version detection", variable=version_detection_var)
version_detection_checkbox.grid(row=3, columnspan=2, pady=5)

start_scan_button = ttk.Button(main_frame, text="Start Scan", command=start_scan)
start_scan_button.grid(row=4, columnspan=2, pady=10)

text_area = scrolledtext.ScrolledText(main_frame, width=60, height=20)
text_area.grid(row=5, columnspan=2, pady=10)

root.protocol("WM_DELETE_WINDOW", root.destroy)  # Handle the window close event
root.mainloop()