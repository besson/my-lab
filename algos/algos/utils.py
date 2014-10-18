def mount_from_file(_file):
    result = []
    for line in open(_file):
        result.append(int(line.strip()))

    return result