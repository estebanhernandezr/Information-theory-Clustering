import sys
sys.path.insert(0, 'python/transmitters/hartley/encoder')
sys.path.insert(1, 'python/transmitters/hartley/decoder')

from Encoder import Encoder
from Decoder import Decoder

def run():
    codificador = Encoder(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1'])
    flujo_codificado = codificador.encode('nigganigganigganiggganigggaonehundredpercent')

    decodificador = Decoder(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1'])
    print(decodificador.decode(flujo_codificado))

    return 0

run()