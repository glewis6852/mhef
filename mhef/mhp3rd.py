DATA_ENCODE_TABLE = b'\xc0\xa8\xca\x07KnHo\xd6\x921,\x9d\xfb\xe1Pa\xc6\xe4R>\x12\xad3\xae\xeb\xf3/ki{S\x96\xc4\xb1\x9c\x1c\xc5 \x86\x19\x13\xe9j&ux\x8cC\xedzf]\x18\x1d\xe8p\xa5^\xf2_X\x05F\r\x97\x9e|\xeae\xdd$\x8fIB\xaf\xf4%\xb8+\x08r\x17\xd9\xa4\xd3\x93q[@\xb2.\x0b~L\x04\xf7\x11\xc17y\xa7)\xbc\x1bV\x8b\xfa\x8d6;m\xd4W\x83\xbd\x1f\xd7b\x84\xf5\xda\xd5\xab\xcc\xa2G\x88\x9a-\xc7\xdf\xcb\x02(A\xa9=\xd8\xa1#<\x81l\\\xd0h\xc9\xbf\x99\x01\xbe\xf9\xfc\xec\xb7\n\x82\x89\xdc\x91\xef\x14\xcf4J\x03\xd1\xba5\x8a\x06\xff8\xa0\xf0\xce}\x0cv\xc2\xb3\xac\t\x94UT\x80\xa3\x95\xbb\xa60*\xf6g\x1e\xfewcd\x87`\x00\xb0\x98D\xeeM\xe5\xc3\xcdQ"s\x9b\xe0\x1at\xc8Z?N\xe6\xaa\x7f!\xf1Y\x9f\xb9\x90O\xe2\xfd\xb4\x16\xe3\xf8\x0e\xe7\x15\x859:\xde\x0f\xd2\xb6\x8e\'\xdb\xb52E\x10'
DATA_DECODE_TABLE = b'\xcb\x96\x85\xa6_>\xab\x03P\xb7\x9c\\\xb2@\xef\xf6\xffa\x15)\xa2\xf1\xecR5(\xd9h$6\xc4t&\xe2\xd5\x8cGM,\xfa\x86f\xc1O\x0b\x81[\x1b\xc0\n\xfd\x17\xa4\xa9mc\xad\xf3\xf4n\x8d\x89\x14\xddY\x87J0\xce\xfe?~\x06I\xa5\x04^\xd0\xde\xe8\x0f\xd4\x13\x1f\xba\xb9iq=\xe4\xdcX\x904:<\xca\x10v\xc7\xc8E3\xc3\x92\x1d+\x1c\x8fo\x05\x078WQ\xd6\xda-\xb3\xc6.d2\x1eC\xb1]\xe1\xbb\x8e\x9drw\xf2\'\xc9\x7f\x9e\xaaj/l\xf9H\xe7\xa0\tV\xb8\xbd A\xcd\x95\x80\xd7#\x0cB\xe5\xae\x8b}\xbcT9\xbfe\x01\x88\xe0{\xb6\x16\x18K\xcc"Z\xb5\xeb\xfc\xf8\x9bN\xe6\xa8\xbegs\x97\x94\x00b\xb4\xd2!%\x11\x82\xdb\x93\x02\x84|\xd3\xb0\xa3\x91\xa7\xf7Upz\x08u\x8aSy\xfb\x9fF\xf5\x83\xd8\x0e\xe9\xed\x12\xd1\xdf\xf07*D\x19\x9a1\xcf\xa1\xaf\xe3;\x1aLx\xc2`\xee\x98k\r\x99\xea\xc5\xac'
DATA_KEY_DEFAULT = (0x2345, 0x7f8d)
DATA_KEY_MODIFIER = (0xffd9, 0xfff1)
DATA_EXCEPTIONS = (17, 18, 19, 20, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92)


SAVEDATA_ENCODE_TABLE = b'\xa9<\xdd\x96\xfe\x8e\x07\xcd\xdf\xa2\x87\x82\xd4\x84\xb5}\xe4\xf7\xf0\xa5Mz\r\x11=\xffB\xb8\x13\xfc\xd1\xf5O\x01\x02l1c7G\x19"\xb9\x86\xf1\x1f\x0f5\xce(&\x0e*\x9aQ\xb4\x91\x17XS\\\x04\xeb\x8btV\xb2\xe9\x9c0Yg\x97\xd3LA\xbf-\xb3R\x12\xfb|\xa0\t\xa6q\xcb{8\x10DZk\x8a\x1eu+!^\xda\xed`\x7f\x8d\xc3\xa3\xea\xdew\xef\xe0)\x8cn\x16i\x0b\n\xa4 \xbaC\xca\x9d~e\x93\x89o\x9e\x95_W\x8f\x08\xbe\xe2\xdbjp\xe6\xf8m\xcc\xe8\xcf\x9f\xf2?\xaf\xfd\x1d\xf3Nh\xaa\xb7\xad\x889>v\xa1\xd6;\x00\xb0\xe5\xbdd\xc1\xc6K,\x15y\xf9J\xd8\xab\x18\xc9\xd0\xd5P\xe7\x90\xae:\xa8\xbb\xe3\xc8/fa\xc2r\xdc\xf6#T[\'\x1c\x92\x83\xc0\xc4\x81\x98s\xec\x8546\x1a\xd2E\xbc\xa7\x14\x9b\xee\xc5\xb1\xacUxH\xfa\xf4\xc7%b]\x0c@\x80F\x1b\xd9\x94I\x06\xb6\xe12\x03\x99\x053$.\xd7'
SAVEDATA_DECODE_TABLE = b'\xa6!"\xf9=\xfb\xf5\x06\x87Tvu\xed\x163.Z\x17P\x1c\xde\xafs9\xb5(\xd9\xf1\xcd\x98_-xb)\xc9\xfd\xea2\xcc1p4a\xaeM\xfe\xc2E$\xf8\xfc\xd7/\xd8&Y\xa0\xbd\xa5\x01\x18\xa1\x95\xeeK\x1az[\xdb\xf0\'\xe6\xf4\xb2\xadJ\x14\x9a \xb96O;\xca\xe4A\x85:F\\\xcb<\xecc\x84f\xc4\xeb%\xaa~\xc3G\x9bt\x8b]#\x8fr\x81\x8cV\xc6\xd4@`\xa2m\xe5\xb0\x15XR\x0f}g\xef\xd2\x0b\xcf\r\xd6+\n\x9f\x80^?qh\x05\x86\xbb8\xce\x7f\xf3\x83\x03H\xd3\xfa5\xdfD|\x82\x93S\xa3\tjw\x13U\xdd\xbe\x00\x9c\xb4\xe3\x9e\xbc\x96\xa7\xe2BN7\x0e\xf6\x9d\x1b*y\xbf\xdc\xa9\x88L\xd0\xab\xc5i\xd1\xe1\xac\xe9\xc1\xb6{W\x90\x070\x92\xb7\x1e\xdaI\x0c\xb8\xa4\xff\xb3\xf2d\x8a\xc7\x02l\x08o\xf7\x89\xc0\x10\xa8\x8d\xba\x91Ck>\xd5e\xe0n\x12,\x94\x99\xe8\x1f\xc8\x11\x8e\xb1\xe7Q\x1d\x97\x04\x19'
SAVEDATA_KEY_DEFAULT = (0xdfa3, 0x215f)
SAVEDATA_KEY_MODIFIER = (0xffef, 0xff8f)
SAVEDATA_HASH_SALT = b'VQ(DOdIO9?X3!2GmW#XF'


PSPSAVEDATA_KEY = b"\xe3\x05\xce\xfa\xebF\xb01\x85\x9a'[\xdf2\xd8c"


QUEST_KEY_DEFAULT = (0xffa9, 0xff9d, 0xfff1, 0xffc7)
QUEST_KEY_MODIFIER = (0x3df3, 0x1709, 0xb381, 0x747b)
QUEST_HASH_SALT = b'sR2Tf4eLAj8b3TH7'

