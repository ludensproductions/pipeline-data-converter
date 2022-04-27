
# ['a|b|c', '1|2|3', '4|5|6'] => [{'a':'1','b':'2','c':'3'},{'a':'4','b':'5','c':'6'}]
import json
import csv
import pandas as pd


# Function used to convert a list of lines to JSON-like dictionary
def PPToJson(lines):
    # Obtain the keys
    names = lines[0].strip().split('|')
    lines.pop(0)

    def lineToJson(line):
        nxt = {}
        values = line.strip().split('|')
        for idx,name in enumerate(names):
            nxt[name] = values[idx]
        return nxt

    json_data = list(map(lambda x: lineToJson(x), lines))


    # --- Beginning: REMOVE THIS IF YOU DON'T WANT TO SAVE THE CSV/JSON FILE ---

    # Convert Json to CSV and store it in 'exports' folder
    df = pd.DataFrame.from_dict(json_data)
    df.to_csv (r'exports/Export.csv', index = False, header=True)

    # Convert Json-like dictionary to a JSON file and store it in 'exports' folder
    with open('exports/json_data.json', 'w') as outfile:
        json.dump(json_data, outfile, indent=4)

    # --- End: REMOVE THIS IF YOU DON'T WANT TO SAVE THE CSV/JSON FILE ---


    return json_data

# Reads file with pipelines, runs the above function to convert it to a JSON-like dictionary
def PPFileToJson(name):
    with open(name, encoding='utf-8') as file:
        lines = file.readlines()
        return PPToJson(lines)

if __name__ == "__main__":
    # Reads the file with pipeline-separated data and stores a JSON-like dictionary in our variable
    json_data = PPFileToJson('ci_aduana.txt')

    # Convert our json-like dictionary to a JSON object (and pretty print it with 4 spaces as indentation)
    json_object = json.dumps(json_data, sort_keys=False, indent=4)