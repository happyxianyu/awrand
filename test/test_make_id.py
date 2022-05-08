import logging
from awrand import *


def test_make_id():
    n = 10000
    ids_int = [make_id_int() for i in range(n)]
    ids_bytes = [make_id_bytes() for i in range(n)]
    ids_str = [make_id_str() for i in range(n)]
    for ids in [ids_int, ids_bytes, ids_str]:
        assert(len(set(ids)) == n)


