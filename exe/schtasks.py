import subprocess
import csv

def scheduled_tasks():
    # Run the schtasks command to list all scheduled tasks
    output = subprocess.check_output('schtasks.exe /query /fo csv', shell=True)

    # Decode the output as a string and split it into lines
    output = output.decode('utf-8')
    lines = output.splitlines()

    # Use the csv module to create a writer object and write the output to a CSV file
    with open('scheduled_tasks.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for line in lines:
            # Split the line into fields and strip the double quotes from each field
            row = [field.strip('"') for field in line.split(',')]
            writer.writerow(row)