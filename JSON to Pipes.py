
# ['a|b|c', '1|2|3', '4|5|6'] => [{'a':'1','b':'2','c':'3'},{'a':'4','b':'5','c':'6'}]
import json
import csv
import pandas as pd


# [{'a':'1','b':'2','c':'3'},{'a':'4','b':'5','c':'6'}] => 'a|b|c\n1|2|3\n4|5|6'
def JsonToPP(data):
    if len(data) <= 0:
        return ''

    names = data[0].keys()

    # Converts { 'a': 1, 'b': 2, 'c': 3, 'd':4 } => 1|2|3|4
    def objToPP(obj):
        parts = []
        for name in names:
            parts.append(obj[name])
        return '|'.join(parts)

    return '|'.join(names) + '\n' + '\n'.join(map(lambda x: objToPP(x), data))

if __name__ == "__main__":
    
    # Opening the JSON file
    with open('exports/json_data.json') as json_file:
        json_dict = json.load(json_file)

    # Convert the JSON to pipes-separated values and store it in a variable
    pp = JsonToPP(json_dict)

    # Save the pipeline-separated data in a file
    python_file = open("pipelineReverted.txt", "w")
    python_file.write(f'{pp}')
    python_file.close()

    # Use the pipeline-separated data for whatever you want
    #pp