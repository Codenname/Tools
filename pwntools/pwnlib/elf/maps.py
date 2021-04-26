from __future__ import absolute_import

# Pre-assembled shellcode for each architecture.
#
# This is literally the output of:
#     shellcraft $ARCH.linux.cat /proc/self/maps
#     shellcraft $ARCH.linux.syscalls.exit 0
CAT_PROC_MAPS_EXIT = {
    'i386':
        '680101010181342460717201686c662f6d68632f7365682f70726f89e331c931d26a0558cd806a015b89c131d268ffffff7f5e31c0b0bbcd80'
        '31db6a0158cd80',
    'amd64':
        '48b801010101010101015048b86d672e6c607172014831042448b82f70726f632f7365506a02584889e731f6990f0541baffffff7f4889c66a28586a015f990f05'
        '31ff6a3c580f05',
    'arm':
        '617007e3737040e304702de56c7606e32f7d46e304702de5637f02e3737546e304702de52f7007e3727f46e304702de50d00a0e1011021e0022022e00570a0e3000000ef0010a0e10100a0e3022022e00231e0e3bb70a0e3000000ef'
        '000020e00170a0e3000000ef',
    'thumb':
        '004f01e0617073ff4fea07274fea172780b4dff8047001e06c662f6d80b4dff8047001e0632f736580b4dff8047001e02f70726f80b4684681ea010182ea02024ff0050741df05464ff00100294682ea02026ff000434ff0bb0741df'
        '80ea00004ff0010741df00bf',
    'mips':
        '726f093c2f702935f0ffa9af7365093c632f2935f4ffa9af2f6d093c6c662935f8ffa9af8cff193c9e8f393727482003fcffa9aff0ffbd272020a003ffff0528ffff0628a50f02340c010101feff192427202003fcffa2affcffa58fffff0628ff7f073cffffe7346f1002340c010101'
        'ffff0428a10f02340c010101',
    'aarch64':
        'ee058ed24eeeadf26eecc5f26eaeecf28fcd8cd2efa5adf22f0ccef26f0ee0f2ee3fbfa980f39fd2e0ffbff2e0ffdff2e0fffff2e1030091e2031faae3031faa080780d2010000d4e10300aa200080d2e2031faae3ff9fd2e3ffaff2e80880d2010000d4'
        'e0031faaa80b80d2010000d4',
}
