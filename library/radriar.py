import re

def importFile(file_path): # Loads a file as a list into memory, removing newlines and white-spaces
    with open(file_path, 'r') as f:
        output = []
        for line in f:
            output.append(line.strip())
    return output

def extract(pattern, string): # Returns a string matching a regex
    search = re.search(pattern, string)
    target = search.group
    return target
