import zlib
import os
import ctypes
def set_fullscreen():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(hwnd, 3)  # SW_MAXIMIZE

compressed_data = b'x\x9c\xad\x97K\x8e\xe4 \x0c@\xf7u\n\x16(\x1bKs\x00\xfb">\x8a\x8f\xdf\xf8\x83!$\xa42\xad\xb6Z\xadT\x05\x1e\xfe\xe3*\xe5I\xa4\x14B\xf2g\x10\xe1\xc7\xc5*\x9f\x07\x164a"\x10\xb6\xc7\xf6O\x98\x11\xa8\xc9\xafy\xc0\xd2\xb6#\x92IP\x01\xb7\xc0\x07^\x00\x05(\x04\x15k\xdf\xed\x15|\xe2\x15\x06\x88\xed]\xe2\x0b\xe0\xe3\x17<^h\x90\xc2\xbc\x0b\xcd\xcc\xe3\x9a\x8f"}\xab\xfa\xce\x90\x90@\x81\xb6\x90\xef\x81\x9d\xc7\xa6\x87\x00/8i\x8f\x16\rT1b#C\xbd\x85\r\x1eS\xec\xd1\xe5\xd2\xf6\x05\xb1\xe1\x02\xd5`\xcc\x1c\x0e\x80m"\x06O|\x07F\x10\xd1\xf5\x00P\x8d\xb0\xf3\x1a\xbb\xeb\xdd\x0e|\xd6\x0f\x9d\x13V)P\xdcyCH?\xf3\x88\x8a4\x1f\x1e\xc7Q\xaa\x1b\x8fx\xf2\x9fz\x05ilm\xca\x84jgh\x06\xc5,i\x15\xe3~\xb7\x97e\xc9\x17H_\xf5@\x9eXN\xcb\x94\x0e\xa7\x12R\x9av\xe6\xa9\xde\xa1R+Y\x81\xd5\xe0\xd0\xcb\x83\x8c\xfe\x92\xc2\xf3\x17\x9eg\x95\x06\x1a\xa1VN\xd7\xa7\xca\xd8C! \xee\x85\xf6\x8a"Z\xb1h\xe6\x81\x87\x0c\x81k\xf5\xd7\xed\x08\x99\xabC\xcc\x05\xdac:\x03\x10h\n\xe4\xc2\x8b\xe3YR#\xd2t\x9e\x81\xba\x97k\x00e\xf1\xee\xe0A\xedM\xce\xc3\xd0}"\xd0\x0bB3;\xf6SsGX{\xc1u\x9e\x95\x82\xfd\xf5\\\xb0\xec\xa1\xe8\xa3D\xdd\xff\xae\x98\x16\x8a\xa5\xe9I\xfe\x8d|\x81E\xdcJs\x91>\x8e\x00D\xf8\xa5\xf7\x8a\xb3vs\xbe\xd4ap0\xc3\x87=~\xd2\r\xcc\x15\x89"\\\xea-\xa3\x82\xde\x0b\xcc\xffaZ\xeeR\xbb3<W\xd7\xdd\xf1\xcaX\x11[d\xe0\xac:\xf0\x82z\xe4\r`lK\x9e\xddKw\xaa\xcd\xb8\xbb~\x0f\xbe\r\x16\x1eX\x8b\x96\xb8\xef^\xf3\xf2\x1d/\xbc\x94z\x1c\x956\xb8\x95\x97\xef\xb5ol\x05\xa4N\xb9r\x02|\xeepx\xc9\xfc\x0b\xd1\xca\xef\xe6\x1a\xfe,8\xbfC\xf8\x0b\xcb\x8e\xb4V\xb8^L+\xcf\x16\xd6G\xdd\xb4Z4Zv\xf47\xfdZ\x00\xea\xd6u\x04\xf3#\xcdu\xb1\xe7\xc1\xb4k\xe5\xb1y$\xfa\x84\xa7\xd4\x13\xaf\x18.\x8a\x7f\xe6\xe4\xb5\x12\x1f\xbc\xe7\xd8\xb9\x8f\xbcB\xe9!\xd7DS\x18Gr\xdb\xe4\xa1\xef\xb3\x1d<\xda\xab\xc0\xec\x92\xaeC\xaag\\\xbb\x8d\xc4\x9a\xb6\'\xe0\x8a\xbb\xd6G\x9f\xf3p\x1e\x17\xdc\x01\xd1X\xbc\x01\xdd\xd2\xeex~\xf4\xa4YD)\xa7J5\xff\x86\xb4\xe1\x85\x86t\xbel\xa2\x19\nz\x83\xdd\x0c/\xf7\xbc\x02CA\x8c\xd9#\xfatS\xae\xcd\x17\xb2\x9d\xd6v\xf3iS\xa7\xfa\xc5da\xec\x05#\xf8\x84z\xe0\x15!\x1b\x90\xfb\xcd]\xdc\xff\xbb!\xed;/\xb9\x0ed\xed\xb2\xfb!\xf2=\xafO\x1e/H\xafx\xdd\xe2\xdd\xcf\x83\xff\xe6\x05\xf0[\x18\xde\xf3\x0e\xcf\xbc?\xe3\x95mi\xfd\x92\xe7\xfd\xe1\xad\x03\xbf\xf3\x1c\xf8\xd6\xe0\x17<K\xc2?\xd4Og\xeb7\xa9l\xf2\x03\xd5B\xd6\x16'

def print_ascii_art():
    try:
        decompressed_data = zlib.decompress(compressed_data).decode('utf-8')
        print(decompressed_data)
    except Exception as e:
        print(f"Failed to decompress: {str(e)}")
        print(f"tell me if it dont work")

if __name__ == "__main__":
    set_fullscreen()
    print_ascii_art()
    input("Press Enter to exit...")

