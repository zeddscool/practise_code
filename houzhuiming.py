def get_suffix(filename):
    index = filename.rfind('.')
    if  0< index < len(filename) - 1:
        suffix = filename[index:]
    return suffix

