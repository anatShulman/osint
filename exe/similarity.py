import tlsh
import os
import subprocess
import shutil

def compute_tlsh(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        hash_value = tlsh.hash(data)
    return hash_value

def compute_ssdeep(file_path):
    try:
        ssdeep_output = subprocess.check_output(['ssdeep.exe', file_path.replace("/", "\\")])
        return ssdeep_output.decode().split("\n")[1].split(",")[0]
    except:
        try:
            # create a temporary copy of the file in current directory
            temp_path = os.path.join(os.getcwd(), os.path.basename(file_path))
            shutil.copy(file_path, temp_path)
            
            # set the file attributes to hidden
            win32api.SetFileAttributes(temp_path, win32con.FILE_ATTRIBUTE_HIDDEN)

            # compute ssdeep of the temporary copy
            ssdeep_output = subprocess.check_output(['ssdeep.exe', temp_path.replace("/", "\\")])
            ssdeep_hash = ssdeep_output.decode().split("\n")[1].split(",")[0]
                       
            # delete the temporary copy
            os.remove(temp_path)
            
            return ssdeep_hash
        except:
            return 'NaN'