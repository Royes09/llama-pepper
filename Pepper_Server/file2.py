import json
import requests
from file1 import output_device

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def output_ai () : 
    
    output = query({
    "inputs":  output_device() ,
})
    # Step 3: Convert the dictionary to a JSON string
    json_string = json.dumps(output, indent=2)  # indent for pretty printing
    print("JSON String:")
    print(json_string)
# Step 4: Write the JSON string to a file
    with open('data.json', 'w') as json_file:
        json.dump(output, json_file, indent=2)
# Step 5: Read JSON data from a file
    with open('data.json', 'r') as json_file:
        loaded_data = json.load(json_file)
    print("\nGenerated Text:")
    print(loaded_data[0]["generated_text"])
    text = str(loaded_data[0]["generated_text"])
    return text
