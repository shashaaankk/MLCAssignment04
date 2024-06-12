import os
import numpy as np
import graphviz

# Provided IP addresses
ip_dict = {
    "mcladhoc-01": {"Ethernet": "129.69.210.60", "WiFi": "192.168.210.60"},
    "mcladhoc-02": {"Ethernet": "129.69.210.61", "WiFi": "192.168.210.61"},
    "mcladhoc-03": {"Ethernet": None, "WiFi": "192.168.210.62"},
    "mcladhoc-04": {"Ethernet": "129.69.210.63", "WiFi": "192.168.210.63"},
    "mcladhoc-05": {"Ethernet": "129.69.210.64", "WiFi": "192.168.210.64"},
    "mcladhoc-06": {"Ethernet": "129.69.210.65", "WiFi": "192.168.210.65"},
    "mcladhoc-07": {"Ethernet": "129.69.210.66", "WiFi": "192.168.210.66"}
}

# IP of Wireless interfaces
ip_lst = [details["WiFi"] for details in ip_dict.values()]

# Initialize a NumPy array to store latency results
latency_matrix = np.full((len(ip_lst), len(ip_lst)), np.nan)

# Function to measure latency
def measure_latency(fromip,ip):
    try:
        response = os.popen(f"ping -c 1 {ip}").read()
        #print(f"Pinging {ip} from {fromip}")
        #print(response)  
        for line in response.split('\n'):
            if 'time=' in line:
                # Extract the time value (in ms)
                time = float(line.split('time=')[1].split(' ')[0])
                return time
        return np.nan
    except Exception as e:
        print(f"Error pinging {ip}: {e}")
        return np.nan

# Pinging every IP from every IP
for i, ip1 in enumerate(ip_lst):
    for j, ip2 in enumerate(ip_lst):
        if ip1 == ip2:
            latency_matrix[i, j] = 0.0  # Pinging Self
        else:
            latency = measure_latency(ip1,ip2)
            latency_matrix[i, j] = latency
        print(f"Latency[{ip1}, {ip2}] = {latency_matrix[i, j]}")  
     
# Print the latency matrix
print("Latency Matrix:")
print(latency_matrix)
