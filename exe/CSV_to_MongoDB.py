import csv
from pymongo import MongoClient

def upload(CSV_name):
    # Connect to the MongoDB instance
    client = MongoClient("mongodb+srv://anatshulman:2HBYgG53On6MzWu4@cluster0.i84nq3q.mongodb.net/?retryWrites=true&w=majority")

    # Choose a database and collection to insert into
    db = client['Cluster0']
    collection = db['CSV']

    # Read the CSV file
    with open(CSV_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        # Insert each row into the collection
        for row in reader:
            collection.insert_one(row)
    return

