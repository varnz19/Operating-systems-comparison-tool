def scan(requests, head, disk_size):
    requests = sorted(requests)
    seek_time = 0
    current = head
    order = [head]
    
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    
    for r in right:
        seek_time += abs(current - r)
        current = r
        order.append(current)
    
    seek_time += abs(current - (disk_size - 1))
    current = disk_size - 1
    order.append(current)
    
    for r in reversed(left):
        seek_time += abs(current - r)
        current = r
        order.append(current)
    
    return seek_time, order