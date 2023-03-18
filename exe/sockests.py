import psutil
import subprocess
import csv
from CSV_to_MongoDB import *

def netstat():
    # Run the netstat command to get a list of all active connections
    output = subprocess.check_output('netstat -ano', shell=True)

    # Decode the output as a string and split it into lines
    output = output.decode('utf-8')
    lines = output.splitlines()

    # Extract information about each connection and store it in a list
    data = []
    for line in lines:
        line = line.strip()
        if line.startswith('TCP') or line.startswith('UDP'):
            parts = line.split()
            proto = parts[0]
            local_addr = parts[1]
            remote_addr = parts[2]
            state = parts[3]
            pid = parts[-1]
            data.append({'proto': proto, 'local_addr': local_addr, 'remote_addr': remote_addr, 'state': state, 'pid': pid})

    # Use the csv module to create a writer object and write the data to a CSV file
    with open('netstat.csv', 'w', newline='') as csvfile:
        fieldnames = ['proto', 'local_addr', 'remote_addr', 'state', 'pid', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for d in data:
            # Use the pid to get information about the process, including its executable path
            try:
                p = psutil.Process(int(d['pid']))
                url = ''
                try:
                    url = p.exe()
                except psutil.AccessDenied:
                    pass
                d['url'] = url
            except (psutil.NoSuchProcess, psutil.AccessDenied, ValueError):
                pass
            writer.writerow(d)
        
    upload(os.getcwd()+'\netstat.csv')