from typing import BinaryIO, Dict, Sequence, Tuple, List
from bitarray import *

def data_from_file(filename: str) -> BinaryIO:
    with open(filename, 'rb') as input_file:
        filedata = input_file.read()
    return filedata

def file_from_bin(filename: str, buffer: bytearray) -> None:
    with open(filename, 'wb') as outfile:
        outfile.write(buffer)
        return None

def bin_from_file(filename: str) -> BinaryIO:
    filedata: bytearray = bitarray(endian='big')
    with open(filename, 'rb') as input_file:
        filedata.fromfile(input_file)
    return filedata