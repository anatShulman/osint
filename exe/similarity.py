import tlsh
import subprocess

def compute_tlsh(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        hash_value = tlsh.hash(data)
    return hash_value

def compute_ssdeep(file_path):
    ssdeep_output = subprocess.check_output(['ssdeep.exe', file_path.replace("/", "\\")])
    return ssdeep_output.decode().split("\n")[1].split(",")[0]
