import psutil
import hashlib
import csv

def get_hash(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def services_hash():
    services = psutil.win_service_iter()
    with open('services_hashes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Service name', 'Executable path', 'SHA256 hash'])
        for service in services:
            try:
                binpath = service.as_dict()['binpath']
                binpath = binpath.split(' ', 1)[0]  # Split the path based on the first space character
                hash_value = get_hash(binpath)
                writer.writerow([service.name(), binpath, hash_value])
            except Exception as e:
                pass