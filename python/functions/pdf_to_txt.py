from typing import BinaryIO, Dict, Sequence, Tuple
import slate3k as slate

def pdf_to_txt(pdf_path: str):
    with open(pdf_path, 'rb') as f:
        txt: str = slate.PDF(f)

    txt: str = str(txt)
    return txt