from datasets import load_dataset
import json

mario_data = load_dataset("TheGreatRambler/mm2_level", split="train", streaming=True)

n=20000
loaded_data = []

for item in mario_data:
    important_info = {
        "num_comments": item["num_comments"],
        "attempts": item["attempts"],
        "clears": item["clears"],
        "plays": item["plays"],
        "likes": item["likes"],
        "boos": item["boos"],
        "world_record": item["world_record"]
    }
    loaded_data.append(important_info)
    if len(loaded_data) > n:
        break

json_file = json.dumps(loaded_data, indent=3)
with open("mario_file.json", 'w') as mario_file:
    mario_file.write(json_file)