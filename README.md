# Port Scanner

This Python script is designed to scan ports on a given host. It allows you to specify a range of ports to scan and optionally perform version detection to retrieve banners from open ports.

## How It Works

The script utilizes the `socket` module in Python to establish connections to specified ports on the provided host. It consists of two main functions:

1. **`get_banner(host, port)`**: This function attempts to retrieve the banner (service information) from a specified port on the given host. It sets a timeout of 5 seconds for the connection attempt and returns the received banner.

2. **`scan_ports(host, start_port, end_port, version_detection)`**: This function iterates over a range of ports between `start_port` and `end_port`, attempting to establish a connection to each port. If the connection is successful, it prints the port number along with the status (open/closed). If version detection is enabled, it also attempts to retrieve and display the banner.

The `main()` function takes user input for the host IP, start and end ports, and whether to perform version detection. It then initiates the port scanning process using the `scan_ports()` function.

## Error Handling

The script incorporates basic error handling to ensure robustness during execution. Error handling includes:

- **Socket Timeout**: A timeout of 1 second is set for socket connections to avoid prolonged waits.
- **Exception Handling**: Exceptions that occur during socket operations are caught and handled gracefully. If an exception occurs during banner retrieval or port scanning, an empty string is returned or an error message is printed respectively.

## Usage

1. Clone the repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python.
4. Follow the prompts to input the host IP, start and end ports, and whether to perform version detection.

### Example:
![portscanner](https://github.com/flamin-goes/PScan/assets/157055209/b98c54cf-8516-4074-89a5-c4e369889402)


### Notes

- Ensure that you have proper authorization before scanning ports on any network.
- This script may not be suitable for scanning large ranges of ports or hosts due to its single-threaded nature and potential performance limitations.

For any further assistance or inquiries, please feel free to contact the author.
