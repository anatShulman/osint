import psutil
import csv

# Get list of all running processes and their network connections
connections = []
for proc in psutil.process_iter(['pid', 'name']):
    try:
        connections.extend(proc.connections())
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# Extract IP address and URL for each connection
data = []
for conn in connections:
    if conn.status == psutil.CONN_ESTABLISHED and conn.raddr:
        url = ''
        ip = conn.raddr.ip
        try:
            url = conn.raddr.geturl()
        except AttributeError:
            pass
        data.append({'pid': conn.pid, 'name': psutil.Process(conn.pid).name(), 'ip': ip, 'url': url})

# Save data to CSV file
with open('network_connections.csv', 'w', newline='') as csvfile:
    fieldnames = ['pid', 'name', 'ip', 'url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for d in data:
        writer.writerow(d)

#This script uses the psutil.process_iter method to get a list of all running processes and their network connections. Then, it extracts the IP address and URL for each established connection using the psutil.CONN_ESTABLISHED constant and the raddr attribute. Finally, it saves the data into a CSV file using the csv.DictWriter class.

#Note that this script only extracts the IP address and URL of established connections. If you want to extract other information such as the port number or protocol, you can modify the script accordingly. Also note that some connections may not have a valid URL, so the url field may be empty in some cases.
