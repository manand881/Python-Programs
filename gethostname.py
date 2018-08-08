# Get the name of the host on which the routine is running

import socket
host_name = socket.gethostname()
print("\nHost name:", host_name,"\n")