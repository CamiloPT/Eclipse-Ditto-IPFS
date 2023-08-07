import app.helper as helper
import shutil
import json

def create_file_copies(source_file, num_copies):
  for i in range(num_copies):
      # Construct the destination filename
      destination_file = f"{source_file}_{i+1}.json"

      # Create a copy of the source file
      shutil.copy2(source_file, destination_file)
      print(f"Created copy: {destination_file}")

def read_json_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        json_data = json.load(file)

    test = {}
    for i in list(range(0, 20)):
        test[f"field_{i}"] = f"value_{i}"
    print(test)
    for result in json_data["results"]:
        result["attributes"] = {**test, **result["attributes"]}

    with open(output_file_path, 'w') as file:
      json.dump(json_data, file, indent=4)


#read_json_file('./data/thing:org.Iotp2c:iwatch.json', './data/thing:org.Iotp2c:iwatch_20.json')

#create_file_copies('./data/thing:org.Iotp2c:iwatch_20.json', 100)
#response = helper.save_ditto_things_ipfs()
#helper.send_ipfs_hash_blockchain(response)
helper.things_data_to_ipfs()
