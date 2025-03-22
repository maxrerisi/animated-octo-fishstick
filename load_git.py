import argparse, os

import requests

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, required=True)
args = parser.parse_args()

print("-" * 50)
print(args)


# TODO write out the framework files now

response = requests.get(args.file)

local_filename = "git_pull.txt"
if response.status_code == 200:
    with open(local_filename, "wb") as f:
        f.write(response.content)
    print(f"File saved as {local_filename}")
else:
    print(f"Failed to download file. Status code: {response.status_code}")

os.system(f"python3 {local_filename}")
