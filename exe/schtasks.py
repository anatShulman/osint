import subprocess
import csv

# Run the schtasks command to list all scheduled tasks
output = subprocess.check_output('schtasks.exe /query /fo csv', shell=True)

# Decode the output as a string and split it into lines
output = output.decode('utf-8')
lines = output.splitlines()

# Use the csv module to create a writer object and write the output to a CSV file
with open('scheduled_tasks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for line in lines:
        row = line.split(',')
        writer.writerow(row)

#This script uses the subprocess.check_output function
#  to run the schtasks.exe command with the /query and
#  /fo csv options, which lists all scheduled tasks in
#  CSV format. The output is then decoded as a string
#  and split into lines using the splitlines() method.

#The script then uses the csv.writer function to create
#  a writer object, which is used to write each line of
#  the output to a row in the CSV file. The newline=''
#  parameter is used to prevent extra blank lines from 
# being inserted between rows in the CSV file.

#After running this script, a file named scheduled_tasks.csv
#  will be created in the same directory as the script,
#  containing a list of all scheduled tasks in CSV format.
