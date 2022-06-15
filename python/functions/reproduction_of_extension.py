def reproduce_extension(string: str, pos: int, size: int, char: chr):
    extension = ''
    for i in range(pos, pos+size):
        string += string[i]
        extension += string[i]
    return extension + char