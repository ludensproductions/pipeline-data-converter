
# ['a|b|c', '1|2|3', '4|5|6'] => [{'a':'1','b':'2','c':'3'},{'a':'4','b':'5','c':'6'}]
import json
import csv
import pandas as pd


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

    # Convert Json to CSV
    df = pd.DataFrame.from_dict(json_data)
    df.to_csv (r'exports/Export.csv', index = False, header=True)

    # Using a JSON string
    with open('exports/json_data.json', 'w') as outfile:
        json.dump(json_data, outfile, indent=4)

    return json_data

# Reads file with pipelines, converts it to JSON-like dictionary
def PPFileToJson(name):
    with open(name, encoding='utf-8') as file:
        lines = file.readlines()
        return PPToJson(lines)

if __name__ == "__main__":
    json_data = PPFileToJson('ci_aduana.txt')
    json_test = json.dumps(json_data)