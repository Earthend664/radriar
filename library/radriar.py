def importFile(file_path):
    with open(file_path, 'r') as f:
        output = []
        for line in f:
            output.append(line.strip())
    return output
