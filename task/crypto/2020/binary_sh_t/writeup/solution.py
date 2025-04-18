gamma = b"\x9a\x9a\x95\xb3\x7a\x8f\xe2\xf2\xf3\xa4\x3a\x6d\xaa"+\
b"\xe2\x30\x16\x98\xf5\x41\x17\x1a\x13\x03\x4e\xf2\xe2\xc4\x15\xa0\x40\xcf"+\
b"\x8b\x9b\x39\x9b\x00\x45\x1e\x3c\x75\x8e\xa0\x73\x4d\x60\x67\xe9\x1b\x75"+\
b"\x79\x83\xf9\x43\x27\x70\x34\x41\xfa\x5a\xf2\x70\xba\xd3\xf1\x2b\x05\x35"+\
b"\x02\xf3\x4d\xdd\xde\x6d\x4c\xf0\xc8\x4e\xd5\xd3\x32\x73\x11\x43\x89\x2b"+\
b"\xf8\x0b\x70\xc2\xa4\x90\x57\xfb\xa7\x5d\xf8\x35\x95\x0a\xd6\x03\x03\x9c"+\
b"\xad\xeb\xb5\x84\x43\xeb\xf5\x0f\x19\xfb\xe7\x59\xcf\xdc\x87\x1c\x46\x9e"+\
b"\x29\x63\x3a\xbc\x32\x3e\xd9\x7e\xfc\xb8\x0c\xa6\x1e\xc3\xfd\x15\x29\x5b"+\
b"\x9f\xa2\xa8\xf0\xff\x7d\xb4\xb9\x93\x98\xce\x0b\xf8\xe1\x0a\x5b\x7c\x27"+\
b"\x6b\x25\xc2\x1a\xc6\x18\x9b\x04\xf8\x64\x8f\x95\x41\xe8\xaa\x68\x88\xa8"+\
b"\xd5\xed\x3c\xe4\x22\xd0\x8a\xf1\x1b\x8f\x12\xd7\x20\x5a\xd4\x2e\xbc\xdf"+\
b"\x9b\xe2\x97\xeb\xb7\x76\xdc\x19\x7f\x24\x6a\x3e\x55\x9c\xfe\x09\x4f\x27"+\
b"\xbc\x5a\xb0\x45\x46\xa6\xa0\xd1\x3a\x99\xe3\x1c\x2b\x3c\xc2\xe2\xef\x15"+\
b"\x3c\xfa\x23\x53\x77\xb7\x6c\x6c\x6f\xfa\x90\xcd\x1f\xb5\x37\xc1\x6b\x67"+\
b"\xd5\xcd\x6f\xc7\xa8\xd3\xc4\xdd\x14"

def encode(flag):
    flag = flag.ljust(256,b"\x00")
    flag = list(flag)
    for i in range(256):
        flag[i]^= gamma[i]
        flag[i] = SWAP_BITS(flag[i], 3, 4)
        flag[i] = SWAP_BITS(flag[i], 2, 7)
        flag[i] = SWAP_BITS(flag[i], 0, 5)
        flag[i] = (flag[i]*67)&0xff
        flag[i] = SWAP_BITS(flag[i], 5, 2)
        flag[i] = SWAP_BITS(flag[i], 3, 0)
        flag[i] = SWAP_BITS(flag[i], 7, 4)
    return flag
	
	
def decode(flag):
    for i in range(256):
        flag[i] = SWAP_BITS(flag[i], 5, 2)
        flag[i] = SWAP_BITS(flag[i], 3, 0)
        flag[i] = SWAP_BITS(flag[i], 7, 4)
        flag[i] = (flag[i]*107)&0xff
        flag[i] = SWAP_BITS(flag[i], 3, 4)
        flag[i] = SWAP_BITS(flag[i], 2, 7)
        flag[i] = SWAP_BITS(flag[i], 0, 5)
        flag[i]^= gamma[i]
    return flag

"".join(list(map(lambda x:chr(x),decode(encode(b"ctfcup{7ddc0a0bb04fcbf4d6f330d95dd22c2d}")))))