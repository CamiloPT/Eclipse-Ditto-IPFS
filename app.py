import pymongo
import json
import schedule
import time
import ipfsApi
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

# General configs
MONGO_DB_CLIENT = os.environ.get("MONGO_DB_CLIENT", "localhost:27017")
IPFS_CLIENT = os.environ.get("IPFS_CLIENT", "127.0.0.1")
IPFS_CLIENT_PORT = os.environ.get("IPFS_CLIENT_PORT", 5001)
DATA_FILE = "things_data.json"

# Eclipse Ditto MongoDB configs
mongoClient = pymongo.MongoClient(f"mongodb://{MONGO_DB_CLIENT}")
database = mongoClient["things"]
collection = database["things_journal"]

# IPFS configs
ipfs = ipfsApi.Client(IPFS_CLIENT, IPFS_CLIENT_PORT)

def save_ditto_things_ipfs():
    last_hour_things = list(map(map_mongo_thing, get_last_hour_things()))

    now = datetime.now()

    ditto_data_to_file(last_hour_things)
    ipfs_response = things_data_to_ipfs()
    print(f"{now.strftime('%Y-%m-%d %H:%M:%S')}: {len(last_hour_things)} entries -> {ipfs_response}")

def get_last_hour_things():
    last_hour = datetime.utcnow() - timedelta(hours=1)
    query = { "events": { "$elemMatch": { "p._timestamp": { "$gte": last_hour.strftime("%Y-%m-%d %H:%M:%S") } } } }
    pipeline = [
        { '$match': query },
        { '$group': { '_id': '$pid', 'docs': { '$push': '$$ROOT' } } },
        { '$project': { '_id': '$_id', 'documents': '$docs' } }
    ]
    return collection.aggregate(pipeline=pipeline)

def ditto_data_to_file(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def things_data_to_ipfs():
    return ipfs.add(DATA_FILE)

def map_mongo_thing(mongo_thing):
    return {
        "thingId": mongo_thing["_id"],
        "results": map_mongo_attributes(mongo_thing["documents"])
    }

def map_mongo_attributes(documents):
    results = []
    for entry in documents:
        for event in entry["events"]:
            thing = event["p"]["thing"]
            results.append({
                "timestamp": event["p"]["_timestamp"],
                "attributes": thing["attributes"]
            })
    return results

print("Listening for Ditto Things started....")
schedule.every().hour.do(save_ditto_things_ipfs)

while True:
    schedule.run_pending()
    time.sleep(1)
