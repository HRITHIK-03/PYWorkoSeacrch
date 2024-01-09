import pymongo
def store_in_mongodb(job_list):
    # Connect to MongoDB 
    client = pymongo.MongoClient('mongodb://localhost:27017/')

    #  create a database
    database = client['jobs_database']

    # create a collection 
    collection = database['python_developer_jobs']

    # Insert the job list into the collection
    collection.insert_many(job_list)

    # Close the MongoDB connection
    client.close()