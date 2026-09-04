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


def breakdownURI(uri):
    protocol = "https://" if "https://" in uri else "http://"
    uri = uri.replace(protocol, "")
    uri  = uri.partition("/")
    domain = uri[0]
    path = uri[1] + uri[2]

    output = {
        "protocol": protocol,
        "domain": domain,
        "path": path
    }
    return output
