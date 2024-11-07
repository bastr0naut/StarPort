# StarPort

This is a simple graphical user interface (GUI) application built with Python to scan a range of ports on a given IP address. It identifies open ports and displays them in green text for easy visibility. The application uses the `socket` library to attempt connections and `tkinter` for the GUI.

## Features
- Allows user input for IP address and port range (start and end).
- Scans each port in the specified range, showing only the open ports in green.
- Provides immediate feedback on the open ports and displays results in a dedicated text area within the GUI.

## Prerequisites
- Python 3.x installed on your machine.
- Required libraries:
  - `socket` (built-in with Python)
  - `tkinter` (also included with Python)

## Installation
1. Ensure that Python is installed on your machine by running `python --version` in your terminal or command prompt.
2. Clone this repository or download the script file.

## Usage
1. Run the program:
   ```bash
   python port_scanner_gui.py
   ```
2. Enter the IP address you want to scan in the "IP Address" field.
3. Specify the port range:
   - Enter the starting port in the "Start Port" field.
   - Enter the ending port in the "End Port" field.
4. Click the "Start Scan" button.
5. The results will be displayed in the text box below. Open ports are highlighted in green.

## Code Structure
- **IP Address Input**: User enters the IP address to scan.
- **Start and End Port Input**: User defines the port range for scanning.
- **Scan Button**: Starts the scan based on user input.
- **Results Display**: Shows open ports in green text, all within the main GUI window.

## Example
1. Enter `8.8.8.8` (Google’s DNS) as the IP.
2. Set the range from `70` to `90`.
3. Click "Start Scan" to view open ports in the specified range.

## License
This project is licensed under the MIT License.
