# -*- coding: utf-8 -*-
"""
<https://bitbucket.org/pypy/pypy/src/tip/lib_pypy/_sha256.py?fileviewer=file-view-default>

The following is Py3 implementation

SHA_DIGESTSIZE = 64
SHA_BLOCKSIZE = 32
class Mysha256(object):
    digest_size = digestsize = SHA_DIGESTSIZE
    block_size = SHA_BLOCKSIZE

    def __init__(self, s=None):
        self.name = 'sha256'
        self._sha = sha_init()
        if s:
            sha_update(self._sha, s)
    
    def update(self, s):
        sha_update(self._sha, s)
    
    def digest(self):
        return sha_final(self._sha.copy())[:self._sha['digestsize']]
    
    def hexdigest(self):
        return ''.join(['%.2x' % i for i in self.digest()])

    def copy(self):
        new = sha256.__new__(sha256)
        new._sha = self._sha.copy()
        return new
"""
import sys
import hashlib

SHA_DIGESTSIZE = 64
SHA_BLOCKSIZE = 32

is_py2 = sys.version[0] == '2'  # added py2&3 compatibility

sha = hashlib.sha256()
org_str = "hahaha"
if not is_py2:
    org_str = org_str.encode(encoding='utf8')
sha.update(org_str)
assert sha.digest_size == 32
# In Python3, cannot have 64L
# In Python3, int and long in Py2 has been mapped to int in Python
assert sha.block_size == 64  # https://stackoverflow.com/questions/23741762/why-does-python-add-an-l-on-the-end-of-the-result-of-large-exponents
rslt = sha.digest()
hexrslt = sha.hexdigest()
if is_py2:
    assert rslt == '\xbe\x17\x8c\x05C\xeb\x17\xf5\xf3\x040!\xc9\xe5\xfc\xf3\x02\x85\xe5W\xa4\xfc0\x9c\xce\x97\xff\x9c\xa6\x18)\x12'    
else:
    rslt_str = ''.join(r'\x%.2x' % x for x in rslt)
    rslt_lst = [x for x in rslt]
    assert rslt_lst[0] == 190
    # convert the list back to bytes array
    assert bytes(rslt_lst) == rslt
    
    # Note: in utf-8, code point of rslt_lst[0] is 190
    tmp = b'\xbe'
    assert type(tmp) == bytes
    assert len(tmp) == 1
    assert tmp[0] == 190
    assert tmp != '¾'  # note here is NOT equal
    assert tmp != 190  # bytes are not equivalent to its code point
    assert chr(tmp[0]) == '¾'
assert len(rslt) == sha.digest_size
assert hexrslt == 'be178c0543eb17f5f3043021c9e5fcf30285e557a4fc309cce97ff9ca6182912'

if is_py2:
    # NOTE: https://docs.python.org/2/library/functions.html#ord
    _hexrslt = ''.join(['%.2x' % ord(i) for i in rslt])
else:
    _hexrslt = ''.join('%.2x' % i for i in rslt)
    # or
    _hexrslt = ''.join('{:02x}'.format(i) for i in rslt)
assert hexrslt == _hexrslt
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    