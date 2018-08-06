# Get height and the width of console window

# def terminal_size():
#     import fcntl, termios, struct
#     th, tw, hp, wp = struct.unpack('HHHH',
#         fcntl.ioctl(0, termios.TIOCGWINSZ,
#         struct.pack('HHHH', 0, 0, 0, 0)))
#     return tw, th

# print('Number of columns and Rows: ',terminal_size())

# above solution is broken

import shutil
wh = shutil.get_terminal_size()
print("terminal size is %d x %d" % wh)