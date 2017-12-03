import os
import argparse
import tempfile
import json

def store(shared_dict, key, val):
    if key in shared_dict:
        shared_dict[key].append(val)
    else:
        shared_dict[key] = [val]

parser = argparse.ArgumentParser()
parser.add_argument("-key", "--key")
parser.add_argument("-val", "--val", required=False)
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if os.path.exists(storage_path) == True:

    if args.val is not None:
        with open(storage_path, 'r') as f:
            content = json.load(f)
            store(content, args.key, args.val)
        with open(storage_path, 'w') as f:
            json.dump(content, f)
    elif args.val is None:
        try:
            with open(storage_path, 'r') as f:
                content = json.load(f)
            if isinstance(content[args.key], list):
                print(', '.join(content[args.key]))
            else:
                print(content[args.key])
        except:
                print(None)

else:
    if args.val is None:
        print(None)

    data = {}
    with open(storage_path, 'w') as f:
        json.dump(data, f)
    with open(storage_path, 'r') as f:
        data = json.load(f)
        store(data, args.key, args.val)
    with open(storage_path, 'w') as f:
        json.dump(data, f)
