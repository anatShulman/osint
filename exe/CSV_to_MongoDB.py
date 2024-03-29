import csv
from pymongo import MongoClient
from similarity import *

def check_connection():
    # Attempt to connect to the MongoDB instance
    try:
        client = MongoClient("mongodb+srv://anatshulman:2HBYgG53On6MzWu4@cluster0.i84nq3q.mongodb.net/?retryWrites=true&w=majority")
        # Access the list_database_names() method to force the client to connect
        client.list_database_names()
        db = client['test']
        collection = db['CSV']
        return collection
    # If there is an error connecting, return False
    except:
        return False

def upload_dict(dictionary, label_db, label_cirle, parent, collection):
    
    if dictionary['instance of'] != 'network connection' and dictionary['instance of'] != 'scheduled task':
        dictionary['ssdeep'] = compute_ssdeep(dictionary['file path']+'\\'+dictionary['file name'])
    
    # transmitinig
    label_cirle.configure(fg='#00e1ff')
    parent.update()

    collection.insert_one(dictionary)

    label_cirle.configure(fg='#00ff80')
    parent.update()
    
    return

def upload(CSV_name):
    # Connect to the MongoDB instance
    client = MongoClient("mongodb+srv://anatshulman:2HBYgG53On6MzWu4@cluster0.i84nq3q.mongodb.net/?retryWrites=true&w=majority")

    # Choose a database and collection to insert into
    db = client['test']
    collection = db['CSV']

    # Read the CSV file
    with open(CSV_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        # Insert each row into the collection
        for row in reader:
            collection.insert_one(row)
    return

