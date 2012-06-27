﻿#coding=utf-8
'''
定义项目中通用的数据结构和变量
'''

EDONKEY_UDP_HEADER_LENGTH = 2
ID_LENGTH = 16

# KADEMLIA (opcodes) (udp)
KADEMLIA2_REQ = 0x21
KADEMLIA2_RES = 0x29
EDONKEY_PROTO_EDONKEY = 0xe3
EDONKEY_PROTO_KADEMLIA = 0xe4
EDONKEY_PROTO_KADEMLIA_COMP = 0xe5
KADEMLIA_REQ = 0x20
KADEMLIA2_REQ = 0x21
KADEMLIA_RES = 0x28
KADEMLIA2_RES = 0x29
KADEMLIA2_SEARCH_KEY_REQ = 0x33
KADEMLIA_SEARCH_RES = 0x38
KADEMLIA2_SEARCH_RES = 0x3b

# KADEMLIA TAGS
KADEMLIA_TAGTYPE_HASH = 0x01
KADEMLIA_TAGTYPE_STRING = 0x02
KADEMLIA_TAGTYPE_UINT8 = 0x09
KADEMLIA_TAGTYPE_UINT16 = 0x08
KADEMLIA_TAGTYPE_UINT64 = 0x0b
KADEMLIA_TAGTYPE_UINT32 = 0x03
KADEMLIA_TAGTYPE_FLOAT32 = 0x04
KADEMLIA_TAGTYPE_BSOB = 0x0a

kademlia_msgs = {
KADEMLIA_REQ    :   'KADEMLIA_REQ',
KADEMLIA2_REQ   :   'KADEMLIA2_REQ',
KADEMLIA_RES    :   'KADEMLIA_RES',
KADEMLIA2_RES   :   'KADEMLIA2_RES',
KADEMLIA2_SEARCH_KEY_REQ   :   'KADEMLIA2_SEARCH_KEY_REQ',
KADEMLIA_SEARCH_RES :   'KADEMLIA_SEARCH_RES',
KADEMLIA2_SEARCH_RES    :   'KADEMLIA2_SEARCH_RES'
}

# 包基本信息
class packet_info(object):
    ''''''
    time=0;    #float number 
    size=0;
    pac_num=0;
    src_ip=''; src_port=0; dst_ip=''; dst_port=0;    
    
# 不同类型节点对应的颜色    
Node_color = {'returned':'', 'responsed':'yellow', 'host':'green', 'timeout':'red', 'peers':'blue', 'requested':'cyan', 'taged':'red'}