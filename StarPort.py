import socket
import tkinter as tk
from tkinter import messagebox

def scan_ports(ip, start_port, end_port):
    open_ports = []
    result_text.delete(1.0, tk.END)  # Clear previous results
    
    for port in range(start_port, end_port + 1):
        try:    
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except Exception as e:
            print(f"Error: {e}")

    # Display results with green text for open ports
    if open_ports:
        open_ports_text = f"Open ports on {ip}: {', '.join(map(str, open_ports))}\n"
        result_text.insert(tk.END, open_ports_text, "green_text")
    else:
        result_text.insert(tk.END, f"No open ports found on {ip} in the range {start_port}-{end_port}.\n")

def start_scan():
    # Retrieve values from the input fields
    ip = ip_entry.get()
    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
        scan_ports(ip, start_port, end_port)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for ports.")

# GUI setup
root = tk.Tk()
root.title("StarPort")

tk.Label(root, text="IP Address:").grid(row=0, column=0, padx=5, pady=5)
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Start Port:").grid(row=1, column=0, padx=5, pady=5)
start_port_entry = tk.Entry(root)
start_port_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="End Port:").grid(row=2, column=0, padx=5, pady=5)
end_port_entry = tk.Entry(root)
end_port_entry.grid(row=2, column=1, padx=5, pady=5)

scan_button = tk.Button(root, text="Start Scan", command=start_scan)
scan_button.grid(row=3, column=0, columnspan=2, pady=10)

# Text box to display results
result_text = tk.Text(root, height=10, width=40)
result_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Define a tag for green text
result_text.tag_config("green_text", foreground="green")

root.mainloop()
