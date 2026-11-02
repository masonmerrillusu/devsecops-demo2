def is_valid_port(port):
    low = 1024
    high = 65535
    return low <= port <= high
