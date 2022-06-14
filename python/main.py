import sys
sys.path.insert(1, 'python/classes/LZ77')

import slate3k as slate
from CoderLZ77 import CoderLZ77


path: str = 'python\data\German [Germany].pdf'
with open(path, 'rb') as f:
    txt = slate.PDF(f)
string: str = str(txt)

codificador = CoderLZ77(n=10, l=5, alphabet=['A', 'T', 'G', 'U', 'X', 'Y', 'Z'])
codificador.codify(string, symb='_')
coded_string: str = codificador.codified_string

print(coded_string)