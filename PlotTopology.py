import numpy as np
import graphviz
import os

# Provided IP addresses (modify as needed)
ip_dict = {
    "mcladhoc-01": {"WiFi": "192.168.210.60"},
    "mcladhoc-02": {"WiFi": "192.168.210.61"},
    "mcladhoc-03": {"WiFi": "192.168.210.62"},
    "mcladhoc-04": {"WiFi": "192.168.210.63"},
    "mcladhoc-05": {"WiFi": "192.168.210.64"},
    "mcladhoc-06": {"WiFi": "192.168.210.65"},
    "mcladhoc-07": {"WiFi": "192.168.210.66"}
}

# Extract only WiFi IP addresses
wifi_ips = [details["WiFi"] for details in ip_dict.values()]

# Latency matrix (example data provided by remote device)
# REPLACE HERE!
latency_matrix = np.array([
    [0, np.nan, 8.57, 5.95, 0.107, 10.8, 5.16],
    [np.nan, 0, 8.6, 5.06, 0.096, 10.0, 4.8],
    [np.nan, np.nan, 0, 9.32, 0.118, 9.48, 5.02],
    [np.nan, np.nan, 13.0, 0, 0.117, 10.2, 4.79],
    [np.nan, np.nan, 8.16, 5.62, 0, 5.23, 5.05],
    [np.nan, np.nan, 8.43, 4.93, 0.106, 0, 7.96],
    [np.nan, np.nan, 8.26, 5.2, 0.108, 8.04, 0]
])

node_labels = list(ip_dict.keys())

# Create a Graphviz graph
#dot = graphviz.Graph(comment='Network Topology')
dot = graphviz.Graph(comment='Network Topology', graph_attr={'splines': 'true', 'overlap': 'false'})

for label in node_labels:
    dot.node(label, label, shape='circle', style='filled', color='lightblue', fontname='arial', fontsize='10')

for i, label1 in enumerate(node_labels):
    for j, label2 in enumerate(node_labels):
        if not np.isnan(latency_matrix[i, j]) and i != j:
            latency = latency_matrix[i, j]
            dot.edge(label1, label2, label=f'{latency:.2f} ms', color='gray', fontname='arial', fontsize='7')

# Save and render the graph
home_dir = os.path.expanduser('~')
output_file_path = os.path.join(home_dir, 'network_topology')

# Save and render the graph
output_path = dot.render(output_file_path, format='png', view=True)
print(f'Graph rendered to: {output_path}')

#print(dot.source)
